from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Books API")


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int


class Book(BookCreate):
    id: int


books: dict[int, Book] = {}
next_book_id = 1


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate) -> Book:
    # Create a book, assign its ID, and store it.
    pass


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    # Return all books.
    pass


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    # Return the requested book or raise a 404 error.
    pass


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: BookCreate) -> Book:
    # Replace the book's data or raise a 404 error.
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> None:
    # Delete the book or raise a 404 error.
    pass
