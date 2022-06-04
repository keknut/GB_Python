# Напишите программу вычисления арифмитического выражения заданного строкой.
# Стандартные опреации +|-|*|/
# 2+2
# 1+2*3
# 1-2/3


#Выражение должно заканчиваться только цифрой. Если будет заканчиваться на оператор, вылетит ошибка.
def index_first(expression):
    return [i for i in range(len(expression)) if expression[i] == '*' or expression[i] == '/']

def index_second(expression):
    return [i for i in range(len(expression)) if expression[i] == '+' or expression[i] == '-']

def first_priority(data_list):
    index = index_first(data_list)
    while len(index) > 0:
        data_list[index[0] - 1] = action[data_list[index[0]]](data_list[index[0] - 1] ,data_list[index[0] + 1])
        data_list.pop(index[0])
        data_list.pop(index[0])
        index = index_first
    return data_list

def second_priority(data_list):
    index = index_second(data_list)
    while len(index) > 0:
        data_list[index[0] - 1] = action[data_list[index[0]]](data_list[index[0] - 1] ,data_list[index[0] + 1])
        data_list.pop(index[0])
        data_list.pop(index[0])
        index = index_second(data_list)
    return data_list

data_list = []

action = {
    '+' : lambda x, y: x + y,
    '-' : lambda x, y: x - y,
    '*' : lambda x, y: x * y,
    '/' : lambda x, y: x / y
}

input_expression = input('Enter expression: ').replace(' ', '')
for char in input_expression:
    try:
        data_list.append(float(char))
    except ValueError:
        data_list.append(char)

data_list = first_priority(data_list)
data_list = second_priority(data_list)
print(f'Answer: {data_list[0]}')