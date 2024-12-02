import os


input_file = '01_Input.txt'
#input_file = '01_Example.txt'

list_1 = []
list_2 = []
list_2_2 = {}

f = open(input_file, 'r', encoding='utf-8')

for line in f:
    #print(line)
    data = line.split('  ')
    list_1.append(int(data[0]))
    list_2.append(int(data[1]))
    if int(data[1]) not in list_2_2.keys():
      list_2_2[int(data[1])] = 1
    else:
      list_2_2[int(data[1])] += 1

f.close()


list_1.sort()
list_2.sort()

print(list_1)
print(list_2)

tot = 0
tot2 = 0
for i in range(len(list_1)):
    print(str(tot) + ' + (' + str(list_2[i]) + ' - ' + str(list_1[i]) + ')' )
    tot += abs(list_2[i] - list_1[i])
    if list_1[i] in list_2_2.keys():
      tot2 += list_1[i] * list_2_2[list_1[i]]
print('Answer 1: ' + str(tot))
print('Answer 2: ' + str(tot2))