from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_login():
    payload = {
        "username": "john",
        "password": '123'
    }
    response = client.post("/login", json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Login successful"}