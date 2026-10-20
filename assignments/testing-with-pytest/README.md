# 📘 Assignment: Testing with pytest

## 🎯 Objective

Practice writing automated tests with `pytest` for Python functions and a small FastAPI application. Use assertions to check expected results and verify how code handles invalid input and missing records.

## 📝 Tasks

### 🛠️ Test Python Functions

#### Description
Install `pytest` with `python -m pip install pytest`. In the assignment directory, create `test_starter_code.py` and write tests for the functions in `starter_code.py`. Run your tests with `python -m pytest`.

#### Requirements
Completed test file should:

- Check `is_even()` with both even and odd numbers
- Check `celsius_to_fahrenheit()` with at least two temperatures, including `0` degrees Celsius
- Check `classify_score()` at grade boundaries and for a score in the middle of a grade range
- Use `pytest.raises(ValueError)` to check that `classify_score()` rejects scores below 0 and above 100

### 🛠️ Test FastAPI Endpoints

#### Description
Install the API testing dependencies with `python -m pip install fastapi httpx`. Create `test_book_api.py` and use FastAPI's `TestClient` to test the endpoints in `book_api.py`. Run both test files with `python -m pytest`; you do not need to start a web server.

#### Requirements
Completed test file should:

- Check that `GET /books` returns HTTP 200 and the expected book data
- Check that `GET /books/1` returns HTTP 200 and the requested book
- Check that requesting an unknown book ID returns HTTP 404
- Assert both response status codes and relevant JSON fields
- Optional stretch: create a pytest fixture for the test client and use `pytest.mark.parametrize` to test multiple IDs
