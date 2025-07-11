import sqlite3

DB_PATH = "expenses.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_expenses_db():
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

def init_user_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL              )

    '''
    )
    conn.commit()
    conn.close()

def user_exists_db(username: str) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT username FROM users WHERE username = ?', (username,))
    rows = cursor.fetchone()
    if rows:
        conn.close()
        return True  
    else:
        conn.close()
        return False
    

def register_user_db(username, hashed_password):
    conn = get_connection()
    cursor = conn.cursor()
    if user_exists_db(username):
        conn.commit()
        conn.close()
        return False
    else:
        cursor.execute('INSERT INTO users (username, password) VALUES (?,?)', (username, hashed_password))
        conn.commit()
        conn.close()
        return True

def get_user_password_hash(username: str) -> str | None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    return row["password"] if row else None


