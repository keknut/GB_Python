# Найдите корни квадратного уравнения Ax² + Bx + C = 0
# двумя способами:
#    *пользователь вводит А, В, С
#    1) с помощью математических формул нахождения
#       корней квадратного уравнения
#    2) с помощью дополнительных библиотек Python

a = int(input('Input A: '))
b = int(input('Input B: '))
c = int(input('Input C: '))

def discriminant(a, b ,c):
    return b ** 2 - 4 * a * c

def math(a, b ,c):
    if(discriminant(a, b, c) < 0):
        print("No result")
    elif(discriminant(a, b, c) == 0):
        x = -b / (2 * a)
        print(f'x = {x}')
    else:
        x1 = (-b + discriminant(a, b, c) ** 0.5) / (2 * a)
        x2 = (-b - discriminant(a, b, c) ** 0.5) / (2 * a)
        xTuple = (x1, x2)
        print(f'x1 = {x1}\nx2 = {x2}')

math(a, b ,c)