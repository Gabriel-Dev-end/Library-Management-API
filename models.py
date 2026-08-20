import sqlalchemy as sa
import sqlalchemy.orm as orm
from database import Base
import enum
import datetime

class Book(Base):
    __tablename__ = "books"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    title = sa.Column(sa.String, nullable=False)
    author = sa.Column(sa.String, nullable=False)
    published_date = sa.Column(sa.Date, nullable=True)
    isbn = sa.Column(sa.String, unique=True, nullable=True)
    pages = sa.Column(sa.Integer, nullable=True)
    cover_image_url = sa.Column(sa.String, nullable=True)
    language = sa.Column(sa.String, nullable=True)
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    updated_at = sa.Column(sa.DateTime, default=datetime.datetime.now(datetime.timezone.utc), onupdate=datetime.datetime.now(datetime.timezone.utc))

    loans = orm.relationship("Loan", back_populates="book", cascade="all, delete-orphan")

class Loan(Base):
    __tablename__ = "loans"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    book_id = sa.Column(sa.Integer, sa.ForeignKey("books.id"), nullable=False)
    borrower_name = sa.Column(sa.String, nullable=False)
    loan_date = sa.Column(sa.Date, default=datetime.date.today)
    return_date = sa.Column(sa.Date, nullable=True)
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    updated_at = sa.Column(sa.DateTime, default=datetime.datetime.now(datetime.timezone.utc), onupdate=datetime.datetime.now(datetime.timezone.utc))
    status = sa.Column(sa.Enum("loaned", "returned", name="loan_status"), default="loaned")

    book = orm.relationship("Book", back_populates="loans")

