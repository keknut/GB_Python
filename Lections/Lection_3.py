# В файле хранятся числа. Нужно выбрать чётные
# и составить список пар (чётные ; квадрат числа)

def quarter(number):
    return number**2

numbers = [1, 2, 3, 5, 8, 15, 22, 23, 38]
quarters = [(i, quarter(i)) for i in numbers if i % 2 == 0]
print(quarters)