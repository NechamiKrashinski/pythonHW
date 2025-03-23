from library import Library
from book import Book
import pytest

#בדיקה שהפונקציה מוסיפה ספר חדש לרשימת הספרים במערכת.
def test_add_book():
    library = Library()
    book = Book("hello world","Israel")
    library.add_book(book)
    assert len(library.books)==1
    assert library.books[0]==book


# בדיקה שהפונקציה מוסיפה משתמש חדש לרשימת המשתמשים.
def test_add_user():
    library = Library()
    library.add_user("shalom")
    assert len(library.users) == 1
    assert library.users[0] == "shalom"

#בדיקה שהספר הושאל בהצלחה למשתמש רשום.
def test_check_out_book():
    library = Library()
    library.add_user("shalom")
    book = Book("hello world","Israel")
    library.add_book(book)
    library.check_out_book("shalom",book)
    assert library.checked_out_books["shalom"]==book
    assert book.is_checked_out == True

#בדיקה שהספר מוחזר בהצלחה לאחר שהושאל.
def test_return_book():
    library = Library()
    library.add_user("shalom")
    book = Book("hello world","Israel")
    library.add_book(book)
    library.check_out_book("shalom", book)
    library.return_book("shalom",book)
    assert library.checked_out_books["shalom"] is not book
    assert book.is_checked_out == False


def test_search_books():
    library = Library()
    book = Book("hello world","Israel")
    book1 = Book("world","Israel")
    library.add_book(book)
    assert book in library.search_books("llo")
    assert book1 not in  library.search_books("llo")
