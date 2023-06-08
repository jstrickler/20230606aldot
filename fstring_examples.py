user_name = "Fred Martin"
city = "Milwaukee"
value = 49.4283909332390

print(user_name, city, value)

print(city + ', ' + user_name)
print(f"{city}, {user_name}")
print("{}, {}".format(city, user_name))
print()

data = [
    ("Virginia", "Richmond"),
    ("Alabama", "Montgomery"),
    ("North Carolina", "Raleigh"),
    ("Texas", "Austin"),
]

for state, capital in data:
    print(f"{state:14} {capital}")
print()

print(f"value is {value:.3f}    ")
