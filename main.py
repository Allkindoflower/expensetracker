from fastapi import FastAPI
from database import init_user_table, add_expense_db, get_expenses_db, register_user_db, get_user_password_hash, init_expenses_db
from fastapi import FastAPI, Form
from models import Expense
from passlib.hash import pbkdf2_sha256 as algo
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

init_user_table()
init_expenses_db()


@app.get("/")
async def root():
    return RedirectResponse(url="/static/landing.html") 


@app.post("/expenses")
def add_expense(expense: Expense):
    add_expense_db(expense)
    return {"message": "Expense added"} #TODO: return to expenses page


@app.get("/expenses")
def get_expenses():
    rows = get_expenses_db()
    return [{'category': row['category'], 'amount': row['amount']} for row in rows] #TODO: return these neatly to the expenses page


@app.post('/register')
def user_register(username: str = Form(...), password: str = Form(...)):
    hashed_password = algo.hash(password)
    if register_user_db(username, hashed_password):
        return RedirectResponse(url="/static/landing.html") 
    else:
        return {'message': 'That user already exists!'} #TODO: do in-page warning
    

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    stored_hash = get_user_password_hash(username)
    if not stored_hash or not algo.verify(password, stored_hash):
        return {"error": "Invalid username or password"} #TODO: in-page warning
    return RedirectResponse(url="/static/expenses.html", status_code=303)


    



