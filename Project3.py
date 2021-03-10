# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 08:11:01 2021

@author: craig
"""

import random
import time

#Create deck of cards
class Cards:
    def __init__(self):
        self.deck = []
        self.comphand = []
        self.compsets = []
        self.userhand = []
        self.usersets = []
        
        
        for x in range(2,15):
            for y in range(1,5):
                if x == 11:
                    self.deck.append('J')
                elif x == 12:
                    self.deck.append('Q')
                elif x == 13:
                    self.deck.append('K')
                elif x == 14:
                    self.deck.append('A')
                else:
                    self.deck.append(x)
                    
        for x in range (0,7):
            card = random.choice(self.deck)
            self.comphand.append(card)
            self.deck.remove(card)
            
        for x in range(0,7):
            card = random.choice(self.deck)
            self.userhand.append(card)
            self.deck.remove(card)
            
    def remove(self, turn, card):
        if turn == 'user':
            self.userhand.remove(card)
        else:
            self.comphand.remove(card)
            
    def append(self, turn, card):
        if turn == 'user':
            self.userhand.append(card)
        else:
            self.comphand.append(card)
            
    def printHand(self):
        user_str = " "
        for x in range(2,15):
            if x == 11:
                curr = 'J'
            elif x == 12:
                curr = 'Q'
            elif x == 13:
                curr = 'K'
            elif x == 14:
                curr = 'A'
            else:
                curr = str(x)
                
            if x < 11:
                count = self.userhand.count(x)
                
            else:
                count = self.userhand.count(curr)
                
            while count > 0:
                user_str = user_str + curr + ", "
                count = count - 1
                
        sets_str = str(self.usersets).strip('[]')
        print(user + " Hand: " + user_str.replace("'", ""))
        print(user + " Sets: " + sets_str.replace("'", ""))
    
    def drawCard(self, player):
        card = random.choice(self.deck)
        self.deck.remove(card)
        if player == "comp":
            self.comphand.append(card)
            
        else:
            self.userhand.append(card)
            
    def checkForSet(self, player):
        if player == "user":
            for c in self.userhand:
                num = self.userhand.count(c)
                if num == 4:
                    for x in range(0,4):
                        self.userhand.remove(c)
                    self.usersets.append(c)
                    
        else:
            for c in self.comphand:
                num = self.comphand.count(c)
                if num == 4:
                    for x in range(0,4):
                        self.comphand.remove(c)
                    self.compsets.append(c)
                    
    def printComp(self):
        comp_str = str(self.compsets).strip('[]')
        print("My Sets: " + comp_str.replace("'", ""))
        
#####################################################################
user = input('Please enter the name of the player: ')
help = ("""1. 52 card deck of cards
2. At least 2 players
3. 5 to 7 cards per player
4. A table to play on
5. Someone who can shuffle cards
5. Instructions and rules


The instructions to start out with in the game of Go Fish each player is dealt five to seven cards from a well shuffled deck with the dealer dealing the cards from left to right or clockwise.

Seven cards are dealt when there are four players or less or five if there are five players or more.

The cards that are left after each player is dealt their cards are put in a pile face down that are drawn from during the game which is called the pool or ocean which the rules allow for players draw from.

The players take turns from left to right, or clockwise with the objective being to get four cards matching the same rank which are called books.

The rules allow for each player to make a book by asking other players for the cards they need in order to make books, or obtain the cards they need to make books by drawing from the pool or ocean.

Instructions state that each player MUST have at least one card of the rank type they are asking the other player for. If they do not have at least one card of the same rank, the rules state that they cannot ask for it.

If a player asks another for a rank and the player being asked does not have any cards of the rank they are asking for, they reply "Go Fish" at which point the person asking must draw a card from the pool or ocean and the next person is instructed to take his or her turn.

If the player being asked does however have a card or cards of the same rank they are being asked for, they must hand over ALL of the cards of that rank they are holding. If they refuse to hand it over, they are in violation of breaking the rules of the game.

In an example of a turn, a player might ask: "Do you have any sevens?" at which point the player being asked must hand over any sevens in his possession regardless of what suit it is.

If the player however does not have any sevens, he or she would reply "Go Fish" and the player asking would draw a card from the pool or ocean and his turn would be over.

Then, the player on the left of him or her would be free to take their turn and so on and so forth until there are no cards left in the ocean or pool.

If the player runs out of cards before the pool or ocean is empty, the player must draw five new cards from the pool or ocean and continue playing.

Winning in the Go Fish card game happens when there is no cards left in the ocean, or pool. The winner is the player who has made the most books, or sets of four cards with the same rank.""")



deck = Cards()
turn = "user"
faceCards = ['K', 'Q', 'J', 'A']
regCards = [2, 3, 4, 5, 6, 7, 8, 9, 10]
numStrings = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
faceStrings = ['King', 'Queen', 'Jack', 'Ace']
faceCard = 0

def processInput(user_input):
    cardType = -1
    try:
        if ' ' in user_input:
            cardType = -2
        elif user_input.upper() in (card.upper() for card in faceCards):
            cardType = 1
        elif user_input.upper() in (card.upper() for card in faceStrings):
            cardType = 1
        elif user_input.upper() in (card.upper() for card in numStrings):
            cardType = 0
        elif int(user_input) in regCards:
            cardType = 0
        return cardType
    except ValueError:
        cardType = -2;
        return cardType;
    
def userHelp(user_input):
    if ' ' in user_input:
        user_input == '--help'
        return(help)
       

def adjustCard(cardType, user_input):
    if cardType == 0:
        if user_input.upper() in (card.upper() for card in numStrings):
            return int(regCards[numStrings.index(user_input)])
        else:
            return int(user_input)
    else:
        return user_input[0].upper()
    
def guessWrong(turn):
    deck.drawCard(turn)
    deck.checkForSet(turn)
    
    if turn == 'user':
        print("Go Fish")
        
    else:
        print("Gone Fishing, Your Turn")
        
    time.sleep(1)
    
def guessRight(turn, card, count, cardType):
    if cardType == 0:
        index = regCards.index(card)
        cardString = numStrings[index]
        
    else:
        index = faceCards.index(card)
        cardString = faceStrings[index]
        
    if count > 1:
         cardString = cardString + "s"
         
    if turn == 'user':
        print("I had " + str(count) + " " + cardString)
        print("You get to go again")
        
    else:
        print("Thanks for the " + cardString)
        
    updateHand(count, card, turn)
    
def updateHand(count, card, turn):
    if turn == 'user':
        opp = 'comp'
    else:
        opp = 'user'
    while count > 0:
        deck.remove(opp, card)
        deck.append(turn, card)
        count = count - 1
        
    deck.checkForSet(turn)
    time.sleep(1)
    
while len(deck.userhand) > 0 and len(deck.comphand) > 0 and len(deck.deck) > 0:
    if turn == 'user':
        print("\n")
        deck.printHand()
        
        user_input = input("Please request a card from me: ")
        cardType = processInput(user_input)
        
        if cardType == -1:
            print("Please provide a valid selection")
            
        elif cardType == -2:
            print("Please provide a valid selection")
        else:
            card = adjustCard(cardType, user_input)
            count = deck.comphand.count(card)
            if count == 0:
                guessWrong(turn)
                turn = "comp"
            else:
                guessRight(turn, card, count, cardType)
                turn = 'user'
    if turn == 'comp':
        print("\n")
        card = random.choice(deck.comphand)
        cardType = processInput(str(card))
        print("Do you have any " + str(card) + "s")
        count = deck.userhand.count(card)
        time.sleep(1)
        
        if count ==0:
            guessWrong(turn)
            turn = 'user'
        else:
            guessRight(turn, card, count, cardType)
            turn = 'comp'
            
    if user_input == '--help':
        while True:
            print(help)
            z = input("Type '--resume' to resume: ")
            if z == '--resume':
                repeatNeeded = True
                break
        
            
print("\n")
print("Out of card, game over")
numCompSets = len(deck.compsets)
numUserSets = len(deck.usersets)

print("You made " + str(numUserSets) + " sets")
print("I made " + str(numCompSets) + " sets")

#determine winner based on number of sets
if numCompSets > numUserSets:
	print("Computer Wins")
elif numUserSets > numCompSets:
	print(user + " Wins")
else:
	print("We Tied")
        
        
        
        
        
        
        
            
            
