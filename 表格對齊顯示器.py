# Transpose data practice.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def maxLen(number):
    length = []
    for y in range(4):
        w = len(tableData[number][y])
        length.append(w)
    return max(length)

def  printTable(tableData):
    for y in range(4):
        for x in range(3):
            print(tableData[x][y].rjust(maxLen(x)), end = ' ')
        print()

printTable(tableData)