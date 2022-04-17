# Выяснить, являются ли числа от 1 до N чётными.

number = int(input('Input number: '))
for i in range (1, number + 1):
    if not i % 2:
        print(f'{i}')