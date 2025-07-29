# LibraryProject 
# LibraryProject

This is a Django-based library management system for the ALX Django Learn Lab.  
It includes custom user authentication, role-based access control, permissions, and model relationships.

## Features
- Custom User Model with `date_of_birth` and `profile_photo`
- Group-based permissions (Admin, Editor, Viewer)
- CRUD functionality for books
- Role-based dashboards

## Technologies
- Python
- Django
- SQLite (default)
- Bootstrap (for templates)

## Getting Started
1. Clone the repository.
2. Set up a virtual environment.
3. Run migrations and create a superuser.
4. Start the development server.

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
