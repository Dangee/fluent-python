"""
Working with namedtuples
It is similar to creating a database table structure
where Card is the table name, and rank / suit are the columns.

the attributes in the [ ] act as the record primary key.
len() is equivalent to returning the number of rows in the table

items can be retrived using the row number (index)

Reference: Fluent Python, Pythonic Card Deck
"""
import collections
from random import choice

Card = collections.namedtuple('Card', ['rank','suit'])

class FrenchDeck:
    rank_list = [str(n) for n in range(2, 11)] + list('JQKA')
    suit_list = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suit_list for rank in self.rank_list]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
print(f"Number of cards in deck: {len(deck)}")
print(f"first card in the deck: {deck[0]}")
print(f"last card in the deck : {deck[-1]}")
print(f"first 3 cards in the deck: {deck[:3]}")
print(f"get the Aces: {deck[12::13]}") #  step 13 to get the same card rank
print("can also iterate through card deck using for card in deck")
print("can also iterate in reverse using for card in reversed(deck)")

beer_card = Card('7', 'diamonds')
print(f"Beer card: {beer_card}")
print(f"Random card this time: {choice(deck)}")

