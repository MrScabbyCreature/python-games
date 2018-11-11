import simplegui
import math
import random

background = simplegui.load_image("http://s8.postimg.org/6d5csc5jn/background.jpg")
bg_length = (2500, 500)
bg_center = [bg_length[0]/2, bg_length[1]/2]
monster = simplegui.load_image("http://s4.postimg.org/cxl8ge7n1/monster.jpg")
monster_length = (300, 300)
control_var = 1240
velocity = 0
frame_len = [1000, 500]
right_end = -250
left_end = 1250

def draw(canvas):
    global control_var
    if control_var <= left_end and control_var >= right_end :
        control_var += velocity
    canvas.draw_image(background, bg_center, bg_length, [control_var, bg_center[1]], [bg_length[0], frame_len[1]])
    
def keydown_handler(key):
    global control_var, velocity
    if key == simplegui.KEY_MAP['left']:
        velocity += 10
    if key == simplegui.KEY_MAP['right']:
        velocity -= 10
        
def keyup_handler(key):
    global control_var, velocity
    if key == simplegui.KEY_MAP['left']:
        velocity -= 10
    if key == simplegui.KEY_MAP['right']:
        velocity += 10
    if control_var > left_end:
        control_var = left_end
    if control_var < right_end:
        control_var = right_end

        
frame = simplegui.create_frame('War', frame_len[0], frame_len[1])
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)
frame.set_draw_handler(draw)
frame.start()
