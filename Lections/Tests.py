# dictionary = {'up': 'up',
#               'left': 'left',
#               'right': 'right',
#               'bottom': 'bottom'
#               }
# path = "test.txt"

# with open(path, 'w') as dataWrite:
#     for i in dictionary.items():
#         dataWrite.write(f'{i}\n')

# with open(path, 'r') as dataRead:
#     allData = dataRead.read()
# print(allData)


# dictionary = {
#     1 : 0,
#     2 : 0,
#     3 : 0,
#     4 : 0, 
#     5 : 0,
#     6 : 0
# }

# array = [1, 2, 1, 3, 4, 5, 5, 6, 5]
# flag = True

# for i in range (0, len(array)):
#     flag = True
#     for j in dictionary.keys():
#         if(j == array[i]):
#             dictionary[j]+=1
#             flag = False
#             continue
#     if flag:
#         dictionary[array[i]] = 1
# for i in dictionary:
#     if(dictionary[i] == 1):
#         print(i, end=' ')


# dictionary = {}
# numbers = [1, 2, 4, 6, 2]

# dictionary[numbers[0]]+= 1

# for i in dictionary:
#     if (dictionary[i] == 0):
#         print(f'{i}', end=' ')

for i in range(0, 5):
    print(i)