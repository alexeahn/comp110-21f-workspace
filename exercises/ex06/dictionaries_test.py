"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730389910"


# tests for invert


def test_invert_one() -> None:
    """Test for first."""
    tester: dict[str, str] = {}
    assert invert(tester) == {}


def test_invert_two() -> None:
    """Test for second."""
    second_tester: dict[str, str] = {"gold": "silver"}
    assert invert(second_tester) == {"silver": "gold"}


def test_invert_three() -> None:
    """Test for third."""
    third_tester: dict[str, str] = {"silver": "gold"}
    assert invert(third_tester) == {"gold": "silver"}


def test_favorite_color_one() -> None:
    """Favorite color test one."""
    first_color: dict[str, str] = {}
    assert favorite_color(first_color) == {}


def test_favorite_color_two() -> None:
    """Favorite color test one."""
    second_color: dict[str, str] = {}
    assert favorite_color(second_color) == {}


def test_favorite_color_three() -> None:
    """Favorite color test one."""
    tester: dict[str, str] = {}
    assert favorite_color(tester) == {}


def test_count_one() -> None:
    """Count test one."""
    test_one: dict[str, str] = {}
    assert count(test_one) == {}


def test_count_two() -> None:
    """Count test two."""
    test_two: dict[str, str] = {}
    assert count(test_two) == {}


def test_count_three() -> None:
    """Count test three."""
    third_tester: dict[str, str] = {}
    assert count(third_tester) == {}