# SpendWise – Personal Finance & Expense Tracker

SpendWise is a full-stack personal finance application that helps users record, organize, and review their daily expenses. It provides authenticated access, expense management, category-wise breakdowns, and monthly spending summaries.

## Features

- **User authentication:** User registration and login with password hashing.
- **Expense management:** Create, view, edit, and delete expenses.
- **Expense categorization:** Organize transactions into categories such as Food, Travel, Shopping, Bills, Education, Health, and Other.
- **Monthly summaries:** Review spending totals and transaction counts for a selected month.
- **Category-wise breakdown:** View how spending is distributed across expense categories.
- **Persistent storage:** Store users and expenses in PostgreSQL.
- **REST API:** Use FastAPI endpoints to handle application requests.

## Tech Stack

- **Backend:** Python, FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Frontend:** HTML, CSS, JavaScript
- **Authentication:** Password hashing and token-based authentication
- **API documentation:** FastAPI Swagger UI

## Project Structure

```text
SpendWise/
├── backend/
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── frontend/
│   └── index.html
├── .env
├── .gitignore
└── requirements.txt
```

*The structure above is representative; adjust it to match the actual files in your repository.*

## Run Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the environment

Create a local `.env` file with the database connection settings and authentication secret expected by the backend. Create the PostgreSQL database and configure its credentials to match your local setup.

**Do not commit `.env` or publish database passwords, secret keys, or other credentials.**

### 5. Start the backend

From the project root, run:

```bash
uvicorn backend.main:app --reload
```

The API should be available at:

`http://127.0.0.1:8000`

Interactive API documentation:

`http://127.0.0.1:8000/docs`

### 6. Open the frontend

Open `frontend/index.html` using VS Code Live Server, then register or log in and start recording expenses.

## API Overview

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/register` | Register a user |
| POST | `/login` | Authenticate a user |
| GET | `/me` | Retrieve the authenticated user's details |
| POST | `/expenses` | Create an expense |
| GET | `/expenses` | Retrieve expenses |
| PUT | `/expenses/{expense_id}` | Update an expense |
| DELETE | `/expenses/{expense_id}` | Delete an expense |

## What I Learned

- Building REST APIs with FastAPI.
- Connecting a Python backend to PostgreSQL using SQLAlchemy.
- Implementing user authentication and password hashing.
- Performing CRUD operations and validating request data.
- Connecting a JavaScript frontend to backend APIs.
- Calculating monthly totals and category-wise spending summaries.

## Future Enhancements

- Monthly budget limits and budget alerts.
- Improved visualizations for spending trends.
- Deployment for public access.
- Automated tests for API endpoints.
