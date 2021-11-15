"""Greetings and Parameters."""

from typing import Union


def hello(name: Union[str, int, float] = "World") -> str:
    """A greeting function."""
    result: str = "Hello, "
    if isinstance(name, str):
        return result + name
    elif isinstance(name, float):
        return result + "Alien from sector " + str(name)
    else:
        return result + "COMP" + str(name)


#Calling Hello with no argument to use default value
#print(hello())
#Calling Hello with an argument overrides the default parameter
print(hello("Alex"))
print(hello(110))
print(hello(3.14))