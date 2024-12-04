import os
from zipfile import stringCentralDir

input_file = '02_Input.txt'
#input_file = '02_Example.txt'

def is_increasing(level, max_gap):
    return all(0 < level[i+1] - level[i] <= max_gap for i in range(len(level)-1))

def is_decreasing(level, max_gap):
    return all(0 < level[i] - level[i+1] <= max_gap for i in range(len(level)-1))

def part1():
    result = sum(l==True for l in [is_increasing(level, 3) or is_decreasing(level,3) for level in puzzle])
    print(f"Result is {result}")

def is_increasing_tolerate(level, max_gap):
    return sum(is_increasing(level[:i] + level[i+1:], max_gap) for i in range(len(level))) > 0

def is_decreasing_tolerate(level, max_gap):
    return sum(is_decreasing(level[:i] + level[i + 1:], max_gap) for i in range(len(level))) > 0





def check_dir(row):
    data = row.split(' ')
    direction = ''
    for i in range(len(data) - 1):
        new_dir = 'A'
        if int(data[i + 1]) > int(data[i]) and int(data[i + 1]) - int(data[i]) < 4: new_dir = 'I'
        if int(data[i + 1]) < int(data[i]) and int(data[i]) - int(data[i + 1]) < 4: new_dir = 'D'
        direction += new_dir
    if direction.count('D') == len(direction)  or direction.count('I') == len(direction) :
        return 'ok'
    else:
        return 'ko'



def check_dir2(row):
    data = row.split(' ')
    r = 'ko'
    print('\n' + row[:-1])
    for i in range(len(data)):
        new_row = ' '.join(data[:i] + data[i+1:])
        print(new_row[:-1] + ' ' + check_dir(new_row))
        if check_dir(new_row) == 'ok':
            r = 'ok'

    print(r + ' | Decreasing ' + str(is_decreasing_tolerate([int(value) for value in data], 3)) + ' Increasing ' + str(is_increasing_tolerate([int(value) for value in data], 3)))
    if r == 'ok' :
        return 'ok'
    else:
        return 'ko'



if __name__ == '__main__':

    f = open(input_file, 'r', encoding='utf-8')

    tot = 0
    tot2 = 0
    d = 0

    for line in f:
        #print(line)
        if check_dir(line) == 'ok':
            tot += 1
        else:
            #print(line)
            if check_dir2(line) == 'ok': tot2 += 1





        if d < 0:
            print(line[:-1] )
            data = line.split(' ')

            for i in range(len(data) - 1):
                print( str(i) + '-> ' + '-'.join(data[0:i] + data[i+1:]))

        d += 1

    f.close()


    print('Answer 1: ' + str(tot))
    print('Answer 2: ' + str(tot2))
    print('Answer 2: ' + str(tot + tot2))