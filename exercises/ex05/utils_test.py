"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730389910"

# tests for only_evens


def test_only_evens_no_value() -> None:
    """Test for nothing."""
    start: list[int] = []
    assert only_evens(start) == []


def test_only_evens_odd() -> None:
    """Test for odds."""
    start: list[int] = [1, 3, 5]
    assert only_evens(start) == []


def test_only_evens_even() -> None:
    """Test for evens."""
    start: list[int] = [2, 4, 6]
    assert only_evens(start) == [2, 4, 6]


# tests for sub


def test_sub_one() -> None:
    """Test for nothing."""
    start: list[int] = []
    assert only_evens(start) == []


def test_sub_two() -> None:
    """Test for odds."""
    start: list[int] = [1, 3, 5]
    assert only_evens(start) == []


def test_sub_three() -> None:
    """Test for evens."""
    start: list[int] = [2, 4, 6]
    assert only_evens(start) == [2, 4, 6]


# tests for concat


def test_concat_one() -> None:
    """Test for nothing."""
    start: list[int] = []
    assert only_evens(start) == []


def test_concat_two() -> None:
    """Test for odds."""
    start: list[int] = [1, 3, 5]
    assert only_evens(start) == []


def test_concat_three() -> None:
    """Test for evens."""
    start: list[int] = [2, 4, 6]
    assert only_evens(start) == [2, 4, 6]