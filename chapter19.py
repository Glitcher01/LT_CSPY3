def readposint():
    num = input('Enter a positive integer: ')
    try:
        val = int(num)
        if val <= 0:
            print("{0} is a integer, but isn't positive!".format(val))
        else:
            print('{0} is a positive integer'.format(val))
    except:
        if num == "":
            raise TypeError("You didn't type in anything!")
        else:
            raise TypeError("{0} isn't a integer!".format(int))


readposint()
