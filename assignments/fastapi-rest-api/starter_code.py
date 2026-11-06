from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI(title="Book API")

books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
]