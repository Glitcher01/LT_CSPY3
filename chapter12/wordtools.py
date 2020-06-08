import string

def cleanword(word):
    str = ''
    for i in word:
        if i not in string.punctuation:
            str += i
    return str

def has_dash(word):
    if "-" in word:
        return True
    return False

def extract_words(str):
    seperators = string.punctuation

    for i in seperators:
        str = str.replace(i, ' ')
    return[j.strip() for j in str.split()]

def longest_word(list):
    arr = []
    for i in list:
        arr.append(len(i))
    arr.append(0)
    arr.sort(reverse=True)
    return arr[0]

print(longest_word(['superdsgsgvds']))