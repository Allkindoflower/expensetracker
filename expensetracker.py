import time
import json
import os

DATA_PATH = os.path.expanduser('~/expenses.json')

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Screen cleared!')

def add_expense():
    while True:
        for expense in expenses:
            print(f'{expense}')
        chosen_category = input('> ').strip().lower()
        if chosen_category not in expenses:
            print('That category is invalid, please try again.')
            continue
        else:
            try:
                print('Please choose an expense value.')
                expense_value = int(input('> '))
                if expense_value < 0:
                    print('Please enter a positive number.')
                    continue
                expenses[chosen_category] += expense_value
                save_expenses_json(expenses)
                print('Expense successfully added!')
                break
            except ValueError:
                print('Please enter a valid positive number. ')
                continue

def view_expenses():
    print('\n ----- Expense Overview -----')
    for category, amount in expenses.items():
        print(f'{category:<15}: {amount:>5}')
    print('\n ----------------------------')

def load_expenses_json():
    try:
        with open(DATA_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {
        'food': 0,
        'transportation': 0,
        'bills': 0,
        'fun': 0,
        'emergency': 0
}
    


def save_expenses_json(expenses):
    with open(DATA_PATH, "w") as file:
        json.dump(expenses, file, indent=4)

def add_category():
    print('Name of your new category: ')
    new_cat = input('> ').strip().lower()
    if new_cat in expenses:
        print('Category already exists!')
    elif not new_cat:
        print('Category name cannot be empty!')
    else:
        expenses[new_cat] = 0
        save_expenses_json(expenses)
        print('Category successfully added!')
 
        
    
expenses = load_expenses_json()


def print_help():
    print('''
help - for a list of commands
add - to add an expense
view - to view all expenses
quit - to quit program
cat - to add a new category of expenses
clear - to clear the terminal
          
default categories:
food
transportation
bills
fun
emergency
''')

print('This is your expense tracker. Type "help" for a list of commands.')

while True:
    user_command = input('> ').strip().lower()
    if user_command == 'add':
        add_expense()
    elif user_command == 'help':
        print_help()   
    elif user_command == 'view':
        view_expenses()
    elif user_command == 'quit':
        print('Exiting program...')
        time.sleep(2)
        quit()
    elif user_command == 'cat':
        add_category()
    elif user_command == 'clear':
        clear_terminal()
    else:
        print('Wrong input, type "help" for a valid list of commands.')
    













