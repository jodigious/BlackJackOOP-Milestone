'''
Blackjack Object Oriented Programing
Milestone Project 2
'''

import random

# global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
playing = True

# Creates a class for cards
class Card:

    def __init__(self, suit, rank): # the __init__ for Cards
        self.suit = suit            # maps the passed parameter to the attribute
        self.rank = rank            # maps the passed parameter to the attribute

    def __str__(self):                          # sets the ability to print() what we want
        return f"{self.rank} of {self.suit}"    # defines the print() output

# Create a class for deck
class Deck:

    def __init__(self):                                 # the __init__ for Deck
        self.deck = []                                  # start with an empty list
        for suit in suits:                              # loops through the suits...
            for rank in ranks:                          # loops through the ranks...
                self.deck.append(Card(suit, rank))      # and adds the card objects to the deck

    def __str__(self):                              # sets the print() method
        deck_comp = ''                              # start with an empty string
        for card in self.deck:                      # loops through the cards in deck
            deck_comp += '\n ' + card.__str__()     # add each Card object's print string,
                                                        # calling card's print() method
        return 'The deck has:' + deck_comp          # outputs both a statement and the card suit + rank

    def shuffle(self):              # the shuffle deck method
        random.shuffle(self.deck)   # uses random libray's shuffle

    def deal(self):                     # card dealing method
        single_card = self.deck.pop()   # pops a card object off the deck object
        return single_card              # returns the card object

# Creates a hand class to calculate the value of the hand
class Hand:

    def __init__(self):     # __init__ for hand
        self.cards = []     # start with an empty list as we did in the Deck class
        self.value = 0      # start with zero value
        self.aces = 0       # add an attribute to keep track of aces

    def add_card(self, card):               # method for adding cards to the hand
        self.cards.append(card)             # adds the passed card object to the hand list (which starts empty)
        self.value += values[card.rank]     # increments the value of the hand by the value
                                                # associated with the card rank... does this by looking up the
                                                # card value (as a value) against the rank (as a key).
        if card.rank == 'Ace':              # checks to see if the rank is an "Ace" (which can be 1 or 11)
            self.aces += 1                  # add to self.aces

    def adjust_for_ace(self):                   # method for handling whether an Ace is a 1 or an 11
        while self.value > 21 and self.aces:    # as long as the hand had aces and is valued at > 21,
            self.value -= 10                        # it will decrement the value by 10
            self.aces -= 1                          # and set the aces in the hand = 1.

class Chips:

    def __init__(self, total=100):      # __init__ for chips, setting the default value to 100
        self.total = total              # maps the parameter to the attribute
        self.bet = 0                    # sets a default value to a bet

    def win_bet(self):              # methods for adding chips if you win
        self.total += self.bet      # increments your chip total by the bet amount

    def lose_bet(self):             # method for subtracting chips if you lose
        self.total -= self.bet      # decrements your chip total by the bet amount

###
### Start functions of gameplay here. ###
###

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed", chips.total)
            else:
                break
