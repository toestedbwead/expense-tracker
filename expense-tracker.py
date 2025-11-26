import sys
import json
import os
import argparse
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
   expenses = load_expenses()

   if args.command == 'add':
       print(f"Adding expense: {args.description} - ₱{args.amount}")
       if expenses:
           highest_id = 0
           for expense in expenses:
               if expense['id'] > highest_id:
                   highest_id = expense['id']
           new_id = highest_id + 1
       else:
           new_id = 1
       

       new_expense = {
           'id': new_id,
           'description': args.description,
           'amount': args.amount
       }

       expenses.append(new_expense)
       print(f"Expense added successfully. ID: {new_id}")

       save_expenses(expenses)
   elif args.command == 'delete':
        expense_id = args.id

        found_index = -1
        for index, expense in enumerate(expenses):
            if expense['id'] == expense_id:
                found_index = index
                break

        if found_index == -1:
            print(f"Error: Task with ID {expense_id} not found.")
            return
        
        expenses.pop(found_index)
        print(f"Expense {expense_id} deleted successfully.")

        save_expenses(expenses)

   elif args.command == 'update':
       expense_id = args.id
       expense_description = args.description
       expense_amount = args.amount

       found_index = -1
       for index, expense in enumerate(expenses):
           if expense['id'] == expense_id:
               expense['description'] = expense_description
               expense['amount'] = expense_amount
               found_index = index
               break
           
       if found_index == -1:
           print(f"Error: Expense with ID {expense_id} is not found")
           return
       
       print(f"Expense {expense_id} updated successfully.")
       save_expenses(expenses)

   elif args.command == 'list':
        for expense in expenses:
            print(f"ID: {expense['id']} | Description: {expense['description']} | Amount: ₱{expense['amount']}")

        print(f"Total List: {len(expenses)} expense/s.")
   elif args.command == 'summary':
       pass
   
   # wait...i would need a month column for the commands here...
   
   # imported datetime module
   # have to somehow check if '2024-08-06' can be converted or sliced into 1-12 so the expenses can be summarized by specific month
   # add date column in expenses 







if __name__ == "__main__":
    main()