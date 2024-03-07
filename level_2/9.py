import datetime
from typing import TypeAlias
from constants import ___

Product: TypeAlias = list[tuple[str, int, float]]


def parse_receipt(raw_receipt: str) -> tuple[int, datetime.date, Product]:
    pass


if __name__ == "__main__":
    assert parse_receipt(
        raw_receipt="Кассовый чек 12 Продажа Позиции: ...",
    ) == (12, datetime.date(2022, 6, 12), [("Молоко", 1, 32.2)])
