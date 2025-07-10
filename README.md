Contributions are welcome! If you'd like to help improve this project, feel free to reach out at bastugugur85@gmail.com.

Expense Tracker API
A simple backend API to track expenses by category using FastAPI and SQLite.

Features
Add expenses with category and amount

List all recorded expenses

Persistent storage with SQLite

Interactive API docs via Swagger UI

Requirements
Python 3.9+
FastAPI
Uvicorn

Installation
Install dependencies with:

pip install fastapi uvicorn

Running the App
Start the server with:

uvicorn main:app --reload

The API will be available at http://localhost:8000

API Endpoints

GET / -- for automatic redirection to avoid having the user manually type /docs at the end of the app link

GET /expenses — Retrieve all expenses

POST /expenses — Add a new expense

Request body example:
{
  "category": "food",
  "amount": 25
}

API Documentation
Open your browser and go to:

http://localhost:8000/docs

to access the Swagger UI for interactive API exploration.

Project Structure
main.py — FastAPI application and route definitions
models.py - Has only one model, but good practice for scalability
database.py — SQLite database setup and helper functions
requirements.txt - For deployment on Render.com

License

MIT License

