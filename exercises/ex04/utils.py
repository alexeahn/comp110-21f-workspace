"""List utility functions."""

__author__ = "730389910"


# TODO: Implement your functions here.

# function 1: deriving a single number for all sequences

def all(sequence: list[int], number: int) -> bool:
    """Testing if all numbers in a list are the same."""
    i: int = 0
    if len(sequence) == 0:
        return False
    while i < len(sequence):
        if sequence[i] != number:    
            return False
        i += 1
    return True


# function 2: matching the same sequence to a list


def is_equal(initial: list[int], test: list[int]) -> bool:
    """Testing if two sequences are the same."""
    i: int = 0

    if len(initial) != len(test):
        return False
    while i < len(initial):
        if initial[i] != test[i]:    
            return False
        i += 1
    return True


# function 3: maximum function creation


def max(sequence: list[int]) -> int:
    """Finding the max within a list of int."""
    i: int = 0
    most: int = sequence[0]

    if len(sequence) == 0:
        raise ValueError("max() arg is an empty List")
    
    while i < len(sequence):
        print(sequence[i])
        if sequence[i] > most:
            most = sequence[i]
        i += 1
    return most