def func13_1(document):
    doc = open(document, 'r+')
    lines = doc.readlines()
    newdoc = open('newdoc.txt', 'w')
    for i in range(len(lines) - 1, -1, -1):


func13_1('chapter13text.txt')