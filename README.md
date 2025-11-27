# Expense Tracker CLI

A command-line expense tracker built with Python to manage personal finances. Track, update, and analyze your expenses with simple commands.

## Features

- **Add expenses** with descriptions, amounts, and dates
- **Update existing expenses** (modify description, amount, or date)
- **Delete expenses** by ID
- **List all expenses** with detailed view
- **Expense summaries** - total or filtered by month
- **Date validation** supports multiple formats (YYYY-MM-DD, YYYYMMDD, MM/DD/YYYY)
- **Persistent storage** using JSON files
- **Professional CLI** with argparse

## Installation

1. Clone or download this repository
2. Ensure you have Python 3.6+ installed
3. No external dependencies required!

## Usage

```bash
# Add a new expense
python expense_tracker.py add --description "Lunch" --amount 20 --date 2024-01-15

# List all expenses
python expense_tracker.py list

# Update an expense
python expense_tracker.py update --id 1 --amount 25 --description "Business Lunch"

# Delete an expense
python expense_tracker.py delete --id 2

# View summary of all expenses
python expense_tracker.py summary

# View summary for specific month
python expense_tracker.py summary --month 8
```

# Example Output
```
$ python expense_tracker.py list
ID: 1 | Description: Lunch | Amount: ₱20 | Date: 2024-01-15
ID: 2 | Description: Dinner | Amount: ₱30 | Date: 2024-01-15
Total List: 2 expense/s.

$ python expense_tracker.py summary
Total expenses: ₱50

$ python expense_tracker.py summary --month 1
Total expenses for January: ₱50
```

Based on project: https://roadmap.sh/projects/expense-tracker

