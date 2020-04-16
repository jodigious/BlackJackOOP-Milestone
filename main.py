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

# function placing a bet
def take_bet(chips):
    while True:                                                                 # setup loop to prompt for input
        try:                                                                    # try block
            chips.bet = int(input('How many chips would you like to bet? '))    # inputs from player an amount to bet
        except ValueError:                                                      # error if the type isn't an int
            print('Sorry, a bet must be an integer!')                           # error string
        else:                                                                   # set up additional exception
            if chips.bet > chips.total:                                             # for if you bet too much.
                print("Sorry, your bet can't exceed", chips.total)              # string for too large a bet
            else:                                                               # exception to above
                break                                                           # break from while

# function to hit
def hit(deck, hand):

    hand.add_card(deck.deal())      # gets dealt a card object from the deck object
    hand.adjust_for_ace()           # adjusts the ace(s) value(s) based off the hand value

# function to either hit or stand
def hit_or_stand(deck, hand):

    global playing  # to control an upcoming while loop

    while True:                                                                     # starts loop prompting player
        decision = input("Would you like to Hit or Stand? Enter 'h' or 's' ")       # gets decision from player

        if decision[0].lower() == 'h':  # if decision is 'h' for hit
            hit(deck, hand)             # hit() function defined above

        elif decision[0].lower() == 's':                    # if decision is 's' for stand
            print("Player stands. Dealer is playing.")      # update the dealer of you decision
            playing = False                                 # and player is no longer player

        else:                                       # if you don't hit or stand
            print("Sorry, please try again.")       # you will be prompted to try again
            continue                                # continue playing
        break                                       # exit while loop


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")

###
### and now on to the game! ###
###

print("\n\n Get ready to play some fuckin blackjack! \n\n")

while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()  # remember the default value is 100

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

            # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

            # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)

            # Inform Player of their chips total
    print("\nPlayer's winnings stand at", player_chips.total)

    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break

