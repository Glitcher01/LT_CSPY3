import sys
import turtle

tess = turtle.Turtle()


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def test_suite():
    '''test stuff here'''


def func11_1():
    print(list(range(10, 0, -2)))


def func11_2():
    alex = tess
    alex.color("hotpink")


def func11_3():
    a = [1, 2, 3]
    b = a[:]
    print(a, b)
    b[0] = 5
    print(a, b)


def func11_4():
    this = ['I', 'am', 'not', 'a', 'crook']
    that = ['I', 'am', 'not', 'a', 'crook']
    print('Test 1: {0}'.format(this is that))
    that = this
    print('Test 2: {0}'.format(this is that))


def add_vectors(vector1, vector2):
    list = []
    if len(vector1) == len(vector2):
        for i in range(len(vector1)):
            list.append(vector1[i] + vector2[i])
            return list


def scalar_mult(scale, vector):
    for (i, v) in enumerate(vector):
        vector[i] = v * scale
    return vector


def dot_product(vector1, vector2):
    if len(vector1) == len(vector2):
        dot = 0
        for i in range(len(vector1)):
            dot += vector1[i] * vector2[i]
        return dot


def cross_product(vector1, vector2):
    list = []
    if len(vector1) == len(vector2) and len(vector1) == 3:
        for i in range(3):
            list.append(vector1[(i + 1) % 3] * vector2[(i + 2) % 3] - vector1[(i + 2) % 3] * vector2[(i + 1) % 3])
        return list


def replace(str, old, new):
    return new.join(str.split(old))


def swap(a, b):
    print("before swap statement: x:", a, "y:", b)
    (a, b) = (b, a)
    print("after swap statement: x:", a, "y:", b)


swap([1, 2, 3], [3, 4, 6])
test_suite()
turtle.mainloop()
