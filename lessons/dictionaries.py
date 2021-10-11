"""Demonstrations of dictionary capabilities"""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["DUKE"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

# Access a value by its key -- "Lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key value pair from a dictionary
# By its key
schools.pop("DUKE")

# Test for the existance of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

print(schools)

# Update / Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictoinary literals

# Empty dictionary literal
schools = {} # Same as a dict()
print(schools)

# Alternatively, initialize key-value pairs
schools = {
    "UNC": 19400, "Dukie": 6717, "NCSU": 26150
}
print(schools)

# Example looping over the keys of a dict
for key in schools:
    print(f"key: {schools} -> Value: {schools[school]}")