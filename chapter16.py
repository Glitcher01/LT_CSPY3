from unit_tester import test
from chapter15 import Point

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w=1, h=1):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        return self.width * self.height

    def flip(self):
        self.width, self.height = self.height, self.width

    def contains(self, pt):
        if self.corner.x <= pt.x < self.corner.x + self.width:
            if self.corner.y <= pt.y < self.corner.y + self.height:
                return True
        return False


rect = Rectangle(Point(), 10, 5)
test(rect.contains(Point(0, 0)) == True)
test(rect.contains(Point(3, 3)) == True)
test(rect.contains(Point(3, 7)) == False)
test(rect.contains(Point(3, 5)) == False)
test(rect.contains(Point(3, 4.99999)) == True)
test(rect.contains(Point(-3, -3)) == False)

