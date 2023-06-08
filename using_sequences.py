colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow', 'black']

print(f"colors[0]: {colors[0]}")
print(f"colors[2]: {colors[2]}")
print(f"colors[-1]: {colors[-1]}")

print(f"colors[2:6]: {colors[2:6]}")
print(f"colors[:4]: {colors[:4]}")
print(f"colors[-3:]: {colors[-3:]}")

#  str, bytes, list, tuple

print(f"len(colors): {len(colors)}")

for color in colors:
    print(color.upper())

m = "abc"
for letter in m:
    print(letter)
