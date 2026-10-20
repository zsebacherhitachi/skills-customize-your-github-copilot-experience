from fastapi import FastAPI, HTTPException

app = FastAPI(title="Book API for Testing")

books = {
    1: {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    2: {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
}


@app.get("/books")
def list_books() -> list[dict[str, int | str]]:
    return list(books.values())


@app.get("/books/{book_id}")
def get_book(book_id: int) -> dict[str, int | str]:
    book = books.get(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
