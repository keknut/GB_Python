# Задайте натуральное число N.
# Напишите программу, которая составит
# список простых множителей числа N.

multipliers = [] # список будет хранить все простые множители
number = int(input('Enter number: '))
devider = 2 # изначальный делитель числа

while number > 1: # пока число больше единицы, функция выполняется
    # Если число делится без остатка на делитель,
    # заносим делитель в список множителей
    # и обнуляем делитель на двойку
    if number % devider == 0:
        number = number / devider
        multipliers.append(devider)
        devider = 2
    # иначе увеличиваем делитель на единицу
    else:
        devider += 1

print(f'Multipliers: {multipliers}')