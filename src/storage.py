import os
import json

DATA_Dir = os.path.join(os.path.dirname(__file__), ".." , "data")
DATA_File = os.path.join(DATA_Dir, "expense.json")

def ensure_data_file_exists() -> None:
    """Ensures that the data file exists. If it doesn't, creates an empty JSON file."""
    os.makedirs(DATA_Dir, exist_ok=True)

    if not os.path.exists(DATA_File):
        with open (DATA_File, "w", encoding="utf-8") as f:
            json.dump([],f)

def load_expenses() -> list[dict]:
    """Load expenses list from JSON file."""
    ensure_data_file_exists()

    try:
        with open(DATA_File, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # If the file is empty or invalid JSON, return an empty list
        return []
    
def save_expenses(expenses: list[dict]) -> None:
    """Save expenses list to JSON file."""
    with open(DATA_File, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=2)