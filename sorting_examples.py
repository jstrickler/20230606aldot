fruits = ['pomegranate', 'cherry', 'apricot', 'Apple',
'lemon', 'Kiwi', 'ORANGE', 'lime', 'Watermelon', 'guava', 
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon', 
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]

f1 = sorted(fruits)
print(f"f1: {f1}\n")

f2 = sorted(fruits, key=str.lower)
print(f"f2: {f2}\n")

f3 = sorted(fruits, key=len)
print(f"f3: {f3}\n")

def len_and_name(item):
    return len(item), item.lower()

f4 = sorted(fruits, key=len_and_name)
print(f"f4: {f4}\n")

numbers = [5, -3, 18, 16, 4, 33, 9, 2]
n1 = sorted(numbers)
print(f"n1: {n1}\n")


people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

def by_dob(person):
    return person[3], person[1], person[0]  # return 4th element

for person in sorted(people, key=by_dob):
    print(person)
print('-' * 60)

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

for code, city in sorted(airports.items()):
    print(code, city)
print('-' * 60)

def by_value(item):
    return item[1], item[0]   # return value, key

for code, city in sorted(airports.items(), key=by_value):
    print(code, city)
print()

f6 = sorted(fruits, key=lambda f: f[-1])
print(f"f6: {f6}\n")

# lambda params: (return-value)

f7 = sorted(fruits, key=lambda f: (len(f), f.lower()))
print(f"f7: {f7}\n")
