from typing import Dict, List
from borrow import Borrow
from reader import Reader


class NotABorrowedBook(Exception):
    pass


class BorrowRegister:
    _borrows: Dict[int, List[Borrow]]

    def __init__(self) -> None:
        self._borrows = {}

    def add_borrow(self, reader: "Reader", new_borrow: "Borrow") -> None:
        """Adds a borrow to reader."""
        if not self._borrows.get(reader.number):
            self._borrows[reader.number] = []
        self._borrows[reader.number].append(new_borrow)

    def pop_borrow(self, reader: "Reader", isbn_number: int, copy_number: int) -> Borrow:
        """Removes and returns a borrow corresponding to provided parameters."""
        for borrow in self._borrows[reader.number]:
            if not borrow.book.isbn_number == isbn_number:
                continue
            if not borrow.book.copy_number == copy_number:
                continue

            self._borrows[reader.number].remove(borrow)

            # Remove list under reader number if list is empty
            if not len(self._borrows[reader.number]):
                del self._borrows[reader.number]

            return borrow
        raise NotABorrowedBook(f"Reader: {reader}\ndidn't borrow book with:\nisbn number: {isbn_number}\ncopy number: {copy_number}")

    def check_for_overdue(self, reader: "Reader", current_date) -> bool:
        """Check if reader has overdue book."""
        if not self._borrows.get(reader.number):
            return False
        for borrow in self._borrows[reader.number]:
            if borrow.return_date > current_date:
                return True
        return False
