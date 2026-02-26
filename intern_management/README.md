# Intern Management System

Django web application for managing interns with admin panel and Bootstrap 5 interface.

## Features

- 📋 **Intern Management**: Create, read, update, and delete intern records
- 📸 **Photo Upload**: Upload and preview photos for interns via admin panel
- 🔍 **Search**: Search interns by full name, passport ID, or department
- 📊 **Admin Panel**: Jazzmin-themed admin interface
- 🎨 **Responsive Design**: Bootstrap 5 responsive UI
- ⏰ **Status Tracking**: Automatic status calculation (Active/Expired)
- 📅 **Days Left**: Automatic calculation of remaining internship days
- 🗄️ **SQLite3**: Lightweight database

## Installation

### 1. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create superuser

```bash
python manage.py createsuperuser
```

### 5. Run development server

```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000/`

## Project Structure

```
intern_management/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── db.sqlite3               # SQLite database
├── config/                  # Django settings
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── interns/                 # Interns app
│   ├── models.py            # Intern model
│   ├── views.py             # Views
│   ├── urls.py              # App URLs
│   ├── admin.py             # Admin configuration
│   └── migrations/          # Database migrations
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   └── index.html           # Home page template
├── media/                   # User uploaded files
│   └── interns/             # Intern photos
└── static/                  # Static files
```

## Model Fields

### Intern Model

- **full_name** (CharField): Full name of the intern
- **passport_id** (CharField): Unique passport ID
- **department** (CharField): Department where intern works
- **reason** (TextField): Reason for internship
- **start_date** (DateField): Internship start date
- **end_date** (DateField): Internship end date
- **photo** (ImageField): Intern photo (uploaded via admin)
- **created_at** (DateTimeField): Created timestamp
- **updated_at** (DateTimeField): Last update timestamp

### Dynamic Properties

- **days_left**: Calculated remaining days (0 if expired)
- **status**: "Active" or "Expired" based on current date

## Usage

### Admin Panel

- Visit `http://localhost:8000/admin/`
- Login with superuser credentials
- Add, edit, or delete interns
- Upload photos for interns
- View photo previews

### Home Page

- Visit `http://localhost:8000/`
- Search interns by full name, passport ID, or department
- View all interns in a table format
- Expired interns are highlighted in red

## Search Functionality

Search by using the search input on the home page:

```
http://localhost:8000/?q=search_term
```

Search works on:
- Full Name
- Passport ID
- Department

## Admin Features

- Photo preview in admin list
- Color-coded status display
- Search functionality
- Filter by status, department, and date
- Read-only days left and status fields

## Technologies Used

- **Framework**: Django 5.0.1
- **Database**: SQLite3
- **Admin Theme**: Jazzmin 3.0.0
- **Frontend**: Bootstrap 5
- **Image Processing**: Pillow 10.1.0

## Configuration

Edit `config/settings.py` to customize:
- `SECRET_KEY`: Change this in production
- `ALLOWED_HOSTS`: Add your domain
- `DATABASES`: Database configuration
- `JAZZMIN_SETTINGS`: Admin panel customization

## Development Tips

1. Create sample data via admin panel
2. Access admin at `/admin/`
3. View interns at `/`
4. Search functionality uses GET parameters

## License

This project is provided as-is for educational purposes.
