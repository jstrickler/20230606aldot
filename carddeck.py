from dataclasses import dataclass
import random

@dataclass
class Card:
    rank: str
    suit: str

class CardDeck:   #  object
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    CLUB = '\u2663\uFE0F'  #  FE0F converts chars to emoji
    DIAMOND = '\u2666\uFE0F'
    HEART = '\u2665\uFE0F'
    SPADE = '\u2660\uFE0F'
    SUITS = CLUB, DIAMOND, HEART, SPADE

    # self is the *instance* of the class
    def __init__(self, dealer):
        self._dealer = dealer  # save data
        self._make_deck()

    # 1. getter method
    # 2. getter property

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards
    
    # cards = property(cards)

    @property
    def dealer(self):  # getter property
        return self._dealer
    
    @dealer.setter
    def dealer(self, value):  # setter property
        if isinstance(value, str):
            self._dealer = value
        else:
            raise TypeError("Dealer must be a str")

    def shuffle(self):
        random.shuffle(self._cards)
    
    def draw(self):
        return self._cards.pop()

    @classmethod
    def get_suits(cls):
        return cls.SUITS

if __name__ == "__main__":
    c = Card('2', 'Clubs')
    print(f"c: {c}")
    print(f"repr(c): {repr(c)}")

    k = Kard('2', 'Clubs')
    print(f"k: {k}")
    print(f"repr(k): {repr(k)}")
    
    
    