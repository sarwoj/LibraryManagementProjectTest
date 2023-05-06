from datetime import date
from book import Book


class Order:
    def __init__(self, book, collect_date: "date", invalidation_date: "date") -> None:
        self._book = book
        self._collect_date = collect_date
        self._invalidation_date = invalidation_date

    @property
    def book(self) -> "Book":
        return self._book

    @property
    def collect_date(self) -> "date":
        return self._collect_date

    @property
    def invalidation_date(self) -> "date":
        return self._invalidation_date
