from carddeck import CardDeck, Card

class JokerDeck(CardDeck):
    JOKER = '\U0001F0CF'

    def _make_deck(self):
        super()._make_deck()
        for _ in range(2):
            self._cards.append(Card(self.JOKER, None))



