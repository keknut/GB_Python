# Даны два числа. Показать большее и меньшее из них.

number1 = int(input('Input first number: '))
number2 = int(input('Inpust second number: '))
if(number1 > number2):
    print(f'{number1} > {number2}')
elif(number1 < number2):
    print(f'{number2} > {number1}')
else:
    print("The numbers are equal.")