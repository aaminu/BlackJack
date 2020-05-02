
import random


suits = ('Daimonds', 'Hearts', 'Spades', 'Clubs')
orders = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 
         'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9,
          'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


class Card:
    """Individual card class"""
    
    def __init__(self, suit, order):
        self.suit = suit
        self.order = order
        
    def __str__(self):
        return f'{self.order} of {self.suit}'

    
class DeckofCards:
    """Creates a deck of class"""
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for order in orders:
                self.deck.append(Card(suit, order)) #class Card class to creat a card object in the Deck
                
    def shuffle(self):
        "Randomly reshuffles deck"
        random.shuffle(self.deck)
        
    def deal(self):
        "pops a card from the back"
        deal_card = self.deck.pop()
        return deal_card
    
    def __str__(self):
        dck = ''
        for crd in self.deck:
            dck += '\n'+crd.__str__()
        return f'Available Cards in deck: {dck}'
    
    def __len__(self):
        return len(self.deck)
