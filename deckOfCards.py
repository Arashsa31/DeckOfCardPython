#prints a tuple of cards in a deck that is randomized

import random

#initialize and randomize the deck
def initialize_deck():
    initialDeck = []
    for i in range(4):
        for j in range(13):
            if   i == 0:
                initialDeck += [(j+1,'Hearts')]
            elif i == 1:
                initialDeck += [(j+1,'Diamonds')]
            elif i == 2:
                initialDeck += [(j+1,'Clubs')]
            elif i == 3:
                initialDeck += [(j+1,'Spades')]
    #random.shuffle(initialDeck)
    return initialDeck  

#convers deck numbers to text
def numberToText(number):
    if number == 1:
        return 'Ace'
    elif number == 2:
        return 'Two'   
    elif number == 3:
        return 'Three' 
    elif number == 4:
        return 'Four'   
    elif number == 5:
        return 'Five'   
    elif number == 6:
        return 'Six'   
    elif number == 7:
        return 'Seven'   
    elif number == 8:
        return 'Eight'   
    elif number == 9:
        return 'Nine'   
    elif number == 10:
        return 'Ten'   
    elif number == 11:
        return 'Jack'   
    elif number == 12:
        return 'Queen'   
    elif number == 13:
        return 'King'  

#calls on the initialize function and stores in theDeck
theDeck = initialize_deck()

#prints the deck into four columns
columnCounter = 0
for number, suit in theDeck:
    if columnCounter < 3:
        print(f'{numberToText(number)} of {suit}', end='    \t')
        columnCounter += 1
    else:
        print(f'{numberToText(number)} of {suit}', end='    \n')
        columnCounter = 0

print('------------------------------------------------------------------------------------------------')

#randomize theDeck
random.shuffle(theDeck)

#prints the new randomized deck into four columns
columnCounter = 0
for number, suit in theDeck:
    if columnCounter < 3:
        print(f'{numberToText(number)} of {suit}', end='    \t')
        columnCounter += 1
    else:
        print(f'{numberToText(number)} of {suit}', end='    \n')
        columnCounter = 0