"""List utility functions part 2."""

__author__ = "730389910"

# Define your functions below

def only_evens(start: list[int]) -> list[int]:
    """Returns the even numbers in a sequence."""
    i: int = 0
    evens: list[int] = []
    while i < len(start):
        if start[i] % 2 == 0:
            evens.append(start[i])
        i += 1
    return evens

def sub(sequence: list[int], start: int, end: int) -> list[int]:
    """Returns a portion of a list defined by parameters."""
    final: list[int] = []
    if start < 0:
        start = 0
    if end > len(sequence):
        end = len(sequence)
    while start < end:
        final.append(sequence[start])
        start += 1
    return final

def concat(first: list[int], second: list[int]) -> list[int]:
    """Concats one list onto another list."""
    i: int = 0
    f: int = 0
    final: list[int] = []
    while i < len(first):
        final.append(first[i])
    i += 1
    print(final)
    while f < len(second):
        final.append(second[i])
    f += 1
    print(final)
    return final

a_list = [1, 2, 3]
b_list = [4, 5, 6]
print(concat(a_list, b_list))