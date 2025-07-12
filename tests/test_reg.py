from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_loginandreg():
    payload = {
        "username": "testusername",
        "password": 'testpassword'
    }
    response = client.post("/register", json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Registration successful!"}