# Показать последнюю цифру трёхзначного числа

number = int(input('Input number: '))
if(number > 99 and number < 1000):
    print(number % 10)
else:
    print('Number is not three digits')