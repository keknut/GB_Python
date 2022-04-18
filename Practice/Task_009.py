# Показать последнюю цифру трёхзначного числа
while True:
    number = int(input('Input number: '))
    if(number > 99) and (number < 1000):
        print(number % 10)
        break
    else:
        print('Number is not three digits.')