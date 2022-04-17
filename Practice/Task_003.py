# Найти максимальное из трёх чисел

number1 = int(input('Input first number: '))
number2 = int(input('Input second number: '))
number3 = int(input('Input third number: '))
max = number1
if(number2 > max):
    max = number2
if(number3 > max):
    max = number3
print(f'Numbers {number1}, {number2}, {number3}.\nMax number: {max}')