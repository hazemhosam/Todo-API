# To-Do API

A simple To-Do API built with Django and Django REST Framework (DRF). This API allows users to create, read, update, and delete tasks in a to-do list.

---

## Features

- **User Authentication**: Secure user registration and login using JWT (JSON Web Tokens).
- **CRUD Operations**: Create, Read, Update, and Delete tasks.
- **Task Filtering**: Filter tasks by status (completed/incomplete).
- **Pagination**: Paginated responses for large datasets.
- **Search Functionality**: Search tasks by title or description.

---

## Technologies Used

- **Python**: Programming language.
- **Django**: Web framework.
- **Django REST Framework (DRF)**: For building RESTful APIs.
- **JWT**: For user authentication.
- **MysSQL**: Database
- **Swagger**: For Documentaion you can find it at ```/api/swagger/```

---

## Installation and Setup

Follow these steps to set up the project locally:

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/hazemhosam/todo-api.git
   cd todo-api 
   ``` 
2. **Create a virtual environment**: (optional but recommended):
    ```bash
        python -m venv venv
        venv\Scripts\activate  # On mac: source venv/bin/activate 
    ```     
3. **Install dependencies**:

    ```bash
        pip install -r requirements.txt
    ```
4. **Set up the database**:

  Update the DATABASES configuration in settings.py with your database credentials.

  Run migrations:
    ```bash
        python manage.py migrate
    ```   

### Contributing
Contributions are welcome! If you'd like to contribute.