# Выяснить, кратно ли число заданному. Если нет, вывести остаток.

number1 = int(input('Input first number: '))
number2 = int(input('Input second number: '))

if not number1 % number2:
    print(f'Number {number1} is a multiple of {number2}')
else:
    print(f'The number {number1} is not a multiple of {number2}. Remainder: {number1 % number2}')