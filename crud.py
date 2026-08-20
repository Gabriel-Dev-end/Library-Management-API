from sqlalchemy.orm import Session
import models, schemas
import datetime

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, book_update: schemas.BookUpdate):
    db_book = get_book(db, book_id)
    if db_book:
        for key, value in book_update.model_dump(exclude_unset=True).items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = get_book(db, book_id)
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book

def create_loan(db: Session, loan: schemas.LoanCreate):
    db_book = get_book(db, loan.book_id)
    if not db_book:
        raise ValueError("Book not found") 
    db_loan = models.Loan(**loan.model_dump(),status="loaned", loan_date=datetime.date.today())
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan

def return_loan(db: Session, loan_id: int):
    db_loan = db.query(models.Loan).filter(models.Loan.id == loan_id).first()
    if db_loan and db_loan.status != "returned":
        db_loan.return_date = datetime.date.today()
        db_loan.status = "returned"
        db.commit()
        db.refresh(db_loan)
    return db_loan