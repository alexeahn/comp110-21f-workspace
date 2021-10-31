"""Practice with dictionaries."""

__author__ = "730389910"

# Define your functions below


# Invert function: by giving values, returns a flip of the values

def invert(first: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary."""
    switch: dict[str, str] = {}
    for key in first:
        value: str = first[key]
        switch[value] = key
    return switch 


# Favorite color: sort different colors based on what people like the most

def favorite_color(colors: dict[str, str]) -> str:
    """Gives the most frequently listed color."""
    favorite: str = ""
    for key in colors:
        value: str = colors[key]
        favorite = value 
    return favorite
        

# Count: shows how many times a certain key was given


def count(find: list[str]) -> dict[str, int]:
    """Counts how many times a string is presented.""" 
    i: int = 0
    final: dict[str, int] = {}
    
    while i < len(find):
        key = find[i]
        if key in final:
            final[key] += 1
        else:
            final[key] = 1
        i += 1
    return final
    

f: str = "blue"
g: str = "silver"
h: str = "gold"
link: list[str] = ["fish", "bird", "dog", "fish"]
print(invert({g: f}))
print(favorite_color({"Alex": f, "Jeff": f, "Joe": g}))
print(count(link))