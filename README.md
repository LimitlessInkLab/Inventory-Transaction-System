# Inventory-Transaction-System
A sophisticated Inventory Management System built with Python, utilizing the **Model-View-Controller (MVC)** architectural pattern. This project demonstrates clean code principles, dependency injection, and robust database transaction handling.

---

## Key Features
- **MVC Architecture**: Clean separation of data, UI, and logic.
- **Atomic Transactions**: Secure sales processing with SQL commit/rollback logic.
- **Dependency Injection**: Modular database management via `DatabaseProvider`.
- **Automated Setup**: Seamless environment preparation script.
- **Interactive UI**: Real-time inventory tracking with Tkinter.

## Tech Stack
- **Python 3**
- **Tkinter** (GUI)
- **MySQL** (Database)

## File Structure
- `main.py`: Entry point.
- `models.py`: Business logic & Data classes.
- `views.py`: UI components.
- `controllers.py`: Event handling.
- `database.py`: DB connection provider.
- `setup.py`: Environment setup script.

## Installation & Usage
1. **Dependencies**: `pip install mysql-connector-python`
2. **Setup**: Run `python setup.py` to initialize the database.
3. **Launch**: Run `python main.py` to start the application.
