"""Utility functions for the project."""
from adventOfCode.paths import INPUTS_DIR


def binary_to_decimal(binary: str) -> int:
    """Converts a binary number to a decimal number."""
    return int(binary, 2)

def import_input(file_name: int | str) -> list[str]:
    """Reads a file and returns its content."""
    with open(INPUTS_DIR / f"{str(file_name)}.txt", encoding="utf-8") as f:
        return f.read().splitlines()