# my_str = 'Усложнение. В данном решении пользователь сам задаёт строку. Если программа найдёт слова содержащие эту строку, она их удалит.'
# print(f'Actual string:\n{my_str}\n----')
# my_str = my_str.split(' ')

# for word in my_str:
#     if '.' in word:

# from operator import index


# li =['1', '2', '3', '45', '6']
# for word in li:
#     if '5' in word:
#         word.replace('5')
#         li.insert(index, '5')
# print(li)
# import random

# player_list = ['Player 1', 'Player 2']
# print(player_list[1])
# bots_name = ['Anna', 'Maria', 'David', 'John', 'Simon', 'Alfred', 'Alex']
# temp = ''.join(random.choices(bots_name)).replace('[', '').replace('\'', '')
# # player_list[1] = random.choices(bots_name)
# print(temp)
path = 'GB_Python\HomeWorks\Practice_05\Practice_05_Task_04_test.txt'
try:
    print('Opening file...')
    data = open(path, 'r')
    print('Reading file...')
    print(f'Data in file: {data.read()}')
except FileNotFoundError:
    print('File not found\nCreating file with test data-set')
    data = open(path, 'w')
    data.write('test')
except Exception:
    print("Something gone wrong!")
data.close