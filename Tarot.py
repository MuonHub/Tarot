# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:34:19 2019


Images from 1910 version by: Arthur Edward Waite. Pamela Coleman Smith was the artist 
and worked as an artist 'for hire.' Waite was the copyright holder and he died in 1942. 

Notes:
    
    

@author: Steve Alley
"""
from PIL import Image
import matplotlib.pyplot as plt
import random # Library to create random numbers
import json

class Tarot:
    '''
    Creates a new instance of a deck of Rider-Waite (1910) Tarot cards.
    Returns a dictionary containing the deck and it attributes.
    
    '''
        
    def __init__(self, deck_name = "Rider-Waite", game = 'Celtic Cross'):
#        Default deck attributes
        self.deck_name = deck_name
        self.game = game
#        Initialize a dictionary that will store the cards.
        self.deck = {}

#        Create the deck specified by the deck name.
        if self.deck_name == 'Rider-Waite':
            self._rider_waite()
            if self.deck == {}:
                print("Can't find the Rider-Waite card set!")
                return
        else:
            print('Deck not found! Enter a valid deck name.')
            print('Tarot Decks Available:')
            print('Rider-Waite')
            return

#Create a list representing the order that the cards are in. It is the length of the deck chosen.
        self.card_order = list(range(len(self.deck)))

#Choose what game to play.
        if self.game == 'Celtic Cross':
            self._celtic_cross()
        else:
            print('Game not found! Please enter a valid game name.')
            print('Tarot games available are:')
            print('Celtic Cross')
            return

    def _rider_waite(self):
        '''
        Creates a deck of classic 1910 era Rider-Waite cards.
        
        '''
        print(self.deck_name)
        
#Load JSON file        
#        The JSON file must already exist. Use the utility .\utils\createRiderWaiteJSONFile.py         
        try:
            file_object = open('./data/riderwaite.json', 'r')
            self.deck = json.load(file_object)
        except:
            print('Rider-Waite JSON file may be missing or unavailable.')
            print('<./data/riderwaite.json>')
            self.deck = {}
            return
        else:
            pass
             
        file_object.close()
             
            
    def _shuffle_cut(self):
        ''' This program simulates shuffling and cutting the deck.
        In addition the cards' 'up' or 'down' orientation is randomized.
        '''

        random.seed() # Start up the random number generator with the system time
        random.shuffle(self.card_order)
#        print(self.card_order) # Test to see what the card order is.
        for item in self.card_order:
            
            self.deck[str(item)]['top_up'] = random.randint(0, 1)

#        Select a 'cut' card. The cut card can also be called the bottom card
#        in that it is at the bottome of the top pile and therefor will be at
#        the bottom of the deck once the cut has been made. 
        cut_card = random.randint(0, len(self.card_order))
        cut = self.card_order.index(cut_card)
        top_pile = self.card_order[:cut + 1]
#        print(top_pile)
        bottom_pile = self.card_order[cut + 1:]
#        print(bottom_pile)
        self.card_order =  bottom_pile + top_pile
#        print(self.card_order)

#Celtic Cross Game
    def _celtic_cross(self):
        '''Classic Rider-Waite Celtic Cross Tarot devination'''
        print(self.game)
#Load the celtic cross card placeholder meanings...
        try:
            file_object = open('./data/celtic_cross.json', 'r')
            cc_dict = json.load(file_object)
        except:
            print('Celtic Cross JSON file missing or unavailable.')
            print('<./data/celtic_cross.json>')
            cc_dict = {}
            return
        else:
            pass
    
#Step 1) Select the 'Significator' card
        print()
        print('Directions:')
        print('1) Choose the topic which best describes the nature of your inquiry.')
        print('2) Meditate on how the topic relates to your inquiry.')
        print('3) Enter the number for the selected topic below.')
        print()
   
        # Ordered by: rank, card_name, suit, symbol, person, description, meaning, reverse meaning
        
#        Print a list if options to chose for the Significator card and its possible meanings.
        for num in range(0, 10):
            card = str(num)
            print(' ' + card + ': ' + self.deck[card]['symbol'])
        for num in range(10, 22):
            card=str(num)
            print(card + ': ' + self.deck[card]['symbol'])

#User input to select the significator card. 
#Pull the Significator card from the deck before shuffling.
        try:
            significator = int(input('Enter Topic Number:'))
            self.card_order.remove(significator)
        except:
            print('The powers that be did not like that selection, please try again.')
            return
        else:
            pass
#Shuffle and Cut the deck three times        
        for times in range(3): 
                self._shuffle_cut()
                
#Place the significator card on top of the deck.
        self.card_order.insert(0, significator)
  
#Create a new figure to draw on. Adjust figsize and color accordingly.
        fig_cc = plt.figure(figsize=(8,16), facecolor='g')
#The placement order that the cards are placed on the table.
        placement = [6, 1, 3, 2, 5, 7, 10, 16, 12, 8, 4]
#Place the cards on the table...
        print(('~' * 25)+' Rider-Waite Tarot ~ Celtic Cross '+('~' * 25)+'\n')

        for k in range(0,11):
           
            kard = str(self.card_order[k])
            place = str(placement[k])
            
#Print out the meanings of the cards...            
            print(('~' * 4) + '~ The ' + cc_dict[place]['place_name'] + ' Card  '+('~'*4))
            print(cc_dict[place]['meaning'])
            print()
            print(self.deck[kard]['card_name'] +' ~ '+ self.deck[kard]['description']+' '+self.deck[kard]['person'])
            print()
            if self.deck[kard]['top_up'] == False and k != 0:
                print('Card Meaning ~ '+self.deck[kard]['reverse'])        
            else:
                print('Card Meaning ~ '+self.deck[kard]['meaning'])
            print()

        
#Draw the cards onto the table in the correct placement.
            axes_k = 'ax' + place
            axes_k =  fig_cc.add_subplot(4, 4, placement[k])
            axes_k.axis('off')
            
            image = Image.open(self.deck[kard]['face_pic'])            
        
            if self.deck[kard]['top_up'] == False and k != 5: 
                image = image.rotate(180)
                
            axes_k.set_title(cc_dict[place]['place_name'])

            plt.imshow(image)

#Cleanup any open files and images being used.            
        plt.show()        
        image.close()
        file_object.close()
        
#End of Tarot
            

if __name__=='__main__':
    my_deck = Tarot()




























