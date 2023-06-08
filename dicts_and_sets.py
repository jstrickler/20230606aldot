# mapping types
from pprint import pprint

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
print(f"airports['YCC']: {airports['YCC']}")
print(f"airports.get('YCC'): {airports.get('YCC')}")
print(f"airports.get('XYZ'): {airports.get('XYZ')}")
print(f"airports.get('XYZ', 27): {airports.get('XYZ', 27)}")

for code, airport in sorted(airports.items()):
    print(code, airport)
print()

airports['MGM'] = 'Montgomery'

del airports['MCI']
pprint(airports, sort_dicts=False)

