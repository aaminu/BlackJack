
import random
from time import sleep

SUITS = ('Diamonds', 'Hearts', 'Spades', 'Clubs')
ORDERS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
UNI = {'Diamonds': '\u2666', 'Hearts': '\u2665', 'Spades': '\u2660', 'Clubs': '\u2663'}

class Card:
    """Individual card class"""

    def __init__(self, suit, order):
        self.suit = suit
        self.order = order

    def __str__(self):
        return f'{self.order} of {self.suit} {UNI[self.suit]}'


class DeckofCards:
    """Creates a deck of class with methods to shuffle, deal, """

    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for order in ORDERS:
                self.deck.append(Card(suit, order))  # class Card class to create a card object in the Deck

    def shuffle(self):
        """Randomly reshuffles deck"""
        random.shuffle(self.deck)

    def deal(self):
        """pops a card from the back the Stack"""
        deal_card = self.deck.pop()
        return deal_card

    def __str__(self):
        dck = ''
        for crd in self.deck:
            dck += '\n' + crd.__str__()
        return f'Available Cards in deck: {dck}'

    def __len__(self):
        return len(self.deck)


class Hand:
    """Handles the cards held by each player, and value for aces """

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_cards(self, card):
        if card.order == 'Ace':
            self.aces += 1
        self.value += VALUES[card.order]
        self.cards.append(card)

    def adjust_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# Repetitive Functions
def display_player(player):
    """display players cards"""
    
    print("\nThe Player's cards are: ")
    print(*player.cards, sep='\n')
    print('Total = ', player.value, '\n')


def display_dealer(dealer, hidden=True):
    """displays dealers card, with the hidden function enabled"""
    
    if hidden:
        print("\nThe Dealer's cards are: ")
        print(dealer.cards[0])
        print('<Hidden Card>\n')
    else:
        print("\nThe Dealer's cards are: ")
        print(*dealer.cards, sep='\n')
        print('Total = ', dealer.value, '\n')


def ask_bet():
    """asks for bet, keeps asking until and integer is inputed"""
    
    while True:
        try:
            bet = int(input('Stake Chips: '))
        except ValueError:
            print('An error occurred! Please try again!')
            continue
        else:
            break
    return bet


def blackjack_c(hand):
    """checks if a hand is blackjack"""
    
    if hand.value == 21:
        print('BLACKJACK')


def clear_cache(player, dealer):
    """Clear player's and dealer's card from previous game """
    
    del player.cards[:]
    del dealer.cards[:]
    dealer.value = 0
    player.value = 0


def replay():
    """ask if player wants to replay"""
    
    return input('\nDo you want to replay BLACKJACK [Y/N]: ').lower().startswith('y')


# Game Play
def main():
    """main gameplay"""
    
    print('Welcome to Black Jack !!!')
    val = ''
    while val not in ['y', 'n']:
        val = input('\nAre you ready to play and have fun [Y/N]: ').lower()
    start = val.startswith('y')
    player1 = Hand()
    dealer = Hand()
    chips = 100

    while start:
        # create deck and shuffle
        game_deck = DeckofCards()
        game_deck.shuffle()

        # optional
        if chips <= 0:
            print('\nOut of Chips to stake. Thank you for playing')
            break

        print(f'Available Chips: {chips}')
        bet = ask_bet()
        while bet > chips:
            print('\nOverdraft not permissible, please renter Chips')
            bet = ask_bet

        sleep(2)
        print('\nShuffling deck....\n')
        sleep(2)
        # clear class object, i.e cards and cards total for a new round.
        clear_cache(player1, dealer)

        # deal first set of cards
        dealer.add_cards(game_deck.deal())
        dealer.add_cards(game_deck.deal())
        dealer.adjust_ace()
        player1.add_cards(game_deck.deal())
        player1.add_cards(game_deck.deal())
        player1.adjust_ace()

        # Display cards
        display_player(player1)
        display_dealer(dealer)

        # Ask if player wants to Hit or stand
        temp = ''
        while temp not in ['y', 'n'] and player1.value < 21:
            temp = input('\nWould you like to Hit? [Y/N]: ').lower()
        temp = temp.startswith('y')

        while temp and player1.value < 21:
            player1.add_cards(game_deck.deal())
            player1.adjust_ace()
            display_player(player1)

            # check to break if player greater than 21 after hitting
            if player1.value > 21:
                break
            temp = input('\nWould you like to Hit again? [Y/N]: ').lower().startswith('y')

        display_dealer(dealer, hidden=False)

        # End Game and ask player to replay
        if player1.value > 21:
            display_dealer(dealer, hidden=False)
            print('BUST!!!!!!\n')
            print('Dealer has won, better luck next time!!!')
            chips -= bet
            if replay():
                continue
            else:
                print('\n\nwe will miss you, see you soon')
                break

                # Other scenario where dealer keeps hitting until it gets to 17 and above
        while dealer.value < 17:
            dealer.add_cards(game_deck.deal())
            dealer.adjust_ace()
            display_dealer(dealer, hidden=False)

        if dealer.value < player1.value:
            blackjack_c(player1)
            print('Player has won, give it up for the Ace Master!!!')
            chips += bet

        elif dealer.value > player1.value:
            blackjack_c(dealer)
            print('Dealer has won, better luck next time!!!')
            chips -= bet
        else:
            print('Better luck next time folks. It was a draw!!!')

        if replay():
            continue
        else:
            print('\n\nwe will miss you, see you soon')
            break

    print('\nThanks and Bye....')


if __name__ == '__main__':
    main()

# main()
