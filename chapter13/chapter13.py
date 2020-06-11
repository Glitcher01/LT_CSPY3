def func13_1(document):
    doc = open(document, 'r+')
    lines = doc.readlines()
    doc.close()
    print(lines)
    newdoc = open('newdoc.txt', 'w')
    for i in range(len(lines) - 1, -1, -1):
        newdoc.write(lines[i] + '\n')


func13_1('chapter13text.txt')