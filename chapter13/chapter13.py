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


func13_2('chapter13text.txt')