import sqlite3

DB_PATH = "expenses.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            amount INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_expense_db(expense):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (category, amount) VALUES (?, ?)",
        (expense.category, expense.amount)
    )
    conn.commit()
    conn.close()
def get_expenses_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, category, amount FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    return rows
