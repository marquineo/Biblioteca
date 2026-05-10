# Sistema de Gestión de Biblioteca

This project is an object-oriented Python application for managing a library's core operations. It handles the registration of books and users, manages loans, processes returns, and calculates fines for late returns. The system is designed with a strong emphasis on clean architecture and design patterns, prioritizing correct business logic over a graphical interface or database persistence. All operations are managed in memory with options to import and export data to CSV and JSON files.

## Features
*   **User and Book Management:** Register new users and add books to the library's inventory.
*   **Loan System:** Create loans, linking a user to a book with a specific due date.
*   **Book Returns:** Process book returns, update loan status, and make the book available again.
*   **Fine Calculation:** Automatically calculate fines for overdue returns using a flexible strategy pattern.
*   **Data I/O:** Import and export library data (books, users, loans) in both CSV and JSON formats.
*   **Extensible Plugin System:** Dynamically load plugins to extend functionality, such as adding new export formats.
*   **Command-Line Interface:** Interact with the system through a simple and intuitive console menu.
*   **Comprehensive Testing:** Includes a suite of unit tests to ensure code quality and correctness.

## Architectural Design
The system is built following key Object-Oriented Programming (OOP) principles and design patterns to ensure a clean, maintainable, and scalable codebase.

*   **Facade Pattern (`Biblioteca`)**: The `Biblioteca` class acts as a central facade, providing a simplified interface to the system's complex inner workings. It orchestrates all interactions between books, users, and loans.
*   **Factory Pattern (`PrestamoFactory`)**: The creation of `Prestamo` objects is decoupled from the main logic using a factory. This centralizes the instantiation process and makes it easier to modify or extend.
*   **Strategy Pattern (`StrategyMulta`)**: The logic for calculating late fees is implemented using the Strategy pattern. Different calculation methods (`MultaEstandar`, `MultaReducida`, `MultaProgresiva`) can be swapped at runtime without altering the core loan logic.
*   **Mixin for I/O (`DataIOMixin`)**: Import and export functionalities are encapsulated in the `DataIOMixin` class. This mixin is then combined with the `Biblioteca` class to add data handling capabilities without cluttering the main class.
*   **Plugin Architecture (`plugin_loader`)**: The application features a dynamic plugin loader that scans the `plugins` directory. It loads any class ending with "Plugin" and integrates it into the `Biblioteca` class, allowing for easy extensibility. This is used for the CSV and JSON export logic.
*   **Abstract Base Class (`Persona`)**: The `Usuario` class inherits from the `Persona` abstract base class, demonstrating the use of abstraction and inheritance. A metaclass (`ValidacionModelo`) is also used to enforce attribute presence at class creation time.

### Core Classes
*   **`Libro`**: Represents a book with an ISBN, title, and author. It's a passive data object.
*   **`Usuario`**: Represents a library user with an ID, name, and a maximum loan limit.
*   **`Prestamo`**: The core logic class. It links a `Libro` and a `Usuario`, manages loan dates, and determines if a loan is active, overdue, or returned.
*   **`Biblioteca`**: The orchestrator that manages collections of books, users, and loans, and enforces business rules like loan limits.

## Getting Started

### Prerequisites
*   Python 3.x

### Running the Application
The main application is a command-line interface. To run it, execute the `main.py` file from the root directory:

```bash
python biblioteca/main.py
```
This will launch an interactive menu where you can perform various library management tasks.

### Running Tests
The project includes a suite of unit tests built with Python's `unittest` module. To run the tests, use the following command from the root directory of the repository:

```bash
python -m unittest discover -s biblioteca/test
```

## File Structure
The repository is organized as follows:
```
.
├── biblioteca/             # Main source code directory
│   ├── biblioteca.py       # Facade class for the library system
│   ├── data_io_mixin.py    # Mixin for data import/export
│   ├── libro.py            # Libro class definition
│   ├── main.py             # Main executable and CLI
│   ├── persona.py          # Abstract base class for User
│   ├── plugin_loader.py    # Logic for loading plugins
│   ├── prestamo.py         # Prestamo class definition and logic
│   ├── prestamo_factory.py # Factory for creating Prestamo objects
│   ├── strategy_multa.py   # Strategy pattern for fine calculation
│   ├── usuario.py          # Usuario class definition
│   ├── plugins/            # Directory for extensible plugins
│   │   ├── export_csv_plugin.py
│   │   └── export_json_plugin.py
│   └── test/               # Unit tests
│       ├── test_biblioteca.py
│       ├── test_libro.py
│       ├── test_prestamo.py
│       └── test_usuario.py
├── libros.csv              # Sample data files
├── libros.json
├── prestamos.csv
├── prestamos.json
├── usuarios.csv
└── usuarios.json
