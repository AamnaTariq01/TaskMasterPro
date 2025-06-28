from flask import render_template, request, redirect, url_for, flash, jsonify
from app import app, db
from models import Task
from forms import TaskForm, FilterForm
from datetime import datetime
from sqlalchemy import or_, desc, asc

@app.route('/')
def index():
    filter_form = FilterForm()
    
    # Get filter parameters from URL
    search = request.args.get('search', '')
    status = request.args.get('status', 'all')
    priority = request.args.get('priority', 'all')
    sort_by = request.args.get('sort_by', 'created_desc')
    
    # Set form values from URL parameters
    filter_form.search.data = search
    filter_form.status.data = status
    filter_form.priority.data = priority
    filter_form.sort_by.data = sort_by
    
    # Build query
    query = Task.query
    
    # Apply search filter
    if search:
        query = query.filter(or_(
            Task.title.contains(search),
            Task.description.contains(search)
        ))
    
    # Apply status filter
    if status == 'pending':
        query = query.filter(Task.completed == False)
    elif status == 'completed':
        query = query.filter(Task.completed == True)
    
    # Apply priority filter
    if priority != 'all':
        query = query.filter(Task.priority == priority)
    
    # Apply sorting
    if sort_by == 'created_desc':
        query = query.order_by(desc(Task.created_at))
    elif sort_by == 'created_asc':
        query = query.order_by(asc(Task.created_at))
    elif sort_by == 'due_date_asc':
        query = query.order_by(Task.due_date.asc().nullslast())
    elif sort_by == 'due_date_desc':
        query = query.order_by(Task.due_date.desc().nullsfirst())
    elif sort_by == 'priority_desc':
        # High, Medium, Low
        query = query.order_by(
            db.case(
                (Task.priority == 'High', 3),
                (Task.priority == 'Medium', 2),
                (Task.priority == 'Low', 1)
            ).desc()
        )
    elif sort_by == 'priority_asc':
        # Low, Medium, High
        query = query.order_by(
            db.case(
                (Task.priority == 'High', 3),
                (Task.priority == 'Medium', 2),
                (Task.priority == 'Low', 1)
            ).asc()
        )
    
    tasks = query.all()
    
    # Calculate statistics
    total_tasks = Task.query.count()
    completed_tasks = Task.query.filter(Task.completed == True).count()
    pending_tasks = total_tasks - completed_tasks
    overdue_tasks = Task.query.filter(
        Task.due_date < datetime.now().date(),
        Task.completed == False
    ).count() if Task.query.filter(Task.due_date.isnot(None)).count() > 0 else 0
    
    stats = {
        'total': total_tasks,
        'completed': completed_tasks,
        'pending': pending_tasks,
        'overdue': overdue_tasks,
        'completion_rate': round((completed_tasks / total_tasks * 100) if total_tasks > 0 else 0, 1)
    }
    
    return render_template('index.html', tasks=tasks, filter_form=filter_form, stats=stats)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            due_date=form.due_date.data,
            priority=form.priority.data,
            completed=form.completed.data
        )
        db.session.add(task)
        db.session.commit()
        flash('Task added successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_task.html', form=form, title='Add New Task')

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    form = TaskForm(obj=task)
    
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.due_date = form.due_date.data
        task.priority = form.priority.data
        task.completed = form.completed.data
        task.updated_at = datetime.now()
        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('edit_task.html', form=form, task=task, title='Edit Task')

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    task.updated_at = datetime.now()
    db.session.commit()
    
    status = 'completed' if task.completed else 'pending'
    flash(f'Task marked as {status}!', 'success')
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found_error(error):
    flash('Task not found.', 'error')
    return redirect(url_for('index'))

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    flash('An internal error occurred. Please try again.', 'error')
    return redirect(url_for('index'))
