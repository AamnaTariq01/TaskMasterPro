# Todo List Application - Architecture Guide

## Overview

This is a Flask-based todo list application that provides users with a simple yet effective task management system. The application follows a traditional MVC (Model-View-Controller) pattern and uses SQLAlchemy ORM for database operations with SQLite as the backend storage.

## System Architecture

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Forms**: Flask-WTF for form handling and validation
- **Templating**: Jinja2 templates with Bootstrap for UI components

### Frontend Architecture
- **CSS Framework**: Bootstrap with Replit Dark Theme
- **Icons**: Feather Icons for consistent iconography
- **JavaScript**: Vanilla JavaScript for client-side interactions
- **Responsive Design**: Mobile-first approach using Bootstrap's grid system

### Application Structure
The application follows a modular structure with clear separation of concerns:
- `app.py`: Application factory and configuration
- `models.py`: Database models and business logic
- `routes.py`: URL routing and request handling
- `forms.py`: Form definitions and validation
- `templates/`: HTML templates
- `static/`: CSS and JavaScript assets

## Key Components

### Task Model
- **Purpose**: Core data model representing todo tasks
- **Features**: Title, description, due date, priority levels, completion status
- **Methods**: Priority styling helpers, overdue detection
- **Timestamps**: Automatic creation and update tracking

### Form System
- **TaskForm**: Main form for creating and editing tasks
- **FilterForm**: Advanced filtering and sorting capabilities
- **Validation**: Server-side validation with Flask-WTF

### Routing System
- **Index Route**: Main dashboard with filtering and statistics
- **CRUD Operations**: Create, read, update, delete tasks
- **AJAX Support**: Prepared for asynchronous operations

### User Interface
- **Dark Theme**: Replit-compatible dark theme implementation
- **Responsive Layout**: Mobile-optimized design
- **Interactive Elements**: Hover effects, smooth transitions
- **Accessibility**: Semantic HTML and ARIA considerations

## Data Flow

1. **User Request**: Browser sends request to Flask application
2. **Route Handling**: Flask routes process request and validate forms
3. **Database Operations**: SQLAlchemy ORM handles data persistence
4. **Template Rendering**: Jinja2 renders HTML with dynamic data
5. **Response**: Complete HTML page sent back to browser

### Task Management Flow
- Users can create tasks with title, description, due date, and priority
- Tasks can be filtered by status, priority, and search terms
- Sorting options include creation date, due date, and priority
- Real-time statistics show task completion progress

## External Dependencies

### Python Packages
- **Flask**: Web framework and core functionality
- **Flask-SQLAlchemy**: Database ORM integration
- **Flask-WTF**: Form handling and CSRF protection
- **WTForms**: Form validation and rendering
- **Werkzeug**: WSGI utilities and proxy handling

### Frontend Libraries
- **Bootstrap**: CSS framework with dark theme
- **Feather Icons**: Lightweight icon library
- **No jQuery**: Pure vanilla JavaScript approach

### Development Dependencies
- **SQLite**: File-based database for development
- **ProxyFix**: Handles proxy headers for deployment

## Deployment Strategy

### Current Configuration
- **Database**: SQLite file-based storage (`todo.db`)
- **Session Management**: Secret key from environment or default
- **Proxy Support**: Configured for reverse proxy deployment
- **Debug Mode**: Enabled for development

### Production Considerations
- Environment-based configuration management
- Database migration strategy (ready for PostgreSQL upgrade)
- Static file serving optimization
- Error handling and logging
- Security headers and CSRF protection

### Scalability Preparation
- ORM abstraction allows easy database switching
- Modular structure supports feature expansion
- Form validation ready for API endpoints
- Frontend prepared for SPA conversion

## Changelog
- June 28, 2025. Initial setup

## User Preferences

Preferred communication style: Simple, everyday language.