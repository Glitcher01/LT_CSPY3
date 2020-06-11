def func13_1(document):
    doc = open(document, 'r')
    lines = doc.readlines()
    doc.close()
    print(lines)
    newdoc = open('newdoc.txt', 'w')
    for i in range(len(lines) - 1, -1, -1):
        if i == len(lines) - 1:
            newdoc.write(lines[i] + '\n')
        else:
            newdoc.write(lines[i])
    newdoc.close()


def func13_2(document):
    doc = open(document, 'r')
    lines = doc.readlines()
    doc.close()
    newdoc = open('newdoc.txt', 'w')
    for line in lines:
        if 'snake' in line:
            if '\n' not in line:
                newdoc.write(line + '\n')
            else:
                newdoc.write(line)


def func13_3(document):
    doc = open(document, 'r')
    lines = doc.readlines()
    doc.close()
    newdoc = open('newdoc.txt', 'w')
    for i in range(len(lines)):
        newdoc.write('{0: < 5} {1}'.format(i + 1, lines[i]))

func13_3('chapter13text.txt')

def func13_4(document):
    doc = open(document, 'r')
    lines = doc.readlines()
    doc.close()
    newdoc = open('newdoc.txt', 'w')
    for line in lines:
        newdoc.write(line[6:])

func13_3('newdoc.txt')