from pydantic import BaseModel

class Expense(BaseModel):
    category: str
    amount: int

class UserLoginAndRegistration(BaseModel): #same attributes, same model
    username: str
    password: str