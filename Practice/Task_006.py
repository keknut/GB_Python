# По двум заданным числа проверить, является первое квадратом второго

number1 = int(input('Input first number: '))
number2 = int(input('Input second number: '))
if(number1 ** 2 == number2):
    print('The second number is the square of the first')
elif(number1 == number2 ** 2):
    print('The first number is the square of the second')
else:
    print('Neither number is the square of the other')