# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

string = input('Input array: ')
array = string.split(' ')
dictionary = {0 : 0}
flag = True

for i in range (0, len(array)):
    flag = True
    for j in dictionary.keys():
        if(j == array[i]):
            dictionary[j]+=1
            flag = False
            continue
    if flag:
        dictionary[i] = 1

for i in dictionary.keys():
    if (dictionary[i] == 1):
        print(f'{i}', end=' ')