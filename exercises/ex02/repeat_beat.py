"""Repeating a beat in a loop."""

__author__ = "7303-89910"


# Begin your solution here...
counter: int = 0

beat = ((input("What beat do you want to repeat? ")))

maximum: int = int(input("How many times do you want to repeat it? ")) 

fb = ""
if maximum <= 0:
    print("No beat...")
else:
    while maximum > counter:
        fb = fb + str(beat) + " "
        counter = counter + 1
    print(fb)