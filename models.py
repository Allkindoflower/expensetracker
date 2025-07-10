from pydantic import BaseModel

class Expense(BaseModel):
    category: str
    amount: int