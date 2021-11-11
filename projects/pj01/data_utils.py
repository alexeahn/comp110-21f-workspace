"""Utility functions."""

__author__ = "7303-89910"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a csv rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row: 
        result[column] = column_values(row_table, column)

    return result


def head(data: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Returns a specificed number of columns."""
    result: dict[str, list[str]] = {}
    i: int = 0

    for column in data:
        empty_list: list[str] = []
    
        if rows > len(data[column]):
            result = data

        else:
            for i in range(rows):
                empty_list.append(data[column][i])
            result[column] = empty_list

    return result


def select(data_two: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Allows viewer to choose which columns to read."""
    result: dict[str, list[str]] = {}

    for column in data_two:
        if column in names:
            result[column] = data_two[column]

    return result


def concat(entry_one: dict[str, list[str]], entry_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concats two entries side by side."""
    result: dict[str, list[str]] = {}

    return result


def count(freq: list[int]) -> dict[str, int]:
    """Counts the frequency of values given a category."""
    result: dict[str, int] = {}

    

    return result
