# SaaS Backend

A backend application built using Python and FastAPI with JWT authentication, multi-tenant middleware support, and CRUD APIs for managing users, projects, and tasks.

---

## Features

- User Authentication with JWT
- Multi-tenant middleware support
- Project management APIs
- Task management APIs
- Secure password handling
- SQLAlchemy ORM integration
- RESTful API structure
- Modular folder architecture

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- JWT Authentication
- SQL Server / Relational Database
- Git & GitHub

---

## Project Structure

```bash
saas_backend/
│
├── app/
│   ├── config/
│   │   └── database.py
│   │
│   ├── middleware/
│   │   └── tenant.py
│   │
│   ├── models/
│   │   ├── organization.py
│   │   ├── project.py
│   │   ├── task.py
│   │   └── user.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── projects.py
│   │   └── tasks.py
│   │
│   ├── schemas/
│   │   ├── auth.py
│   │   ├── project.py
│   │   └── task.py
│   │
│   ├── utils/
│   │   ├── dependencies.py
│   │   └── security.py
│   │
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/surajPratapSinghBhati/saas-backend.git
cd saas-backend
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
uvicorn app.main:app --reload
```

Server will start on:

```bash
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates API docs:

### Swagger UI

```bash
http://127.0.0.1:8000/docs
```

### ReDoc

```bash
http://127.0.0.1:8000/redoc
```

---

## Authentication

This project uses JWT-based authentication.

Features:
- User registration
- Login authentication
- Password hashing
- Protected routes

---

## Functional Modules

### User Module
- Register user
- Login user
- Authentication handling

### Project Module
- Create project
- Update project
- Fetch projects
- Delete projects

### Task Module
- Create tasks
- Assign tasks
- Update task status
- Delete tasks

---

## Learning Outcomes

This project helped in understanding:

- Backend API development
- Authentication workflows
- Database integration
- REST API design
- Middleware handling
- Git and GitHub workflow
- Modular backend architecture

---

## Future Improvements

- Role-based access control
- Docker support
- Deployment on cloud platforms
- Unit testing
- CI/CD integration
- API rate limiting

---

## Author

Suraj Bhati

GitHub:
https://github.com/surajPratapSinghBhati
