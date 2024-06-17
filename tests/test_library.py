from library.library import Library
from library.book import Book
import pytest

library = Library()
book1 = Book("blabla", "author")
book2 = Book("toto", "author xqcq")
book3 = Book("tutu", "author 344")


def test_add_book():
    library.add_book(book1)
    assert book1 in library.books


def test_remove_book():
    library.add_book(book2)
    library.remove_book(book2)
    assert book2 not in library.books


def test_find_book_by_title():
    library.add_book(book3)
    assert library.find_book_by_title("tutu") == book3
    library.remove_book(book3)
    assert library.find_book_by_title("tutu") is None


def test_list_books(library, book1, book2):
    library.add_book(book1)
    library.add_book(book2)
    book_list = library.list_books()
    assert "blabla" in book_list
    assert "toto" in book_list
