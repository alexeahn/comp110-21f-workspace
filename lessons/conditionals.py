"""An example of conditional (if-else) statements"""

SECRET: int = 3

print("I'm thinking of a number between 1 and 5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!")
    print("Good work soldier!")
else:
    print("Sorry, das the wrong numba!")
    if guess > SECRET:
        print("You guessed too high.")
    else :
        print("You guessed too low.")

print("Game over.")