# This is simple bluff program using python 
# Created by Akshay Bhat @zicron13

class Bluff:
    def __init__(self):
        self.deck = []
        self.player = ""
        self.comp = 'Computer'
        self.cards = []
        self.sign = []
        self.values = []
        self.sdeck = []
        self.hdeck = []
        self.ddeck = []
        self.cdeck = []
        self.player_deck =[]
        self.computer_deck = []
        self.num_cards = None




    def prepare(self):
        import random
        self.player = input('Enter your name')

        self.cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

        self.sign = ['S','H','D','C']
        self.sdeck = list(map(lambda cards: cards+'S',self.cards))
        self.hdeck = list(map(lambda cards: cards+'H',self.cards))
        self.ddeck = list(map(lambda cards: cards+'D',self.cards))
        self.cdeck = list(map(lambda cards: cards+'C',self.cards))
        self.deck = self.sdeck + self.hdeck + self.ddeck + self.cdeck
        return self.deck
    

    def distribute(self):
        import random
        self.deck1 = self.prepare()
        status = True
        while status:
            self.num_cards = int(input('Enter number of cards to play with from 5 to 10 cards allowed'))

            if (self.num_cards >=5 and self.num_cards <=10):
            
                random.shuffle(self.deck1)  # Shuffle the deck in place
                print("Deck after shuffling: ", self.deck1)
                self.player_deck=random.sample(self.deck1,self.num_cards)
                self.computer_deck = random.sample(self.deck1,self.num_cards)
                #print(self.player_deck,self.computer_deck)
                status =False
            else:
                print(f'You are not allowed to play with {self.num_cards} cards !!! ')
        return self.player_deck,self.computer_deck
              
         # Update self.deck with the shuffled deck

    
    def play(self):
        import random
        dist = self.distribute()  # Distribute cards to player and computer
        
        # Create dictionaries for player and computer
        player_card_dict = {card[:-1]: card[-1] for card in dist[0]}  # Player's hand
        computer_card_dict = {card[:-1]: card[-1] for card in dist[1]}  # Computer's hand
        
        print("Your cards:", player_card_dict)
        print("Computer cards:", computer_card_dict)  # For debugging, hide this later
        
      
        values_dict = {'J':11,'Q':12,'K':13,'A':1}
        player_keys = [k for k,v in player_card_dict.items()]
        computer_keys = [k for k,v in computer_card_dict.items()]
        # Map the list with values from values_dict if they exist, otherwise keep the original key
       # Use dict.get to simplify the mapping
        #mapped_player_keys = [values_dict.get(k, k) for k in player_keys]
        # Convert player_keys to integers if they are in the values_dict
        mapped_player_keys = [values_dict[k] if k in values_dict else k for k in player_keys]
       
        
        mapped_comp_keys = [values_dict[k] if k in values_dict else k for k in computer_keys]

        mapped_player_keys = [int(i) for i in mapped_player_keys]
        mapped_comp_keys = [int(i) for i in mapped_comp_keys]
        if sum(mapped_player_keys) > sum(mapped_comp_keys):
            print(f'Total sum is {sum(mapped_player_keys)}   {self.player} wins the game !!!')
        else:
            print(f'Total sum is {sum(mapped_comp_keys)}     {self.comp}  wins the game !!!') 
     

B = Bluff()
B.play()




