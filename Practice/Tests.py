delete_str = input('Input string: ')
my_str = 'Усложнение. В данном решении пользователь сам задаёт строку. Если программа найдёт слова содержащие эту строку, она их удалит.'
print(f'Actual string:\n{my_str}\n----')
my_str = my_str.split(' ')
my_str = ' '.join(map(str, list(filter(lambda word: word.find(delete_str) == -1, my_str))))
print(my_str)
# result = map(lambda word: result += word + ' ', my_str)

print(result)
# numbers = [123, -8, 6, 4, 12]
# print(numbers)
# numbers = list(map(lambda x: x ** 2, numbers))
# print(numbers)