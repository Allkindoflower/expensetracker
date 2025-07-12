from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_expense():
    payload = {
        "category": "testcat",
        "amount": 50
    }
    response = client.post("/expenses", json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Expense added"}