# Library-Management-API
RESTful API built with Python, FastAPI, SQLAlchemy, and Pydantic for managing a personal library book catalog and loan lifecycle.

# 📚 Personal Library & Loan Management API

A production-ready RESTful API for managing a personal library book catalog and tracking book loan lifecycles. Built from scratch with Python, FastAPI, SQLAlchemy, and Pydantic V2, focusing on modular architecture, static typing, and separation of concerns.

---

## 🚀 Features

- **Book Management (CRUD):** Add, view, update (partial updates via `PATCH`), and delete books from your collection.
- **Loan Lifecycle Management:** Issue loans for available books and process returns.
- **Data Validation & Serialization:** Enforced strictly via Pydantic V2 schemas (`from_attributes` ORM mode enabled).
- **Relational Database Management:** Powered by SQLAlchemy ORM with foreign keys, relationships, and custom Enums for book and loan statuses.
- **Interactive API Documentation:** Auto-generated Swagger UI and ReDoc endpoints.

---

## 🏗️ Project Architecture

The project follows a clean, layered architecture separating database setup, models, validation schemas, business logic, and HTTP endpoints:

```text
.
├── database.py    # Database connection, engine setup, and SessionLocal generator
├── models.py      # SQLAlchemy ORM models (Book & Loan database entities)
├── schemas.py     # Pydantic V2 schemas (DTOs for request/response validation)
├── crud.py        # Business logic, validation rules, and database operations
├── main.py        # FastAPI initialization and HTTP route declarations
├── .gitignore     # Ignored files (virtual environment, cache, local SQLite database)
├── LICENSE        # MIT License
└── README.md      # Project documentation
