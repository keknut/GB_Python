# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов (нет нулевых кофициентов).

import re
import numpy

def ReadFile(path):
    data = open(path, 'r')
    dataString = data.read()
    data.close()
    dataString = re.sub(r'\*x\^\d*', '', dataString)
    dataString = re.sub(r'\*x', '', dataString)
    dataString = re.sub(r'\s\+', '', dataString)
    dataString = re.sub(r'\s\=\s0', '', dataString)
    #dataString = dataString.replace('=', '')
    dataList = dataString.split(' ')
    for i in range(0, len(dataList)):
        dataList[i] = int(dataList[i])
    return dataList

def writeFile(path, dataWrite):
    # открытие файла для записи
    data = open(path, 'w')

    for i in range(0, len(dataWrite)):
        if(i < (len(dataWrite) - 2)):
            data.write(f'{dataWrite[i]}*x^{len(dataWrite)-i} + ')
        if(i == (len(dataWrite) - 2)):
            data.write(f'{dataWrite[i]}*x + {dataWrite[len(dataWrite) - 1]} = 0\n')
    data.close()

first_path = 'First_x.txt'
second_path = 'Second_x.txt'

first_data = ReadFile(first_path)
second_data = ReadFile(second_path)
resultData = numpy.polyadd(first_data, second_data)
writeFile('Result.txt', resultData)