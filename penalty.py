class Penalty:
    def __init__(self, price_gr) -> None:
        self._price = price_gr

    @property
    def amount(self):
        return self._price

    def __str__(self) -> str:
        price_zl, price_gr = divmod(self._price, 100)
        return f"{price_zl},{str(price_gr).zfill(2)} zl"


def main():
    pen = Penalty(2400)
    print(pen)


if __name__ == "__main__":
    main()
