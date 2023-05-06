from datetime import date


class Book:
    def __init__(self, title: "str", release_date: "date", author: "str", isbn_number: int, copy_number: int) -> None:
        self._title = title
        self._release_date = release_date
        self._author = author
        self._isbn_number = isbn_number
        self._copy_number = copy_number

    @property
    def title(self) -> str:
        return self._title

    @property
    def release_date(self) -> "date":
        return self._release_date

    @property
    def author(self) -> str:
        return self._author

    @property
    def isbn_number(self) -> int:
        return self._isbn_number

    @property
    def copy_number(self) -> int:
        return self._copy_number

    def __str__(self) -> str:
        return f"\"{self._title}\" ~ {self._author}\n\tPublished in {self._release_date}\n\tISBN: {self._isbn_number}\n\tCopy nr: {self._copy_number}"


def main():
    book1 = Book("Ania z zielonego", date(1998, 12, 1), "Lucy Maud Montgomery", 7826, 1)
    book2 = Book("Ania z zielonego", date(1998, 12, 1), "Lucy Maud Montgomery", 7826, 2)
    book3 = Book("Sherlock Holmes: Boy Kisser Mystery", date(1998, 10, 31), "Conan Doyle Arthur", 6786, 1)
    print(book1, end="\n\n")
    print(book2, end="\n\n")
    print(book3, end="\n\n")


if __name__ == "__main__":
    main()
