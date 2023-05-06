from borrow_register import BorrowRegister
from order_register import OrderRegister
from penalty_register import PenaltyRegister
from available_books import AvailableBooks
from book import Book
from reader import Reader
from borrow import Borrow
from penalty import Penalty
from datetime import date, timedelta


class InvalidBorrow(Exception):
    pass


class Library:
    penalty_per_day = 24  # in gr

    def __init__(self) -> None:
        self._borrows = BorrowRegister()
        self._orders = OrderRegister()
        self._penalties = PenaltyRegister()
        self._book = AvailableBooks()
        self._date = date.today()

    @property
    def date(self) -> "date":
        return self._date

    @date.setter
    def date(self, new_date: "date") -> None:
        self._date = new_date
        invalid_orders = self._orders.update_orders(self._date)
        for order in invalid_orders:
            self._book.add_book(order.book)

    def add_book(self, new_book: "Book"):
        self._book.add_book(new_book)

    def borrow_book(self, reader: "Reader", isbn_number: int):
        if self._borrows.check_for_overdue(reader):
            raise InvalidBorrow(f"Can't borrow. Reader {reader} has overdue books!")
        borrowed_book = self._book.pop_book(isbn_number)
        return_time = self._date + timedelta(days=30)
        new_borrow = Borrow(borrowed_book, return_time)
        self._borrows.add_borrow(reader, new_borrow)

    def return_book(self, reader: "Reader", isbn_number: int, copy_number: int):
        reader_borrow = self._borrows.pop_borrow(reader, isbn_number, copy_number)
        self._book.add_book(reader_borrow.book)

        # add penalty if returned to late
        if reader_borrow.return_date < self._date:
            days_missed = (self._date - reader_borrow.return_date).days
            new_penalty = Penalty(days_missed * Library.penalty_per_day)
            self._penalties.add_penalty(reader, new_penalty)

    def order_book(self, reader: "Reader", isbn_number: int):
        """Zamow ksiazke"""
        pass

    def realize_order(self, reader, isbn_number):
        """Zamien zamowienie na pozyczenie"""
        pass

    def pay_penalty(self, reader, penalty_amount):
        pass


def main():
    # Tworzymy biblioteke i ustawiamy czas
    my_library = Library()
    my_library.date = date(2023, 5, 1)
    # Tworzymy czytelnikow
    reader1 = Reader("xXx_Predator_xXx")
    reader2 = Reader("BoyKisser2004")
    # Dodajemy ksiazki do biblioteki
    book1 = Book("Ania z zielonego", date(1998, 12, 1), "Lucy Maud Montgomery", 7826, 1)
    book2 = Book("Ania z zielonego", date(1998, 12, 1), "Lucy Maud Montgomery", 7826, 2)
    book3 = Book("Sherlock Holmes: Boy Kisser Mystery", date(1998, 10, 31), "Conan Doyle Arthur", 6786, 1)
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)
    del book1, book2, book3
    # Pozyczamy ksiazki
    my_library.borrow_book(reader1, 7826)
    my_library.borrow_book(reader2, 7826)
    my_library.borrow_book(reader2, 6786)
    # Zwracamy ksiazke
    my_library.date = date(2023, 5, 15)
    my_library.return_book(reader1, 7826, 1)
    my_library.return_book(reader2, 6786, 1)
    # Zwracamy ksiazke po czasie
    my_library.date = date(2023, 7, 1)
    my_library.return_book(reader2, 7826, 2)
    pass


if __name__ == "__main__":
    main()
