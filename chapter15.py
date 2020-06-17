class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def dist_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    @staticmethod
    def distance_from_origin(pt):
        return (pt.x ** 2 + pt.y ** 2) ** 0.5

    def reflect_x(self):
        return Point(self.x, -self.y)

    def to_string(self):
        return "({0}, {1})".format(self.x, self.y)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    @staticmethod
    def midpoint(p1, p2):
        return Point((p1.x + p2.y)/2, (p1.y + p2.y) / 2)

    def midpoint(self, target):
        return Point((self.x + target.y) / 2, (self.y + target.y) / 2)

    def slope_from_origin(self):
        return self.y / self.x

    def get_line_to(self, pt):
        slope = (self.y - pt.y) / (self.x - pt.x)
        return (slope, self.y - self.x * slope)



def dist(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y)**2) ** 0.5


print(Point(4, 11).get_line_to(Point(6, 15)))