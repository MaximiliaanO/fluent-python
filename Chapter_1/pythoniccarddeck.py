import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank) #returns the index of the first match in the named tuple list
    print(f"rank value: {rank_value}")
    return rank_value * len(suit_values) + suit_values[card.suit] #rank value index * 4 + 0-3 based on suits
    
print(spades_high(Card('10', 'hearts')))

for card in sorted(deck, key=spades_high):
    print(spades_high(card))
    print(card)

