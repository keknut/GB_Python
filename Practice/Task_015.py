# Найти наименьшее общее кратное двух чисел

firstNumber = int(input('Input first number: '))
secondNumber = int(input('Input second number: '))
tmp = max(firstNumber, secondNumber)
i = 1
while True:
    if((tmp * i) % firstNumber == 0 and (tmp * i) % secondNumber == 0):
        break
    else:
        i+=1
print(f'NOK: {tmp * i}')