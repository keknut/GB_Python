# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

my_str = 'Напишите програбвмму, удабвляющую из текста все слова, содержащие'
my_str = my_str.split(' ')
result = ''
for word in my_str:
    if word.find('абв') == -1:
        result += word + ' '

print(result)