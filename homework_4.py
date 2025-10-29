'''Задача 1. Базовые модели
Создайте следующие Pydantic-модели:
Book
– title: str
– author: str
– year: int
– available: bool
User
– name: str
– email: str (с валидацией email)
– membership_id: str

Задача 2. Функции с аннотациями типов
Напишите следующие функции, используя аннотации типов:

add_book(...) -> ...
find_book(...) -> ...
is_book_borrow(...) -> ...
return_book(...) -> ...
Задача 3. Расширенная модель и валидация

Создайте модель Library:
– books: …
– users: …
Добавьте в модель Book поле categories: List[str] с валидацией.
Реализуйте метод total_books() -> ... для модели Library.
Задача 4. Обработка ошибок и исключения

Создайте исключение BookNotAvailable.
Измените функцию is_book_borrow, чтобы она вызывала BookNotAvailable при необходимости.
Напишите декоратор log_operation для логирования операций с книгами*.
Задача повышенной сложности, выполняется по желанию.'''

from typing import List, Optional
from pydantic import BaseModel, EmailStr, field_validator
from functools import wraps

class Book(BaseModel):
    title: str
    author: str
    year: int
    available: bool
    categories: Optional[List[str]] = []

    @field_validator('categories')
    @classmethod
    def validate_categories(cls, value):
        if not isinstance(value, list):
            raise ValueError("Categories must be a list of strings")
        if any(not isinstance(cat, str) for cat in value):
            raise ValueError("All categories must be strings")
        return value


class User(BaseModel):
    name: str
    email: EmailStr
    membership_id: str



def add_book(library_books: List[Book], book: Book) -> None:
    library_books.append(book)


def find_book(library_books: List[Book], title: str) -> Optional[Book]:
    for book in library_books:
        if book.title.lower() == title.lower():
            return book
    return None


class BookNotAvailable(Exception):
    pass


def log_operation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Function '{func.__name__}' executed successfully.")
        return result
    return wrapper


@log_operation
def is_book_borrow(book: Book) -> bool:
    if not book.available:
        raise BookNotAvailable(f"Книга '{book.title}' сейчас недоступна.")
    book.available = False
    return True


@log_operation
def return_book(book: Book) -> bool:
    book.available = True
    return True


class Library(BaseModel):
    books: List[Book]
    users: List[User]

    def total_books(self) -> int:
        return len(self.books)
