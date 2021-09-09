"""Program that outputs one of at least four random, good fortunes."""

__author__ = "7303-89910"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
ft: int = int(randint(1,4))

if ft <= 1:
    print("You will have a good day.")
else:
    if ft <= 2:
        print("You will have a blessed day.")
    else:
        if ft <= 3:
            print("You will discover a pot of gold.")
        else:
            print("You will have a piano fall on your head.")


print("Now, go spread positive vibes!")