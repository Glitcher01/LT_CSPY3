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
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

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

    def collision(self, rect):
        if rect.corner.x + rect.width > self.corner.x > rect.corner.x - self.width:
            if rect.corner.y + rect.height > self.corner.y > rect.corner.y - self.height:
                return True
        return False
