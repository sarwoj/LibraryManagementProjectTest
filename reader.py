class Reader:

    unique_number = 1

    def __init__(self, name) -> None:
        self._name = name
        self._number = Reader.unique_number
        Reader.unique_number += 1

    @property
    def name(self):
        return self._name

    @property
    def number(self):
        return self._number

    def __str__(self) -> str:
        return f"{self._name} : {self._number}"


def main():
    p1 = Reader("A")
    p2 = Reader("B")
    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
