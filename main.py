from fastapi import FastAPI
from pydantic import BaseModel
from database import init_db, add_expense_db, get_expenses_db

app = FastAPI()
init_db()

class Expense(BaseModel):
    category: str
    amount: int

@app.post("/expenses")
def add_expense(expense: Expense):
    add_expense_db(expense)
    return {"message": "Expense added"}

@app.get("/expenses")
def get_expenses():
    rows = get_expenses_db()
    return [{'category': row['category'], 'amount': row['amount']} for row in rows]
