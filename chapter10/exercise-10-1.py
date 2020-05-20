import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
wn.title("Handling keypresses!")
wn.bgcolor("lightgreen")
pen_size = 1
speed = 6
tess.pensize(pen_size)
tess.speed(speed)

def move_forward():
    tess.fd(30)

def turn_right():
    tess.rt(45)

def turn_left():
    tess.lt(45)

def turn_to_red():
    tess.color('red')

def turn_to_blue():
    tess.color('blue')

def turn_to_green():
    tess.color('green')

def pen_increase():
    global pen_size
    tess.pensize(max(1, min(pen_size + 1, 20)))
    pen_size += 1

def pen_decrease():
    global pen_size
    tess.pensize(max(1, min(pen_size - 1, 20)))
    pen_size -= 1

def speed_decrease():
    global speed
    tess.speed(max(1, min(speed - 1, 6)))
    speed -= 1

def speed_increase():
    global speed
    tess.speed(max(1, min(speed + 1, 6)))
    speed += 1

wn.onkey(move_forward, "Up")
wn.onkey(turn_right, "Right")
wn.onkey(turn_left, "Left")
wn.onkey(turn_to_red, 'r')
wn.onkey(turn_to_blue, 'b')
wn.onkey(turn_to_green, 'g')
wn.onkey(pen_increase, '+')
wn.onkey(pen_decrease, '-')
wn.onkey(speed_increase, 'w')
wn.onkey(speed_decrease, 's')
wn.listen()
turtle.mainloop()