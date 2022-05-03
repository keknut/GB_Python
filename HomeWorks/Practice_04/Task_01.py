# Вычислить число Пи c заданной точностью d
# Пример:
#
# при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$


# Импорт библиотеки math
import math 

# Функция 
def Accuracy(data):
    i = 0
    while(1 > data):
        i += 1
        data = data * 10
    return i

def AccuracyPI(precision):
    return round(math.pi, precision)

precision = float(input('Input precision (example: 0.001): '))
print(f'{AccuracyPI(Accuracy(precision))}')