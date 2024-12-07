
# JWKS Server Project

## Overview
This project is a JWKS (JSON Web Key Set) server implemented using Flask. It supports user registration and authentication with a focus on security features such as AES encryption, authentication logging, and database-backed user management.

The project was developed on **Replit** as part of the CSCE 3550 - Foundations of Cybersecurity course.

## Features
- **User Registration**: Register new users with unique usernames and email addresses. Secure passwords are automatically generated.
- **Authentication**: Verify users with proper logging of authentication attempts.
- **Database Integration**: Utilizes SQLite for persistent user data and authentication logs.
- **Testing**: Includes a `test_api.py` script to test the `/register` and `/auth` endpoints.

## Project Files
1. **`app.py`**:
   - Main Flask application for the JWKS server.
   - Contains routes for user registration (`/register`) and authentication (`/auth`).

2. **`main.py`**:
   - Entry point to run the Flask application.

3. **`models.py`**:
   - SQLAlchemy models for `User` and `AuthLog`.
   - Includes database setup and schema management.

4. **`database.db`**:
   - SQLite database file containing the application's data.

5. **`test_api.py`**:
   - Script to test the API endpoints using HTTP requests.

## Requirements
- Python 3.x
- Flask
- SQLAlchemy
- Requests (for `test_api.py`)

## Setup
1. Clone the repository.
2. Ensure Python 3.x is installed.
3. Install dependencies:
   ```bash
   pip install flask sqlalchemy requests
   ```
4. Run the application:
   ```bash
   python main.py
   ```
5. Use the `test_api.py` script to verify functionality.

## Development Environment
This project was developed on **Replit**, an online IDE that facilitates collaborative development.

## Acknowledgments
- Instructor: Rezwanur Rahman
- Course: CSCE 3550 - Foundations of Cybersecurity
