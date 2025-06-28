from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Optional
from datetime import datetime

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=200)])
    description = TextAreaField('Description', validators=[Optional(), Length(max=1000)])
    due_date = DateField('Due Date', validators=[Optional()], format='%Y-%m-%d')
    priority = SelectField('Priority', 
                          choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')],
                          default='Medium',
                          validators=[DataRequired()])
    completed = BooleanField('Completed')
    submit = SubmitField('Save Task')

class FilterForm(FlaskForm):
    search = StringField('Search tasks...', validators=[Optional()])
    status = SelectField('Status', 
                        choices=[('all', 'All Tasks'), ('pending', 'Pending'), ('completed', 'Completed')],
                        default='all')
    priority = SelectField('Priority',
                          choices=[('all', 'All Priorities'), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')],
                          default='all')
    sort_by = SelectField('Sort by',
                         choices=[('created_desc', 'Newest First'), ('created_asc', 'Oldest First'), 
                                ('due_date_asc', 'Due Date (Earliest)'), ('due_date_desc', 'Due Date (Latest)'),
                                ('priority_desc', 'Priority (High to Low)'), ('priority_asc', 'Priority (Low to High)')],
                         default='created_desc')
