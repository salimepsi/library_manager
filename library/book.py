# Book : Représente un livre avec un titre et un auteur.
# Library : Gère une collection de livres et permet d'ajouter, de retirer et de rechercher des livres.


# Code à tester
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            raise ValueError("Book not found in the library")

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def list_books(self):
        return [str(book) for book in self.books]