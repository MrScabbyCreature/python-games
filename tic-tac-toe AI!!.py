import simplegui
import random

height = 700
width = height
#level = 2
in_play = True
turn = 'p'
turn_control = {'p':'X', 'c':'O'}
main_list = [' ', ' ', ' ', 
             ' ', ' ', ' ', 
             ' ', ' ', ' ']

def computer_AI():
    global main_list, in_play
    temp_list = []
    if turn == 'c' and in_play == True:
        for i in range(9):
            temp_list = list(main_list)
            if temp_list[i] == ' ':
                temp_list[i] = turn_control['c']
                if win_check(temp_list, turn_control['c']) == True:
                    main_list[i] = turn_control['c']
                    in_play = False
                    break
    if turn == 'c' and in_play == True:
        for i in range(9):
            temp_list = list(main_list)
            if temp_list[i] == ' ':
                temp_list[i] = turn_control['p']
                if win_check(temp_list, turn_control['p']) == True:
                    main_list[i] = turn_control['c']
                    turn_change()
                    break
    temp_list = []
    if turn == 'c' and in_play == True:
        for i in range(9):
            if main_list[i] == ' ':
                temp_list.append(i)
        main_list[random.choice(temp_list)] = turn_control['c']
        turn_change()
        
def turn_change():
    global turn
    flag = True
    for ch in main_list:
        if ch == ' ':
            flag = False
    if flag == True:
        timer.start()
    else:
        if turn == 'p':
            turn = 'c'
        else:
            turn = 'p'

def win_check(listy, ch):
    for i in range(3):
        if listy[i] == ch and listy[i+3] == ch and listy[i+6] == ch:
            return True
        if listy[3*i] == ch and listy[3*i+1] == ch and listy[3*i+2] == ch:
            return True
    if listy[4] == ch:
        if listy[0] == ch and listy[8] == ch:
            return True
        if listy[2] == ch and listy[6] == ch:
            return True
    return False
  
def get_center(position):
    x_coord = width * (0.7 + 0.8 * (position % 3)) / 3 
    y_coord = height * (0.7 + 0.8 * (position / 3)) / 3
    return list([x_coord, y_coord])

def draw_object(canvas, obj, center, color):
    if obj == 'X':    
        canvas.draw_line((center[0] - 0.1 * width, center[1] - 0.1 * height), (center[0] + 0.1 * width, center[1] + 0.1 * height), 6, color)
        canvas.draw_line((center[0] + 0.1 * width, center[1] - 0.1 * height), (center[0] - 0.1 * width, center[1] + 0.1 * height), 6, color)
    elif obj == 'O':
        canvas.draw_circle(center, (height+width)/20, 6, color)
        
def grid(canvas):
    canvas.draw_line((width * 0.367, height * 0.1), (width * 0.367, height * 0.9), 12, 'black')
    canvas.draw_line((width * 0.634, height * 0.1), (width * 0.634, height * 0.9), 12, 'black')
    canvas.draw_line((width * 0.1, height * 0.367), (width * 0.9, height * 0.367), 12, 'black')
    canvas.draw_line((width * 0.1, height * 0.634), (width * 0.9, height * 0.634), 12, 'black')
    
def draw(canvas):
    grid(canvas)
    for i in range(9):
        draw_object(canvas, main_list[i], get_center(i), 'lime')
    if in_play == False:
        canvas.draw_text('Click New Game to play again', (430, 680), 20, 'blue')
        if turn == 'p':
            canvas.draw_text('Player wins!', (480,650), 30, 'blue')
        else:
            canvas.draw_text('Computer wins', (470,650), 30, 'Blue')                           
        
def click(pos):
    global main_list, in_play
    if turn == 'p' and in_play == True:
        if (pos[0] > 0.1 * width) and (pos[0] < 0.9 * width):
            if (pos[1] > 0.1 * height) and (pos[1] < 0.9 * height):
                x = int((pos[0] - 0.1 * width) / (width * 0.267))
                y = int((pos[1] - 0.1 * height) / (height * 0.267))
                if main_list[(y * 3) + x] == ' ':  
                    main_list[(y * 3) + x] = turn_control['p'] 
                    if win_check(main_list, turn_control['p']) == False:
                        turn_change()
                        computer_AI()
                    else:
                        in_play = False

def new_game():
    global turn, turn_control, main_list, in_play
    timer.stop()
    main_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    turn = random.choice(['p', 'c'])
    in_play = True
    if turn == 'p':
        turn_control['p'] = 'X'
        turn_control['c'] = 'O'
    else:
        turn_control['c'] = 'X'
        turn_control['p'] = 'O' 
        computer_AI()
    
                                      

frame = simplegui.create_frame('Tic-Tac-Toe', width, height)
timer = simplegui.create_timer(500, new_game)
frame.add_button('New Game', new_game)
frame.set_mouseclick_handler(click)
frame.set_canvas_background('orange')
frame.set_draw_handler(draw)
frame.start()
