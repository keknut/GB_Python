# 1. Считать строку чисел из файла. Напишите программу,
# которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

path = 'digits.txt'

with open(path, 'r') as dataRead:
    data = dataRead.read().split(' ')
for i in range (0, len(data)):
    data[i] = int(data[i])
print(data)
print(f'Max: {max(data)}\nMin: {min(data)}')