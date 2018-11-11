# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
condition1 = 'Hit or Stand?'
condition2 = 'Deal again?'


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.suit

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
      
# define hand class
class Hand:
    def __init__(self):
        self.card_list = [] 

    def __str__(self):
        string = ''
        for i in self.card_list:
            string += (i + ' ')
        return string

    def add_card(self, card):
        self.card_list.append(str(card))

    def get_value(self):
        true_value = 0
        A_present = False
        for ch in self.card_list:
            true_value += VALUES[ch[1]]
            if ch[1] == 'A':
                A_present = True
        if A_present == True and true_value <= 11:
            return true_value + 10
        else:
            return true_value
            
    def draw(self, canvas, pos):
        possy = [100, pos]
        for ch in self.card_list:
            drawy = Card(ch[0], ch[1])
            drawy.draw(canvas, possy)
            possy[0] += 100

       
# define deck class 
class Deck:
    def __init__(self):
        self.main_deck = []
        for ch in SUITS:
            for i in RANKS:
                self.main_deck.append(ch + i)

    def shuffle(self):
        random.shuffle(self.main_deck)

    def deal_card(self):
        return str(self.main_deck.pop(0))
    
    def __str__(self):
        string = ''
        for i in self.main_deck:
            string += (i + ' ')
        return string

    
    
#define event handlers for buttons
def deal():
    global outcome, in_play, complete_deck, player_hand, dealer_hand, condition1, score
    
    condition1 = 'Hit or Stand?'
    complete_deck = Deck()
    complete_deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(complete_deck.deal_card())
    player_hand.add_card(complete_deck.deal_card())
    dealer_hand.add_card(complete_deck.deal_card())
    dealer_hand.add_card(complete_deck.deal_card())
    if in_play == True:
        score -= 1
    in_play = True

def hit():
    global condition1, in_play, score
    if in_play == True:
        player_hand.add_card(complete_deck.deal_card())
        if player_hand.get_value() > 21:
                condition1 = 'You are BUSTED!'
                in_play = False
                score -= 1 
  
def stand():
    global condition1, condition2, in_play, score
    
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(complete_deck.deal_card())
    if in_play == True: 
        if dealer_hand.get_value() <= 21:
            if dealer_hand.get_value() >= player_hand.get_value():
                condition1 = 'Dealer wins.'
                score -= 1
            else:
                condition1 = 'Player wins.'
                score += 1
        else:
            condition1 = 'Dealer busted'
            score += 1
    in_play = False
    

    
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Dealer's hand", [100, 80], 40, "Black")
    dealer_hand.draw(canvas, 100)
    canvas.draw_text("Player's hand", [100, 380], 40, "black")
    player_hand.draw(canvas, 400)
    if in_play == True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [236, 148], CARD_BACK_SIZE)
    else:
        canvas.draw_text(condition2, [340,80], 35, "blue")
    canvas.draw_text(condition1, [340, 380], 35, "blue")
    canvas.draw_text("BlackJack", [50, 310], 100, "black")
    canvas.draw_text("Score:", [400, 550], 40, "red")
    canvas.draw_text(str(score), [525, 552], 40, "red")

    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("orange")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric