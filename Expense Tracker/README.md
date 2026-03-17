# Expense Tracker

## Description

This is a simple Expense Tracker application built in Python. It allows users to add, view, and manage their daily expenses. The application stores expense data in a JSON file located in the `data/` directory.

## Features

- Add new expenses with amount, category, and description
- View all expenses in a tabular format
- Calculate total spending
- View spending summary by category
- Persistent storage using JSON file

## Requirements

- Python 3.9 or higher
- `tabulate` library for table formatting

## Installation

1. Clone or download the project repository.
2. Navigate to the project directory.
3. Install the required dependencies:
   ```
   pip install tabulate
   ```

## Usage

Run the application using:
```
python src/main.py
```

Follow the on-screen menu to:
1. Add Expense
2. View All Expenses
3. Total Spending
4. Category Summary
5. Save & Exit

## Modules

The project is organized into the following modules:

### `main.py`
The entry point of the application. It imports functions from `storage` and `tracker` modules, displays a menu-driven interface, and handles user choices in a loop. The menu options include adding expenses, viewing expenses, showing totals, category summaries, and saving data before exit.

### `storage.py`
Manages data persistence for the application. It handles reading expenses from and writing expenses to a JSON file (`data/expense.json`). Includes functions to ensure the data file exists and to load/save expense data.

### `tracker.py`
Contains the core logic for expense tracking. Includes functions to:
- `add_expense`: Prompts user for expense details (amount, category, description), validates input, and adds the expense to the list.
- `list_expenses`: Displays all expenses in a formatted table using the `tabulate` library.
- `show_total`: Calculates and displays the total spending across all expenses.
- `show_category_summary`: Groups expenses by category and shows the total spending per category in a table.

## Project Structure

```
Expense Tracker/
├── README.md
├── data/
│   └── expense.json
└── src/
    ├── main.py
    ├── storage.py
    ├── tracker.py
    └── __pycache__/
```