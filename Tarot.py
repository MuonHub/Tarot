# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:34:19 2019


Images from 1910 version by: Arthur Edward Waite. Pamela Coleman Smith was the artist 
and worked as an artist 'for hire.' Waite was the copyright holder and he died in 1942. 

Instructions: Run the following in python...

from Tarot import *
my_deck = Tarot()

Notes:
    
    It helps to have a lightweight image viewer for this version as it will open a new window for each image.
    

@author: Steve
"""
from PIL import Image
import random # Library to create random numbers
import json

class Tarot:
    '''
    Creates a new instance of a deck of Rider-Waite (1910) Tarot cards.
    Returns a dictionary containing the deck and it attributes.
    
    '''
        
    def __init__(self, deck_name = "Rider Waite", game = 'Celtic Cross'):
#        Default deck attributes
        self.deck_name = deck_name
        self.game = game
        
#        Initialize a dictionary that will store the cards.
        self.deck = {}
        


#        Create the deck specified by the deck name.
        if self.deck_name == 'Rider Waite':
            self._rider_waite()
#        If deck not found notify user and list available decks.
        else:
            print('Deck not found! Enter a valid deck name.')
            print('Tarot Decks Available:')
            print('Rider Waite')

#        Create a list representing the order that the cards are in. It is the length of the deck chosen.
        self.card_order = list(range(len(self.deck)))

#        Choose what game to play!
        if self.game == 'Celtic Cross':
            self._celtic_cross()
        else:
            print('Game not found! Please enter a valid game name.')
            print('Games available for Class Tarot:')
            print('Celtic Cross')


    def _rider_waite(self):
        '''
        Creates a deck of classic 1910 era Rider-Waite cards.
        
        '''
        print(self.deck_name)
        
#        Show the cover card.
        self.back = '.\images\Original_1910_Back.jpg'
        image = Image.open(self.back)
        image.show()
        image.close()

#        The JSON file must already exist. Use the utility .\utils\createRiderWaiteJSONFile.py         
        file_object = open('./data/riderwaite.json', 'r')
        json_object = json.load(file_object)
        
#        The keys of the dictionary need to be converted to integers
        for i in range(len(json_object)):
            key= str(i)
            self.deck[i] = json_object[key]
#        All of the 'top_up' attributes must also be an integer for the boolean conversion to work.
        for i in range(len(self.deck)): self.deck[i]['top_up'] = 1
                    
            
    def _shuffle_cut(self):
        ''' This little program simulates shuffling the deck and then cutting the deck.
        In addition the cards up or down orientation is randomized for each card.
        '''

        random.seed() # Start up the random number generator with the system time
        random.shuffle(self.card_order)
#        print(self.card_order) # Test to see what the card order is.
        for item in self.card_order:
            self.deck[item]['top_up'] = random.randint(0, 1)

#        Select a 'cut' card. The cut card can also be called the bottom card
#        in that it is at the bottome of the top pile and therefor will be at
#        the bottom of the deck once the cut has been made. 
        cut_card = random.randint(0, len(self.card_order))
        place = self.card_order.index(cut_card)
        top_pile = self.card_order[:place + 1]
#        print(top_pile)
        bottom_pile = self.card_order[place + 1:]
#        print(bottom_pile)
        self.card_order =  bottom_pile + top_pile
#        print(self.card_order)
#
    def _celtic_cross(self):
        '''Classic Rider-Waite Celtic Cross Tarot devination'''
        print(self.game)
#       Create a list of the card order meaning in celtic cross.
        celtic_cross = open("./data/celtic_cross.txt", 'r')
        place_order_meaning = list()
        for line in celtic_cross:
            line = line.rstrip('\n')
            line.strip('\r')
            place_order_meaning.append(line)
        celtic_cross.close()

#Step 1) Select the 'Significator' card
        print('Please choose a topic from the following list which generally best describes the nature of your question.')
        print()
        print('Meditate on the topic and how it relates to your question, then...')
        print()
        print('Enter the number of the topic below.')
        # Ordered by: rank, card_name, suit, symbol, person, description, meaning, reverse meaning
        
#        Print a list if options to chose for the Significator card and its possible meanings.
        for card in range(0, 10):
            print(' ' + str(card) + ': ' + self.deck[card]['symbol'])
        for card in range(10, 22):
            print(str(card) + ': ' + self.deck[card]['symbol'])
#        User input to determine the significator card.
        significator = int(input('Enter the number:'))
        #print(self.card_order)


#Step 2) Pull the Significator card from the full deck before shuffling and cutting the deck three times.
        self.card_order.remove(significator)
            
#Step 3) Shuffle and Cut the deck three times        
        for times in range(0,3): 
                self._shuffle_cut()
#Step 4) Put the order of the top 9 cards in a list.
        dealt_cards = self.card_order[:10]
        
#Step 5) Place the significator card at the beginning of the chosen cards (top of the pile). 
        dealt_cards.insert(0, significator)
#        print(deal_cards) # Test to see if significator was inserted correctly at the beginning.
  
#Show each of the cards chosen starting with the Significator card in the middle
        k=0
        for card in dealt_cards:
            
        # Ordered by: rank, card_name, suit, symbol, person, description, meaning, reverse meaning
            
            image = Image.open(self.deck[card]['face_pic'])
            
            if self.deck[card]['top_up'] == False and k != 0: # The significator card is never reversed in meaning i.e. k!=0.
                image = image.rotate(180)
            image.show()
            
            print('\n' * 10)
            print('~' * 25)
            print(self.deck[card]['card_name'])
            print()
            print(place_order_meaning[k])
            print()
            print('It could also represent a...')
            print(self.deck[card]['person'])
            print()
            print('Card Description...')
            print(self.deck[card]['description'])
            print()
            print('Card Meaning...')
            if self.deck[card]['top_up'] == False and k != 0:
                print(self.deck[card]['reverse'])        
            else:
                print(self.deck[card]['meaning'])
            
            k+=1                 
            
            cont = input('To continue select Enter:')
            if cont == "k":
                image.close()
                return()
            image.close()
        
        
#End of Tarot
            


#my_deck = Tarot()




























