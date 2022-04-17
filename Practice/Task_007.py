# По заданному номеру дня недели вывести его название

number = int(input('Enter the number of the day of the week: '))
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Satturday', 'Sunday']

if(number > 0 and number < 8):
    print(week[number - 1])
else:
    print('There is no such day')