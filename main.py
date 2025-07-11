from fastapi import FastAPI
from database import init_user_table, add_expense_db, get_expenses_db, register_user_db, get_user_password_hash
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from models import Expense, UserLoginAndRegistration
from passlib.hash import pbkdf2_sha256 as algo


app = FastAPI()

init_user_table()


@app.get("/")
def root():
    return RedirectResponse(url="/docs")


@app.post("/expenses")
def add_expense(expense: Expense):
    add_expense_db(expense)
    return {"message": "Expense added"}


@app.get("/expenses")
def get_expenses():
    rows = get_expenses_db()
    return [{'category': row['category'], 'amount': row['amount']} for row in rows]


@app.post('/register')
def user_register(user: UserLoginAndRegistration):
    username = user.username
    hashed_password = algo.hash(user.password)
    register_user_db(username, hashed_password)
    return {'message': 'Registration successful!'}


@app.post("/login")
def login(user: UserLoginAndRegistration):
    stored_hash = get_user_password_hash(user.username)
    if not stored_hash or not algo.verify(user.password, stored_hash):
        return {"error": "Invalid username or password"}
    return {"message": "Login successful"}


    



