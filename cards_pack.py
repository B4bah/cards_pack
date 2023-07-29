import random
from random import shuffle


class Card:
    def __init__(self, nameN, suit):
        names = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.name = names[nameN]
        if suit == 0:
            self.suit = '♥'
        elif suit == 1:
            self.suit = '♠'
        elif suit == 2:
            self.suit = '♦'
        elif suit == 3:
            self.suit = '♣'

    def __repr__(self):
        return f'{self.name}{self.suit}'


cards_pack = [Card(u, i) for i in range(4) for u in range(13)]

shuffle(cards_pack)  # Randomising the cards_pack

for i in range(52):
    print(cards_pack[i], end=' ')
