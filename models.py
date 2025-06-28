from app import db
from datetime import datetime
from sqlalchemy import func

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.Date, nullable=True)
    priority = db.Column(db.String(10), nullable=False, default='Medium')  # Low, Medium, High
    completed = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f'<Task {self.title}>'
    
    def get_priority_class(self):
        """Return Bootstrap class for priority styling"""
        priority_classes = {
            'Low': 'text-success',
            'Medium': 'text-warning', 
            'High': 'text-danger'
        }
        return priority_classes.get(self.priority, 'text-secondary')
    
    def get_priority_badge_class(self):
        """Return Bootstrap badge class for priority"""
        priority_classes = {
            'Low': 'badge bg-success',
            'Medium': 'badge bg-warning', 
            'High': 'badge bg-danger'
        }
        return priority_classes.get(self.priority, 'badge bg-secondary')
    
    def is_overdue(self):
        """Check if task is overdue"""
        if self.due_date and not self.completed:
            return self.due_date < datetime.now().date()
        return False
