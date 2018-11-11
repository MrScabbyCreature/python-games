# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global card_length, lst, num, turns, first_choice, second_choice
    card_length = [50, 100]
    lst = [False] * 16
    num = range(8) * 2
    random.shuffle(num)
    turns = 0.0
    first_choice = -10
    second_choice = -10


def draw(canvas):
    canvas.draw_line((card_length[0], 0), (card_length[0], card_length[1]), 1, 'black')
    canvas.draw_line((card_length[0] * 2, 0), (card_length[0] * 2, card_length[1]), 1, 'black')
    canvas.draw_line((card_length[0] * 3, 0), (card_length[0] * 3, card_length[1]), 1, 'black')
    canvas.draw_line((card_length[0] * 4, 0), (card_length[0] * 4, card_length[1]), 1, 'black')
    canvas.draw_line((card_length[0] * 5, 0), (card_length[0] * 5, card_length[1]), 1, 'black')
    canvas.draw_line((card_length[0] * 6, 0), (card_length[0] * 6, card_length[1]), 1, 'black')
    canvas.draw_line((card_length[0] * 7, 0), (card_length[0] * 7, card_length[1]), 1, 'black')
    canvas.draw_line((card_length[0] * 8, 0), (card_length[0] * 8, card_length[1]), 1, 'black')
    canvas.draw_line((card_length[0] * 9, 0), (card_length[0] * 9, card_length[1]), 1, 'black')
    canvas.draw_line((card_length[0] * 10, 0), (card_length[0] * 10, card_length[1]), 1, 'black')
    canvas.draw_line((card_length[0] * 11, 0), (card_length[0] * 11, card_length[1]), 1, 'black')
    canvas.draw_line((card_length[0] * 12, 0), (card_length[0] * 12, card_length[1]), 1, 'black')
    canvas.draw_line((card_length[0] * 13, 0), (card_length[0] * 13, card_length[1]), 1, 'black')
    canvas.draw_line((card_length[0] * 14, 0), (card_length[0] * 14, card_length[1]), 1, 'black')
    canvas.draw_line((card_length[0] * 15, 0), (card_length[0] * 15, card_length[1]), 1, 'black')
    
    if lst[0] == True:
        canvas.draw_text(str(num[0]), (10, 75), 60, 'black')
    if lst[1] == True:
        canvas.draw_text(str(num[1]), (60, 75), 60, 'black')
    if lst[2] == True:
        canvas.draw_text(str(num[2]), (110, 75), 60, 'black')
    if lst[3] == True:
        canvas.draw_text(str(num[3]), (160, 75), 60, 'black')
    if lst[4] == True:
        canvas.draw_text(str(num[4]), (210, 75), 60, 'black')
    if lst[5] == True:
        canvas.draw_text(str(num[5]), (260, 75), 60, 'black')
    if lst[6] == True:
        canvas.draw_text(str(num[6]), (310, 75), 60, 'black')
    if lst[7] == True:
        canvas.draw_text(str(num[7]), (360, 75), 60, 'black')
    if lst[8] == True:
        canvas.draw_text(str(num[8]), (410, 75), 60, 'black')
    if lst[9] == True:
        canvas.draw_text(str(num[9]), (460, 75), 60, 'black')
    if lst[10] == True:
        canvas.draw_text(str(num[10]), (510, 75), 60, 'black')
    if lst[11] == True:
        canvas.draw_text(str(num[11]), (560, 75), 60, 'black')
    if lst[12] == True:
        canvas.draw_text(str(num[12]), (610, 75), 60, 'black')
    if lst[13] == True:
        canvas.draw_text(str(num[13]), (660, 75), 60, 'black')
    if lst[14] == True:
        canvas.draw_text(str(num[14]), (710, 75), 60, 'black')
    if lst[15] == True:
        canvas.draw_text(str(num[15]), (760, 75), 60, 'black')
        
def click(pos):
    global turns, helper_var, first_choice, second_choice
    x = int(pos[0]/50)
    
    if first_choice != -10 and second_choice != -10:
        if num[first_choice] != num[second_choice]:
            lst[first_choice] = False
            lst[second_choice] = False
        
        first_choice = -10
        second_choice = -10
        
    if lst[x] == False:
        lst[x] = True
        turns += 0.5
        if first_choice == -10:
            first_choice = x
        else:
            second_choice = x
            
    label.set_text('turns= ' + str(int(turns)))
    


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.set_canvas_background("lime")
frame.add_button("Reset", new_game)
label = frame.add_label("Turns")

# register event handlers
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
