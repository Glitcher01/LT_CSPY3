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
        return Point((p1.x + p2.y) / 2, (p1.y + p2.y) / 2)

    def midpoint(self, target):
        return Point((self.x + target.y) / 2, (self.y + target.y) / 2)

    def slope_from_origin(self):
        return self.y / self.x

    def get_line_to(self, pt):
        slope = (self.y - pt.y) / (self.x - pt.x)
        return (slope, self.y - self.x * slope)


class SMS_store:

    def __init__(self):
        self.inbox = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.inbox.append((from_number, time_arrived, text_of_SMS, False))

    def message_count(self):
        return len(self.inbox)

    def get_unread_indexes(self):
        return [i for i in range(len(self.inbox)) if self.inbox[i][3] == False]

    def get_message(self, i):
        l = list(self.inbox[i])
        l[3] = True
        t = tuple(l)
        self.inbox[i] = t
        return self.inbox[i]

    def delete(self, i):
        self.inbox.remove(self.inbox[i])

    def clear(self):
        self.inbox = []


def dist(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def circumcircle(a):
    x = 0
    y = 0
    d = 2 * (a[0].x * (a[1].y - a[2].y) + a[1].x * (a[2].y - a[0].y) + a[2].x * (a[0].y - a[1].y))
    sides = []
    for i in range(len(a) - 1):
        x += (a[i].x ** 2 + a[i].y ** 2) * (a[(i + 1) % 3].y - a[(i + 2) % 3].y) / d
        y += (a[i].x ** 2 + a[i].y ** 2) * (a[(i + 2) % 3].x - a[(i + 1) % 3].x) / d
        sides.append(dist(a[i], a[(i + 1) % 3]))

    p = sum(sides)
    area = (p / 2 * (p / 2 - sides[0]) * (p / 2 - sides[1]) * (p / 2 - sides[2])) ** 0.5
    r = sides[0] * sides[1] * sides[2] / (4 * area)
    point = Point(x, y)
    if (dist(a[3], point) == r):
        return point
    return False