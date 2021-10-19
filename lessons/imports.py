"""Examples of imports."""

from lessons import helpers

# Import using an alias
from lessons import helpers as hp

# Import names directly from globals of a module
from lessons.helpers import powerful


def main() -> None:
    # Access the first import
    print(helpers.powerful(2, 4))

    # Acess the function directly
    print(powerful(2, 4))

    # Aliased import
    print(hp.THE_ANSWER)

    # name
    print(f"imports.py: {__name__}")