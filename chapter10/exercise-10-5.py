import turtle
import sys
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
alex = turtle.Turtle()
jess = turtle.Turtle()


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def test_suite():
    """test stuff in here"""


def draw_housing():
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")
alex.pu()
alex.shape("circle")
alex.shapesize(3)
alex.fillcolor("orange")
alex.fd(40)
alex.lt(90)
alex.fd(120)
jess.pu()
jess.shape("circle")
jess.shapesize(3)
jess.fillcolor("red")
jess.fd(40)
jess.lt(90)
jess.fd(190)

wn.colormode(255)

state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0:  # Transition from state 0 to state 1
        tess.fillcolor(0, 255, 0)
        jess.fillcolor(105, 0, 0)
        alex.fillcolor(173, 104, 0)
        state_num = 1
    elif state_num == 1:
        tess.fillcolor(0, 255, 0)
        jess.fillcolor(105, 0, 0)
        alex.fillcolor('orange')
        state_num = 2
    elif state_num == 2:  # Transition from state 1 to state 2
        tess.fillcolor(0, 105, 0)
        jess.fillcolor(105, 0, 0)
        alex.fillcolor("orange")
        state_num = 3
    else:  # Transition from state 2 to state 0
        alex.fillcolor(173, 104, 0)
        jess.fillcolor("red")
        tess.fillcolor(0, 105, 0)
        state_num = 0
    if (state_num == 2 or state_num == 3):
        wn.ontimer(advance_state_machine, 1000)
    elif (state_num == 1):
        wn.ontimer(advance_state_machine, 3000)
    else:
        wn.ontimer(advance_state_machine, 2000)

advance_state_machine()
test_suite()
wn.mainloop()