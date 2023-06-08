fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

rfruits = reversed(fruits)
print(f"rfruits: {rfruits}")

for fruit in rfruits:
    print(fruit, end=' ')
print('\n')

print(f"rfruits: {rfruits}")

print('-' * 60)

for i, fruit in enumerate(fruits):
    print(f"{i:2d} {fruit}")






