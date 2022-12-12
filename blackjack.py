import random

SUITS = ['♥️', '♣️', '♦️', '♠️']
RANKS = ['A', 'J', 'Q', 'K', 2, 3, 4, 5, 6, 7, 8, 9, 10]


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self, suits, ranks):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.cards.append(new_card)

    def __str__(self):
        deck_as_string = ''
        for card in self.cards:
            deck_as_string += f"{card}  "
        return deck_as_string

    def shuffle(self):
        random.shuffle(self.cards)
    

class Game:
    def __init__(self):
        self.deck = Deck(SUITS, RANKS)
        # create a deck
        # shuffle deck

new_game = Game()
print(new_game.deck)