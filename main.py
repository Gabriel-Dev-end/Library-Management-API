from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Personal Library & Loan Management API",
    description="Library management system for tracking books and loans, allowing users to manage their personal library and loan records.",
    version="1.0.0"
)

@app.post("/books/", response_model=schemas.BookResponse, status_code = status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    if crud.get_book_by_title(db=db, title=book.title):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Book with this title already exists")
    return crud.create_book(db=db, book=book)

@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return db_book

@app.get("/books/", response_model=list[schemas.BookResponse])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_books(db=db, skip=skip, limit=limit)

@app.patch("/books/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book_update: schemas.BookUpdate, db: Session = Depends(get_db)):
    db_book = crud.update_book(db=db, book_id=book_id, book_update=book_update)
    if db_book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return db_book

@app.delete("/books/{book_id}", response_model=schemas.BookResponse, status_code=status.HTTP_200_OK)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return db_book

@app.post("/loans/", response_model=schemas.LoanResponse)
def create_loan(loan: schemas.LoanCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_loan(db=db, loan=loan)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@app.patch("/loans/{loan_id}", response_model=schemas.LoanResponse)
def update_loan(loan_id: int, loan_update: schemas.LoanUpdate, db: Session = Depends(get_db)):
    db_loan = crud.update_loan(db=db, loan_id=loan_id, loan_update=loan_update)
    if db_loan is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Loan not found")
    return db_loan
