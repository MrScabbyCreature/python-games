#game that has a timer and you need to stop the timer
#with 0 at the end.

import simplegui

#necessary global variables

#time for the timer
time = 0
#the display for the timer(string form)
watch = ''
#tries and correct presses
tries = 0
correct = 0


#changes time to watch(number to string of form A:BC.D)
def format():
    global time, watch
    t = time
    deciseconds = t % 10
    remains = t - deciseconds
    seconds = (remains % 600) / 10
    minutes = remains / 600
    if seconds<10:
        zero = '0'
    else:
        zero = ''        
    watch = str(minutes) + ":" + zero + str(seconds) + "." + str(deciseconds)
    

#increase the time    
def increment():
    global time
    time = time + 1   
    
    
#start the timer    
def start():
    timer.start()
    

#stop the timer + claculate the tries and correct stops
def stop():
    global correct, tries
    timer.stop()
    if time != 0:
        tries = tries + 1
        if time % 10 == 0:
            correct = correct + 1


#reset all values            
def reset():
    global time, correct, tries
    time, correct, tries = 0,0,0
    stop()    


#necessary drawings    
def draw(canvas):
    format()
    canvas.draw_text(str(correct), (253, 30), 30, 'white')
    canvas.draw_text('/', (270, 30), 30, 'white') 
    canvas.draw_text(str(tries), (280, 30), 30, 'white')
    canvas.draw_text(watch, (70, 130), 60,'white')
    

#frame and event handlers
frame = simplegui.create_frame("StOpWaTcH: gAmE", 320, 200)
button1 = frame.add_button("Start timer", start, 100)
button2 = frame.add_button("Stop timer", stop, 100)
button3 = frame.add_button("Resrt timer", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, increment)


#start of the game
frame.start()
