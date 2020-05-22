import math

import turtle

import sys

import random

bob = turtle.Turtle()


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def test_suite():
    """test stuff in here"""

def func_71(list):
    odd_numbers = 0
    for i in list:
        if i % 2 == 1: odd_numbers += 1
    return odd_numbers


def func_72(list):
    total_even = 0
    for i in list:
        if i % 2 == 0: total_even += i
    return total_even


def func_73(list):
    total_negative = 0
    for i in list:
        if i < 0: total_negative += i
    return total_negative


def func_74(list):
    total = 0
    for i in list:
        if len(i) == 5: total += 1
    return total


def func_75(list):
    first_even = 0
    sum = 0
    for i in list:
        if i % 2 == 0:
            if first_even == 0:
                first_even += 1
            else:
                sum += i
        else:
            sum += i
    return sum


def func_76(list):
    words = 0
    for i in list:
        if i == "sam" or i == "Sam":
            words += 1
            break
        else:
            if type(i) == str:
                words += 1
    return words


def func_77(n, l):
    approx = n / 2
    while True:
        better = (approx + n / approx) / 2
        if abs(approx - better) < l:
            print("better")
            return better
        print("better")
        approx = better


def print_multiples(n, high):
    for i in range(1, high + 1):
        print(i * n, end= '\t')
    print()


def print_mult_table(high):
    for i in range(1, high + 1):
        print_multiples(i, high)


def func_79(n):
    for i in range(1, n + 1):
        print(int(i * (i + 1) / 2)," ", i)


def func_710(number):
    if (type(number) == int and number > 1):
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                print(number, "is not a prime number")
                print(i, "divides", number)
                break
        else:
            print(number, "is a prime number")

    else:
        print(number, "is not more than 1 and/or an integer")


def func_711(t, list):
    for (angle, steps) in list:
        t.rt(angle)
        t.fd(steps)


def func_714(n):
    count = 0
    absolute = abs(n)
    while absolute != 0:
        absolute = absolute // 10
        count += 1
    return count


def func_715(n):
    count = 0
    absolute = abs(n)
    while absolute > 0:
        digit = absolute % 2
        if digit == 0:
            count += 1
        absolute = absolute // 10
    return count


def func_716(list):
    sum = 0
    for i in list: sum += i ** 2
    return sum


def func_717(human_plays_first, player = 0, games = 0, computer = 0):
    rng = random.Random()
    result = rng.randrange(-1, 2)
    result_array = ["You win!", "Game Drawn!", "I win!"]
    games += 1
    print("Human plays first = {0}, winner= {1}".format(human_plays_first, result))
    print(result_array[result + 1])
    if result == -1:
        player += 1
    elif result == 1:
        computer += 1
    print("You tied {0} game(s), won {1} game(s), and lost {2} game(s)".format(games - computer - player, player, computer))
    print("Your win percentage is {0}%".format(round(player / games * 100, 2)))
    play = input("Want to play again? (Y or N) ")
    if play == 'Y' or play == "y":
        print()
        func_717(not human_plays_first, player, games, computer)
    else:
        print("Bye!")
        return

test_suite()
turtle.mainloop()