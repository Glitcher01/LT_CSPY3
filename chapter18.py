import turtle

tess = turtle.Turtle()
tess.pu()
tess.setx(-200)
tess.sety(130)
tess.pd()
tess.speed(1000)


def koch(t, order, size):
    """
       Make turtle t draw a Koch fractal of 'order' and 'size'.
       Leave the turtle facing the same direction.
    """

    if order == 0:  # The base case is just a straight line
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order - 1, size / 3)  # Go 1/3 of the way
            t.left(angle)


def koch_snowflake(t, order, size):
    for i in range(3):
        koch(t, order, size)
        t.right(120)


def cesaro(t, order, size):
    if order == 0:  # The base case is just a straight line
        t.forward(size)
    else:
        for angle in [-85, 170, -85, 0]:
            cesaro(t, order - 1, size)
            t.left(angle)


def cesaro_square(t, order, size):
    for i in range(4):
        cesaro(t, order, size)
        t.right(90)


def sierpinski(t, order, size, colorChangeDepth=-1, color='black'):
    t.color(color)
    if order == 0:
        for i in range(3):
            t.fd(size)
            t.lt(120)
    else:
        if colorChangeDepth == 0:
            sierpinski(t, order - 1, size / 2, colorChangeDepth - 1, 'red')
            t.pu()
            t.fd(size / 2)
            t.pd()
            sierpinski(t, order - 1, size / 2, colorChangeDepth - 1, 'blue')
            t.pu()
            t.bk(size / 2)
            t.lt(60)
            t.fd(size / 2)
            t.rt(60)
            t.pd()
            sierpinski(t, order - 1, size / 2, colorChangeDepth - 1, 'magenta')
            t.pu()
            t.lt(60)
            t.bk(size / 2)
            t.rt(60)
            t.pd()
        else:
            sierpinski(t, order - 1, size / 2, colorChangeDepth - 1, color)
            t.pu()
            t.fd(size / 2)
            t.pd()
            sierpinski(t, order - 1, size / 2, colorChangeDepth - 1, color)
            t.pu()
            t.bk(size / 2)
            t.lt(60)
            t.fd(size / 2)
            t.rt(60)
            t.pd()
            sierpinski(t, order - 1, size / 2, colorChangeDepth - 1, color)
            t.pu()
            t.lt(60)
            t.bk(size / 2)
            t.rt(60)
            t.pd()


def recursive_min(ls):
    firstTime = True
    smallest = None
    for i in ls:
        if isinstance(i, list):
            val = recursive_min(i)
        else:
            val = i

        if firstTime or val < smallest:
            firstTime = False
            smallest = val

    return smallest


def flatten(ls):
    flat = []
    for x in ls:
        if not isinstance(x, list):
            flat.append([x])
        else:
            flat.append(flatten(x))

    print(flat)
    return sum(flat, [])


def not_fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


print(not_fib(200))