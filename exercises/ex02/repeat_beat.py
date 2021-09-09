"""Repeating a beat in a loop."""

__author__ = "7303-89910"


# Begin your solution here...
counter: int = 1

beat = ((input("What beat do you want to repeat? ")))

maximum: int = int(input("How many times do you want to repeat it? ")) 

if maximum <= 0:
    print("No beat...")
else:
    final_beat = beat
    while maximum > counter:
        final_beat = final_beat + " " + str(beat)
        counter = counter + 1
    
    print(final_beat)