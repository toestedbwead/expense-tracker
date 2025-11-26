import sys
import json
import os
from datetime import datetime
import argparse

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
   parser = argparse.ArgumentParser(description='Expense Tracker CLI')

   subparsers = parser.add_subparsers(dest='command', help='Available commands')

   # add command
   add_parser = subparsers.add_parser('add', help='Add a new expense')
   add_parser.add_argument('--description', required=True, help='Expense description')
   add_parser.add_argument('--amount', type=float, required=True, help='Expense amount')

   # delete command
   delete_parser = subparsers.add_parser('delete', help='Delete an expense')
   delete_parser.add_argument('--id', type=int, required=True, help='Expense ID to delete')

   # update command
   update_parser = subparsers.add_parser('update', help='Update an expense')
   update_parser.add_argument('--id', type=int,required=True, help='Expense ID to update')
   update_parser.add_argument('--description', help='Description to be updated')
   update_parser.add_argument('--amount', type=float, help='Amount to be updated')

   # list command
   list_parser = subparsers.add_parser('list', help='List of expenses')

   # summary of all expenses command
   summary_parser = subparsers.add_parser('summary', help="Summary of all expenses")

   summary_parser.add_argument('--month', type=int,help='Summary of expenses per specific month. 1-12')

   args = parser.parse_args()
   







if __name__ == "__main__":
    main()