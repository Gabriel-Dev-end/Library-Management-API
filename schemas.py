from pydantic import BaseModel
import datetime

class BookBase(BaseModel):
    title: str
    author: str
    isbn: str | None
    pages: int | None
    cover_image_url: str | None
    language: str | None
    published_date: datetime.datetime | None


class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    published_date: datetime.datetime | None

    class Config:
        from_attributes = True

class LoanBase(BaseModel):
    book_id: int
    borrower_name: str

class LoanCreate(LoanBase):
    pass

class LoanResponse(LoanBase):
    id: int
    loan_date: datetime.date
    return_date: datetime.date | None
    status: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True