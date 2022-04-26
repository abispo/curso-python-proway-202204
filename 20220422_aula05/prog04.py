"""
Orientação a Objetos: Composição

Dizemos que uma classe pode ser composta ou pode compor outras classes.
Por exemplo, um objeto de consulta ao banco de retorna outros objetos.

Vamos implementar um baralho

"""


class DeckOfCards:

    def __init__(self):

        self._counter = -1
        self._cards_list = []
        self._card_values = [
            '2', '3', '4', '5', '6', '7', '8', '9', '10',
            'J', 'Q', 'K', 'A'
        ]
        self._card_suits = ['\u2660', '\u2665', '\u2663', '\u2666']
        self._build_deck()

    def __iter__(self):
        return self

    def __next__(self):
        self._counter += 1
        if self._counter < len(self._cards_list):
            return self._cards_list[self._counter]

        raise StopIteration

    def _build_deck(self):
        for suit in self._card_suits:
            for value in self._card_values:
                self._cards_list.append(Card(value, suit))


class Card:

    def __init__(self, value, suit):
        self._value = value
        self._suit = suit

    def __str__(self):
        return f"<Card({self._suit}{self._value})>"


if __name__ == '__main__':

    deck_of_cards = DeckOfCards()

    for card in deck_of_cards:
        print(card)
