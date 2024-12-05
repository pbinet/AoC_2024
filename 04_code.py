import os

input_file = '04_Input.txt'
input_file = '04_Example.txt'
#input_file = '03_Example2.txt'

def lines(puzzle):
    return puzzle

def columns(puzzle):
    c = []
    for i in range(len(puzzle[0])):
        l = ''
        for j in range(len(puzzle[0])):
            l+=puzzle[j][i:i+1]
        c.append(l)
    return c

def diag1(puzzle):
    c = []
    for i in range(len(puzzle) + len(puzzle[0] -1 )):
        l = ''

        for j in range(min(i, len(puzzle[0],len(puzzle) + len(puzzle[0]) - i ):
            l+=puzzle[max(len(puzzle)-i,0)][i:i+1]
        c.append(l)
    return c




if __name__ == '__main__':
    tot = 0
    tot2 = 0
    puzzle = []
    f =  open(input_file, 'r')
    for line in f:
      chars = line.split()
      l = []
      puzzle.append(line[:-1])

    print(puzzle[0])
    print(puzzle)
    print(columns(puzzle))