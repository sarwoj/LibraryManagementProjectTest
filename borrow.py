from datetime import date
from book import Book


class Borrow:
    def __init__(self, book: "Book", return_date: "date") -> None:
        self._book = book
        self._return_date = return_date

    @property
    def book(self) -> "Book":
        return self._book

    @property
    def return_date(self) -> "date":
        return self._return_date

    def __str__(self) -> str:
        book_str = str(self._book).replace('\n', '\n\t')
        return f"Borrowed:\n\t{book_str}\nReturn date: {self._return_date}"


def main():
    book = Book("Ania z zielonego", date(1998, 12, 1), "Lucy Maud Montgomery", 7826, 2)
    borrow = Borrow(book, date(2023, 6, 13))
    print(borrow)


if __name__ == "__main__":
    main()
