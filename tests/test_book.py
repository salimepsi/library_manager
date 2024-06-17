from library.book import Book


def test_book_creation():
    book_GO = Book("1984", "George Orwell")
    assert book_GO.title == "1984"
    assert book_GO.author == "George Orwell"
    assert str(book_GO) == "1984 by George Orwell"
# Test de la création d'un livre
