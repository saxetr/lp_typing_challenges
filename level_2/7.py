from typing import TypeAlias
from constants import ___

User: TypeAlias = tuple[str, int, list[int]]


def calculate_total_spent_for_user(user: User) -> int:
    pass


if __name__ == "__main__":
    assert calculate_total_spent_for_user(user=("Ilya", 32, [102, 15, 63, 12])) == 192
