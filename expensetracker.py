import time
import json
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


expenses = {
'food': 0,
'transportation': 0,
'bills': 0,
'fun': 0,
'emergency': 0
}

def open_json_file():
    try:
        with open('expenses.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {
        'food': 0,
        'transportation': 0,
        'bills': 0,
        'fun': 0,
        'emergency': 0
}
        
expenses = open_json_file()

def add_expense():
    while True:
        print('Please enter the category of your expense:')
        for expense in expenses:
            print(f'{expense}')
        chosen_category = input('> ').strip().lower()
        if chosen_category not in expenses:
            print('That category is invalid, please try again.')
            continue
        else:
            try:
                print('Please choose an expense value. (Type "0" if you made a mistake.)')
                expense_value = int(input('> '))
                expenses[chosen_category] += expense_value
                with open('expenses.json', 'w') as file:
                    json.dump(expenses, file, indent=4)
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
        with open('expenses.json', 'r') as file:
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
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=4)


expenses = load_expenses_json()

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
        
    



def print_help():
    print('''
help - for a list of commands
add - to add an expense
view - to view all expenses
quit - to quit program
cat - to add a new category of expenses
clear - to clear the terminal
          
all categories:
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
    













