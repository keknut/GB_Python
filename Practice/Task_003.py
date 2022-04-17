# Найти максимальное из трёх чисел

number1 = int(input('Input first number: '))
number2 = int(input('Input second number: '))
number3 = int(input('Input third number: '))
maxx = number1
if(number2 > maxx):
    maxx = number2
if(number3 > maxx):
    maxx = number3
print(f'Numbers {number1}, {number2}, {number3}.\nMax number: {maxx}')