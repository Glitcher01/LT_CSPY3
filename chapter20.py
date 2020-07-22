from unit_tester import test


def c20_1(string):
    data = {}
    for i in string:
        i = i.lower()
        if i.isalpha():
            if i not in data:
                data[i] = 1
            else:
                data[i] += 1
    data = list(data.items())
    data.sort()
    for (l, t) in data:
        print('{0:<2}{1}'.format(l, t))


def add_fruit(inventory, fruit, quantity=0):
    if fruit not in inventory:
        inventory[fruit] = quantity
    else:
        inventory[fruit] += quantity


def text_to_words(the_text):
    """ return a list of words with all punctuation removed,
        and all in lowercase.
    """

    my_substitutions = the_text.maketrans(
        # If you find any of these
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
        # Replace them by these
        "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds


def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds


def alice_words():
    data_file = open('alice_words.txt', 'w')
    data_file.write('{0}{1:>18}\n'.format('Word', 'Count'))
    data_file.write('======================\n')
    data = {}
    words = get_words_in_book('AliceInWonderland.txt')
    words.remove('s')
    counter = 0
    for i in words:
        if i not in data:
            data[i] = 1
        else:
            data[i] += 1
    data_file = open('alice_words.txt', 'w')
    data_file.write('{0}{1:>18}\n'.format('Word', 'Count'))
    data_file.write('======================\n')
    data = list(data.items())
    data.sort()
    for (word, count) in data:
        data_file.write('{0:<17}{1}\n'.format(word, count))

alice_words()
