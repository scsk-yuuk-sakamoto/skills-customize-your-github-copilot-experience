# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI that returns and creates book records. Practice defining API routes, validating request data with Pydantic, and returning appropriate HTTP status codes.

## 📝 Tasks

### 🛠️ Create a Book List Endpoint

#### Description
Use the provided starter code to create a FastAPI endpoint that returns the current book list. Install FastAPI and Uvicorn with `python -m pip install fastapi uvicorn`, then run the app with `uvicorn starter_code:app --reload`.

#### Requirements
Completed program should:

- Define a `GET /books` endpoint that returns the book records in the starter list.
- Start successfully with Uvicorn and display the interactive API documentation at `http://127.0.0.1:8000/docs`.
- Return the book list when the `GET /books` endpoint is tested in the interactive documentation.

### 🛠️ Add a Book Creation Endpoint

#### Description
Add a request model and a `POST` endpoint so clients can submit a new book and receive the created record.

#### Requirements
Completed program should:

- Define a Pydantic model named `BookCreate` with `title` and `author` string fields.
- Define a `POST /books` endpoint that accepts a JSON request body validated with `BookCreate`.
- Add each submitted book to the in-memory book list and assign it a unique integer `id`.
- Return the created book, including its `id`, `title`, and `author`, with HTTP status code `201`.
- Demonstrate creating a book and then confirming it appears in the `GET /books` response.