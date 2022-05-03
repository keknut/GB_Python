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

# array = [1, 2, 1, 3, 4, 5, 5, 6, 5, ]

# for i in range (0, len(array)):
#     for j in dictionary.keys():
#         if(j == array[i]):
#             dictionary[j]+=1
# for i in dictionary.keys():
#     if(dictionary[i] == 1):
#         print(i, end=' ')


dictionary = {}
numbers = [1, 2, 4, 6, 2]

dictionary[numbers[0]]+= 1

print(dictionary)