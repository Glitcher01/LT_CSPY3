import string
import math
import sys


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def test_suite():
    """test stuff in here"""


def find(string, char, index=0, end=None):
    if end is None:
        end = len(string)
    while index < end:
        if string[index] == char:
            return index
        index += 1
    return -1


def func_82():
    prefixes = "JKLMNOPQ"
    suffix = "ack"
    for i in prefixes:
        if i in 'OQ':
            print(i + 'u' + suffix)
        else:
            print(i + suffix)


def func_84(str, letter):
    counter = 0
    index = 0
    while index < len(str):
        result = find(str, letter, index)
        if result == -1:
            return counter
        else:
            counter += 1
        index = result + 1
    return counter


def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct


def func_85(str):
    words = remove_punctuation(str).split()
    words_with_e = 0
    for word in words:
        if "e" in word: words_with_e += 1

    print("Your text contains", len(words), "words, of which", words_with_e, "(",
          round(words_with_e * 100 / len(words), 2), '%) contain a "e" ')


def func_86(number):
    #layout = ""
    #list = []
    #for i in range(1, number + 1):
        #layout += ("{" + ":>" + (str(math.ceil(number / 10) * 3)) + "}")
        #list.append(i)
    #for i in range(1, number + 1):
        #new_list = [x * i for x in list]
        #print(layout.format(*new_list))
        for i in range(1, number + 1):
            for j in range(1, number + 1):
                print(i * j, end = "\t");
            print()


def func_87(str):
    new_str = ""
    for i in range(1, len(str) + 1):
        new_str += str[-i]
    return new_str


def func_88(str):
    return str + func_87(str)


def func_89(letter, string):
    new_word = ""
    arr = []
    for i in string:
        if i != letter: new_word = new_word + i
    return new_word
    #return string.replace(letter, '')


def func_810(string):
    return func_87(string) == string


def func_811(substring, word):
    index = 0
    counter = 0
    while index < len(word):
        result = word.find(substring, index)
        if result == -1:
            return counter
        else:
            counter += 1
        index = result + 1
    return counter


def func_812(substring, word):
    #result = word.find(substring)
    #if result != -1:
        #return word[0:result] + word[result + len(substring):]
    #return word
    return word.replace(substring, '', 1)

def func_813(substring, word):
    # index = 0
    # new_word = word
    # while index <= len(word):
    # result = new_word.find(substring, index)
    # if result == -1:
    # return new_word
    # else:
    # new_word = func_812(substring, new_word, index)
    # index = result
    # return new_word
    return word.replace(substring, "")

func_86(12)