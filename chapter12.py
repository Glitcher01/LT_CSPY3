import sys
from unit_tester import test
import calendar
import math
import mymodule1
import mymodule2


def func12_1a():
    cal = calendar.TextCalendar()
    cal.pryear(2012)


def func12_1b():
    cal = calendar.TextCalendar(3)
    cal.pryear(2012)


def func12_1c(year=0, month=0):
    cal = calendar.TextCalendar()
    cal.prmonth(year, month)


def func12_1d(weekday=0, language='English', year=0):
    d = calendar.LocaleTextCalendar(weekday, language)
    d.pryear(year)

# calendar.isleap(year) prints out whether or not the year is a leap year
# math.ceil(x) is the smallest integer >= x
# math.floor(x) is the largest integer <= x
# we can do x**(1/2) to find the square root of x without using the math module
# there are actually 3, but tau is essentially 2 pi:
# math.pi = 3.141592653589793
# math.e = 2.718281828459045
# math.tau = 6.283185307179586
# deep copy creates a copy of the object and the elements inside that

def func12_4():
    print(mymodule1.myage - mymodule2.myage ==
          mymodule2.year - mymodule1.myage)
    print("My name is ", __name__)
