# Дано число в отрезке [10, 99].Показать наибольшую цифру числа.

number = int(input('Input number: '))
if(number > 9 and number < 100):
    tmp = number % 10
    number = number // 10
    if(number > tmp):
        print(number)
    else:
        print(tmp)
else:
    print('Number is not two digits')