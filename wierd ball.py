import simplegui
import random

width = 700
height = 700
radius = 20

position = [436 , 192]
vel  = [0,0]

def draw(canvas):
    position[0] += vel[0]
    position[1] += vel[1]
    
    if (position[0] <= radius) or (position[0] >= (width - (radius + 1))):
        vel[0] = - vel[0]
        #if abs(vel[0]) > 20:
         #   vel[0] = vel[0] / 2
    if (position[1] <= radius) or (position[1] >= (height - (radius + 1))): 
        vel[1] = - vel[1]
        #if abs(vel[1]) > 20:
         #   vel[1] = vel[1] / 2
    variance1 = random.randrange(-1 , 2)
    variance2 = random.randrange(-1 , 2)
    vel[0] = vel[0] + variance1
    vel[1] = vel[1] + variance2
    
    canvas.draw_circle(position, radius, 35, "white", "blue")
    
frame = simplegui.create_frame("ball", width, height)
frame.set_draw_handler(draw)
frame.start()