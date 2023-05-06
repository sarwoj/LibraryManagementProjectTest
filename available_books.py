from typing import List
from book import Book
from datetime import date


class NoBookFound(Exception):
    pass


class AvailableBooks:
    _books: List["Book"]

    def __init__(self) -> None:
        self._books = []

    def add_book(self, new_book: "Book") -> None:
        """Add books to self."""
        self._books.append(new_book)

    def pop_book(self, isbn_number: int) -> "Book":
        """
        Removes and returns a book from self.

        Throws a NoBookFound exception if book not in self.
        """
        for book in self._books:
            if book.isbn_number == isbn_number:
                self._books.remove(book)
                return book
        raise NoBookFound("No book with that number")

    def __str__(self) -> str:
        return_string = ""
        for book in self._books:
            return_string += str(book)
            return_string += '\n'

        return return_string[:-1]


def main():
    av_book = AvailableBooks()
    av_book.add_book(Book("A", date(1998, 1, 1), "A A", 1, 1))
    av_book.add_book(Book("B", date(1998, 1, 1), "B B", 2, 1))
    av_book.add_book(Book("C", date(1998, 1, 1), "C C", 3, 1))
    av_book.add_book(Book("D", date(1998, 1, 1), "D D", 4, 1))

    print(av_book)

    book = av_book.get_book(3)

    print(f"-------------\nAfter taking out:\n{book}\n-------------")
    print(av_book)


if __name__ == "__main__":
    main()
