import turtle as t

def move_up():
    t.setheading(90)
    t.forward(50)
    t.stamp()

def move_down():
    t.setheading(-90)
    t.forward(50)
    t.stamp()

def move_right():
    t.setheading(0)
    t.forward(50)
    t.stamp()
    
def move_left():
    t.setheading(180)
    t.forward(50)
    t.stamp()

def reset():
    t.reset()

    
t.shape('turtle')
t.onkey(move_up, 'w')
t.onkey(move_down,'s')
t.onkey(move_right, 'd')
t.onkey(move_left, 'a')
t.onkey(reset, 'Escape')
t.listen()
