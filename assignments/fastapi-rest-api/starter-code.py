from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Book API")


class BookCreate(BaseModel):
    title: str
    author: str


class Book(BookCreate):
    id: int


books: dict[int, Book] = {
    1: Book(id=1, title="The Hobbit", author="J.R.R. Tolkien"),
}
next_book_id = 2

# Add your GET, POST, PUT, and DELETE endpoints below.
