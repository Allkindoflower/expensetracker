from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_expense_success():
    payload = {
        "category": "Food",
        "amount": 50
    }
    response = client.post("/expenses", json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Expense added"}
