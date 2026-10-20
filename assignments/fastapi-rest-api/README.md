# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI that lets clients read, create, update, and delete book records. Practice defining endpoints, using request and response models, and returning appropriate HTTP status codes.

## 📝 Tasks

### 🛠️ Create Read Endpoints

#### Description
Use the provided starter code to create endpoints for listing all books and retrieving one book by its ID. From the assignment directory, install FastAPI and Uvicorn with `python -m pip install fastapi uvicorn`, then run the application with `uvicorn starter-code:app --reload`. Explore and test the endpoints in FastAPI's interactive documentation at `http://127.0.0.1:8000/docs`.

#### Requirements
Completed API should:

- Return all books as JSON from `GET /books`
- Return one book as JSON from `GET /books/{book_id}`
- Return HTTP 404 when the requested book ID does not exist


### 🛠️ Add a Book

#### Description
Create an endpoint that accepts a book's title and author, assigns it a unique ID, and adds it to the in-memory collection.

#### Requirements
Completed API should:

- Accept a JSON request body at `POST /books`, for example:

  ```json
  {
    "title": "A Wrinkle in Time",
    "author": "Madeleine L'Engle"
  }
  ```
- Use the `BookCreate` model to validate the request body
- Return the created book, including its ID, with HTTP 201
- Make the new book available through the read endpoints


### 🛠️ Update and Delete Books

#### Description
Add endpoints to replace a book's title and author and to remove a book from the collection.

#### Requirements
Completed API should:

- Accept a `PUT` request at `/books/{book_id}` with a `BookCreate` JSON body and return the updated book
- Accept a `DELETE` request at `/books/{book_id}` and remove that book
- Return HTTP 404 for update or delete requests that use an unknown book ID
- Confirm that a deleted book can no longer be retrieved
