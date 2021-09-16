"""An exercise in remainders and boolean logic."""

__author__ = "730389910"


# Begin your solution here...
gdtbath: int = int(input("Enter an int: "))

if gdtbath % 14 == 0:  
    print("TAR HEELS")
else:
    if gdtbath % 2 == 0:
        print("TAR")
    else:
        if gdtbath % 7 == 0: 
            print("HEELS")
        else:
            print("CAROLINA")