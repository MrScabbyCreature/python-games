# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
# put them in a function and save space!
def variables():
    global width, height, radius, pad_width, pad_height, half_pad_width, half_pad_height, left, right, ball_pos, ball_vel
    global score1, score2, pad1_pos, pad2_pos, pad1_vel, pad2_vel
    width = 600
    height = 400       
    radius = 20
    pad_width = 8
    pad_height = 80
    half_pad_width = pad_width / 2
    half_pad_height = pad_height / 2
    right = True
    left = False
    pad1_pos = [half_pad_width, height/2 - half_pad_height]
    pad2_pos = [width - half_pad_width, height/2 - half_pad_height]
    pad1_vel = 0
    pad2_vel = 0
    score1 = 0
    score2 = 0
variables()    

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [width/2, height/2]
    x = random.randrange(3, 5)
    y = random.randrange(2, 4)
    if direction == True:
        ball_vel = [x, -y]
    if direction == False:
        ball_vel = [-x, -y]        
    

# define event handlers
def new_game():
    global pad1_pos, pad2_pos, pad1_vel, pad2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(right)
    
def draw(canvas):
    global score1, score2, pad1_pos, pad2_pos, ball_pos, ball_vel, pad1_vel, pad2_vel
 
        
    # draw mid line and gutters
    canvas.draw_line((0, height/2), (width, height/2), width, 'green')  
    canvas.draw_line([width / 2, 0],[width / 2, height], 1, "White")
    canvas.draw_line([pad_width, 0],[pad_width, height], 1, "White")
    canvas.draw_line([width - pad_width, 0],[width - pad_width, height], 1, "White")
       
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[1] <= radius or ball_pos[1] >= height - radius:
        ball_vel[1] = - ball_vel[1]
        
    if ball_pos[0] <= pad_width + radius and ball_pos[0] >= pad_width:
        if ball_pos[1] >= pad1_pos[1] and ball_pos[1] <= pad1_pos[1] + pad_height:
            ball_vel[0] *= 1.1
            ball_vel[0] = - ball_vel[0]
        else:
            score2 += 1
            spawn_ball(right)
            
    
    
    if ball_pos[0] >= width - (pad_width + radius) and ball_pos[0] <= width - pad_width:
        if ball_pos[1] >= pad2_pos[1] and ball_pos[1] <= pad2_pos[1] + pad_height:
            ball_vel[0] *= 1.1
            ball_vel[0] = - ball_vel[0]
        else:
            score1 += 1
            spawn_ball(left)
    
    # draw ball
    canvas.draw_circle(ball_pos, radius, 4, "blue", "yellow")
    
    # update paddle's vertical position, keep paddle on the screen
    if pad1_pos[1] > 0 and (pad1_pos[1] + pad_height) < height:
        pad1_pos[1] += pad1_vel
    
    if pad2_pos[1] > 0 and (pad2_pos[1] + pad_height) < height:
        pad2_pos[1] += pad2_vel
        
    # draw paddles
    canvas.draw_line(pad1_pos, (pad1_pos[0], pad1_pos[1]+pad_height) , pad_width, "black")
    canvas.draw_line(pad2_pos, (pad2_pos[0], pad2_pos[1]+pad_height), pad_width, "black")
    
    # draw scores
    canvas.draw_text(str(score1), [150,100], 60, "orange")
    canvas.draw_text(str(score2), [450,100], 60, "orange")
        
def keydown(key):
    global pad1_vel, pad2_vel
    if key == simplegui.KEY_MAP['w']:
        pad1_vel -= 7
    if key == simplegui.KEY_MAP['s']:
        pad1_vel += 7
    if key == simplegui.KEY_MAP['up']:
        pad2_vel -= 7
    if key == simplegui.KEY_MAP['down']:
        pad2_vel += 7
   
def keyup(key):
    global pad1_vel, pad2_vel, pad1_pos, pad2_pos
    if key == simplegui.KEY_MAP['w']:
        pad1_vel += 7           
        if pad1_pos[1] <= 0:
            pad1_pos[1] = 1
    if key == simplegui.KEY_MAP['s']:
        pad1_vel -= 7
        if pad1_pos[1] >= (height - pad_height):
            pad1_pos[1] = height - pad_height - 1
    if key == simplegui.KEY_MAP['up']:
        pad2_vel += 7
        if pad2_pos[1] <= 0:
            pad2_pos[1] = 1
    if key == simplegui.KEY_MAP['down']:
        pad2_vel -= 7
        if pad2_pos[1] >= (height - pad_height):
            pad2_pos[1] = height - pad_height - 1
            
def restart():
    global score1, score2
    score1, score2 = 0, 0
    spawn_ball(left)

# create frame
frame = simplegui.create_frame("Pong", width, height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart)

# start frame
new_game()
frame.start()
