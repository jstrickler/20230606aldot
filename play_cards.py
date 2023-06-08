"""
Play a game of cards
"""
from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck('Molly')   # CardDeck.__init__()
print(f"d1: {d1}")

d2 = CardDeck('Bela')  # separate deck

# VERY NAUGHTY
# print(f"d1._dealer: {d1._dealer}")

print(f"d1.dealer: {d1.dealer}")
print(f"d2.dealer: {d2.dealer}")

d2.dealer = "Sierra"
print(f"d2.dealer: {d2.dealer}")

# d2.dealer = 42  NO CAN DO

d1.shuffle()
print(d1.cards)
print('-' * 60)

for _ in range(7):
    card = d1.draw()
    print(f"card: {card}")
print()

print(f"d1.get_suits(): {d1.get_suits()}")

print(f"CardDeck.get_suits(): {CardDeck.get_suits()}")

j = JokerDeck("Alfonso")
print(f"j: {j}")
j.shuffle()
print(j.cards)
print()
