import turtle
import random

class TurtleGTX(turtle.Turtle):
    def __init__(self, *args, **kwargs):
        super(TurtleGTX, self).__init__(*args, **kwargs)
        self.odometer = 0
        self.break_percent = 23
        self.can_drive = True

    def forward(self, distance: float) -> None:
        if random.randint(1, 100) <= self.break_percent or self.can_drive is False:
            self.can_drive = False
            print('Uh oh!')
            return
        super(TurtleGTX, self).forward(distance)
        self.odometer += abs(distance)

    def back(self, distance: float) -> None:
        if random.randint(1, 100) <= self.break_percent or self.can_drive is False:
            self.can_drive = False
            print('Uh oh!')
            return
        super(TurtleGTX, self).back(distance)
        self.odometer += abs(distance)

    def change_tire(self):
        self.can_drive = True

    bk = back
    backward = back
    fd = forward


tess = TurtleGTX()
tess.fd(100)
turtle.mainloop()
print(tess.odometer)