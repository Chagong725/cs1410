'''The main function frames the game, and each class acts as a feature of inheritance'''
import os
import random
import time

class Card:
    '''This sets the values and suits'''
    def __init__(self):
        self.values = ['2','3', '4', '5', '6', '7', '8', '9', '10', 'A', 'K', 'Q', 'J'] 
        self.suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']


class Deck:
    '''Arrange and mix cards according to shape and order'''
    def __init__(self):
        self.deck = []
        card = Card()
        for i in card.suits:
            for j in card.values:
                self.deck.append([(j, i)])
        random.shuffle(self.deck)


class Hand:
    '''Controls all movements in the hand. Divide the criteria between hit and stand to determine the option of ace'''
    def __init__(self):
        self.score = 0
        self.aces = 0
        self.hand = []

    def draw_hand(self, deck):
        '''Take the player's card from the deck'''
        for i in range(2):
            newcard = deck.deck[0]
            self.hand.append(deck.deck[0])
            self.calculatescore(newcard)
            deck.deck.pop(0)

    def hit(self, deck):
        '''If player enter Hit, hand out the card.'''
        newcard = deck.deck[0]
        self.hand.append(newcard)
        self.calculatescore(newcard)
        deck.deck.pop(0)

    def calculatescore(self, data):
        '''Calculate the score'''
        newcard = data[0]
        if newcard[0] in ['1', '2', '3', '4', '5','6','7', '8', '9', '10']:
            self.score+= int(newcard[0])
        elif newcard[0] in ['K', 'Q', 'J']:
            self.score+= 10
        elif newcard[0] == 'A':
            self.score += 11
            self.aces += 1
    
    def checkaces(self):
        '''Define the values of Ace'''
        while self.score > 21:
            if self.aces > 0:
                self.score -= 10
                self.aces -= 1
                print('Ace value changed from 11 to 1')
            else:
                break
    def __str__(self, card):
        '''Draw of a card with the ascii'''
        newcard = card[0]
        number = newcard[0]
        suit = newcard[1]

        if suit == 'Clubs':
            suit = '\u2667'
        elif suit == 'Hearts':
            suit = '\u2661'
        elif suit == 'Spades':
            suit = '\u2664'
        else:
            suit = '\u2662'
        return f'''\
        .-------.
        |{number}      |
        |       |
        |   {suit}   |
        |       |
        |      {number}|
        `-------´
        '''.split('\n')

    def display_hand(self):
        '''Draw pictures side by side'''
        cards = [self.__str__(card) for card in self.hand]
        for lines in zip(*cards):
            print(' '.join(lines))
                        
class Player(Hand):
    '''Inherit the hand class to indicate the player's score and card'''
    def __init__(self):
        super().__init__()
    
    def __str__(self, card):
        '''Draw of a card with the ascii'''
        newcard = card[0]
        number = newcard[0]
        suit = newcard[1]

        if suit == 'Clubs':
            suit = '\u2667'
        elif suit == 'Hearts':
            suit = '\u2661'
        elif suit == 'Spades':
            suit = '\u2664'
        else:
            suit = '\u2662'
        return f'''\
        .-------.
        |{number}      |
        |       |
        |   {suit}   |
        |       |
        |      {number}|
        `-------´
        '''.split('\n')

    def display_hand(self):
        '''Draw pictures side by side'''
        cards = [self.__str__(card) for card in self.hand]
        for lines in zip(*cards):
            print(' '.join(lines))

class Dealer(Hand):
    '''Inherit the hand class to indicate the dealer's score and card'''
    def __init__(self):
        super().__init__()
        self.card2 = f'''\
        .-------.
        |?      |
        |       |
        |       |
        |       |
        |      ?|
        `-------´
        '''.split('\n')
        
    def createonecard(self):
        '''Draw one card from the deck'''
        data = self.hand[0]
        card1 = data[0]
        number = card1[0]
        suit = card1[1]

        if suit == 'Clubs':
            suit = '\u2667'
        elif suit == 'Hearts':
            suit = '\u2661'
        elif suit == 'Spades':
            suit = '\u2664'
        else:
            suit = '\u2662'
        return f'''\
        .-------.
        |{number}      |
        |       |
        |   {suit}   |
        |       |
        |      {number}|
        `-------´
        '''.split('\n')

        
    def showdealercards(self):
        '''Show dealer's card on the terminal'''
        card1 = self.createonecard()
        spacing = ' ' * 5
        for pieces in zip(card1, self.card2):
            print(spacing.join(pieces))

class Game():
    '''Make the main function and play the game'''
    def __init__(self,temp):
        self.temp= temp

    def main():
        deck = Deck()
        dealerphase = False

        while True:
            hitphase = True
            playerhand = Player()
            dealerhand = Dealer()
            playerhand.draw_hand(deck)
            dealerhand.draw_hand(deck)
            print('PLAYER CARDS: ')
            playerhand.display_hand()
            print('PLAYER SCORE =  ', playerhand.score)
            print('                                                    ')
            print("Dealer's CARD: ")
            dealerhand.showdealercards()
            print('DEALER SCORE =  ?')

            while hitphase == True:
                user = input('Stand or Hit :  ').lower()
                if user == 'hit':
                    clear()
                    playerhand.hit(deck)
                    playerhand.display_hand()
                    print('PLAYER SCORE =  ', playerhand.score)
                elif user == 'stand':
                    hitphase = False
                else:
                    print('Invalid input')

                playerhand.checkaces()
                
                if playerhand.score == 21:
                    print('You win!')
                    hitphase = False
                    time.sleep(1)
                elif playerhand.score > 21:
                    print('Bust!  You lose!')
                    hitphase = False
                    time.sleep(1)
                else:
                    dealerphase = True

            while dealerphase == True:
                clear()
                time.sleep(1)
                print('DEALER CARDS')
                dealerhand.display_hand()
                print('PLAYER CARDS: ')
                playerhand.display_hand()
                time.sleep(5)

                while dealerhand.score < 17:
                    dealerhand.hit(deck)
                    clear()
                    print("Dealer hits")
                    dealerhand.display_hand()
                    print('Dealer scores: ', dealerhand.score)
                    time.sleep(2)

                dealerhand.checkaces()
                clear()
                time.sleep(1)
                dealerhand.display_hand()
                print('-------------------------------------------------------')
                playerhand.display_hand()
                print('Player scores: ', playerhand.score)
                print('Dealer scores: ', dealerhand.score)
                time.sleep(5)

                if dealerhand.score > 21:
                    print('DEALER BUSTED!!! YOU WIN!!!')
                    dealerphase = False
                    break
                
                if dealerhand.score == 21:
                    print('Dealer wins!')
                    dealerphase = False

                elif dealerhand.score > playerhand.score:
                    print('Dealer wins')
                    dealerphase = False
                
                elif dealerhand.score < playerhand.score:
                    print('Player wins!')
                    dealerphase = False

                elif dealerhand.score == playerhand.score:
                    print("It's a tie!")
                    dealerphase = False

            time.sleep(5)
            clear()
        
def clear():
   """Clear the console."""
   # for windows
   if os.name == 'pos':
      _ = os.system('cls')
   # for mac and linux, where os.name is 'posix'
   else:
      _ = os.system('clear')


if __name__ == "__main__":
    Game.main()