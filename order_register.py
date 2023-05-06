from typing import Dict, List
from datetime import date
from order import Order
from reader import Reader


class NotAnOrder(Exception):
    pass


class OrderRegister:
    _orders: Dict[int, List[Order]]

    def __init__(self) -> None:
        self._orders = {}

    def add_order(self, reader: "Reader", new_order: "Order"):
        if not self._orders.get(reader.number):
            self._orders[reader.number] = []
        self._orders[reader.number].append(new_order)

    def pop_order(self, reader: "Reader", isbn_number):
        for order in self._orders[reader.number]:
            if order.book.isbn_number == isbn_number:
                self._orders[reader.number].remove(order)
                return order
        raise NotAnOrder(f"No order for {isbn_number} for {reader}")

    def update_orders(self, current_date: "date") -> List[Order]:
        invalid_orders = []
        for reader_number, orders in self._orders.items():
            for order in orders:
                if order.invalidation_date > current_date:
                    invalid_orders.append(order)
                    self._orders[reader_number].remove(order)
        return invalid_orders