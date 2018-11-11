import simplegui

size = 1000
scale = 2

def draw_graph(canvas):
    for i in range(int(size / 10 * scale)):
        canvas.draw_line((i*10 / scale, 0), (i*10 / scale, size), 0.5, 'green')
        canvas.draw_line((i*100/scale, 0), (i*100/scale, size), 1.5, 'green')
        canvas.draw_line((0 ,i*10 / scale), (size , i*10 / scale), 0.5, 'green')
        canvas.draw_line((0, i*100/scale), (size, i*100/scale), 1.5, 'green')
        

def scale_inc():
    global scale
    scale += 0.1

def scale_dec():
    global scale
    scale -= 0.1

def draw(canvas):
    draw_graph(canvas)
    
    
frame = simplegui.create_frame('graph', size, size)
button1 = frame.add_button('Increase scale', scale_inc)
button1 = frame.add_button('Decrease scale', scale_dec)
frame.set_canvas_background('white')
frame.set_draw_handler(draw)
frame.start()

