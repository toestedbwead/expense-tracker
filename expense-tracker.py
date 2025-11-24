import sys
import json
import os
from datetime import datetime

EXPENSES_FILE = 'expenses-tracker.json'

def load_expenses():
    if not os.path.exists(EXPENSES_FILE):
        return []
    try:
        with open(EXPENSES_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: Invalid JSON file. Starting with an empty expense tracker list.")
        return []
    

def save_expenses(expenses):
    try:
        with open(EXPENSES_FILE, 'w') as file:
            json.dump(expenses, file, indent=4)
    except Exception as e:
        print(f"Error saving tasks: {e}")

def main():
    if len(sys.argv) > 6:
        print("Usage: python expense-tracker.py <command> [args] ")
        return
    
    





if __name__ == "__main__":
    main()