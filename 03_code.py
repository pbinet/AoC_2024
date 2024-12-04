import os

input_file = '03_Input.txt'
#input_file = '03_Example.txt'
#input_file = '03_Example2.txt'

if __name__ == '__main__':
    tot = 0
    tot2 = 0

    input = ''
    f =  open(input_file, 'r')
    for line in f:
        input += line

    i = 0
    while input.find('mul(',i) > 0:
        j = input.find(')',input.find('mul(',i))
        s = input[input.find('mul(',i)+4:j]
        if s.count(',') == 1:
            data = s.split(',')
            try:
                if int(data[0]) < 1000 and int(data[0]) < 1000:
                    #print(s)
                    tot += int(data[0]) * int(data[1])
            except:
                a = 1
                #print (s)
        i = input.find('mul(',i) + 1

    i = 0
    do = True
    while input.find('mul(',i) > 0:
        i = min(max(input.find('mul(',i),i), max(input.find('do()',i),i), max(input.find('don\'t()',i),i))

        if input[i:i+4] == 'do()': do = True
        print(str(i) + ' - ' + input[i:i+7])
        if input[i:i+7] == 'don\'t()':
            do = False

        if input[i:i+3] == 'mul' and do:
            j = input.find(')',input.find('mul(',i))
            s = input[input.find('mul(',i)+4:j]
            if s.count(',') == 1:
                data = s.split(',')
                try:
                    if int(data[0]) < 1000 and int(data[0]) < 1000:
                        #print(s)
                        tot2 += int(data[0]) * int(data[1])
                except:
                    print (s)
        i += 1


    print('Answer 1: ' + str(tot))
    print('Answer 2: ' + str(tot2))