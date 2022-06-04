action = {
    '+' : lambda x, y: x + y,
    '-' : lambda x, y: x - y,
    '*' : lambda x, y: x * y,
    '/' : lambda x, y: x / y
}

expression = [1.0, '+', 2.0, '-', 3.0, '*', 4.0, '/', 5.0]
index = [i for i in range(len(expression)) if expression[i] == '*' or expression[i] == '/']
while len(index) > 0:
    expression[index[0] - 1] = action[expression[index[0]]](expression[index[0] - 1] ,expression[index[0] + 1])
    expression.pop(index[0])
    expression.pop(index[0])
    index = [i for i in range(len(expression)) if expression[i] == '*' or expression[i] == '/']
print(index)
print(expression) 