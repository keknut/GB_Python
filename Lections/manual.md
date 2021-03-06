# Материалы по Python

### Арифмитические операции

Умножение: `*`

`a * b`

Деление: `/`

`a / b`

Возведение в степень: `**`

`a ** b`

Остаток от деления: `%`

`a % b`

Целочисленное деление: `//`

`a // b`

### Списки

Копирование списка (срез): `a = b[:]`

``` b = [1, 2, 3]
    a = b[:]
    b.append[4]

    Console:    a = [1, 2, 3]
                b = [1, 2, 3, 4]
```

Ссылка на список: `a = b`

``` b = [1, 2, 3]
    a = b
    b.append[4]

    Console:    a = [1, 2, 3, 4]
                b = [1, 2, 3, 4]
```
### Работа с файлами
```
with open('path', 'a/w/r') as name:
data write('string')
```
Модификаторы:

1. `а` : Режим добавления новой информации в файл (без удаления старой).
2. `w` : Режим перезаписи файла. Старая информация удаляется.
3. `r` режим чтения из файла.

### Функции и модули

Функции
```
def function_name(argument)
    #body line 1
    #body line 2
    ...
    #body line n
    #optional return x
```

Модули

Можно использовать код из других файлов
```
import moduleName as module
```
В этом примере есть конструкция `as`. С её помощью можно делать алиасы для упрощения работы с обращением к модулю.

### Кортежи
Кортеж - некий неизменямый список.
```
t = (1, 2, 3)
```
Кортеж с единственным элементом при помощи одной запятой.
```
t = (1,)
```
### Словари
Неупорядоченные коллекции произвольных объектов с доступом по ключу.

методы:

`keys()`

`values()`

`items()`

```
dictionary = {}
dictionary = {
    'key_1': 'value_1',
    'key_2': 'value_2',
    'key_3': 'value_3',
    'key_4': 'value_4',
}
print(dictionary['<key_1>']) #value_1
```
Добавление или изменение элементов:
```
dctionary['key'] = 'value'
```
Удаление элементов:
```
del dictionary['key']
```
### Множества
Множества содержат в себе уникальные неупорядоченные элементы
```
example = {'value_0', 'value_1', 'value_2'}
```
Добавление элемента (которого нет в множестве):
```
example.add('value_3')
```
Удаление элемента, если такого элемента нет, то данный метод вызовет ошибку:
```
example.remove('value_3')
```
Метод удаления элемента, даже если его нет. Этот метод игнорирует ошибку, если элемента нет:
```
example.discard('value_3')
```
Метод очистки множества:
```
example.celar()
```
Работа со множествами.

```
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
```
Копирование множества:
```
c = a.copy() # c = {1, 2, 3, 5, 8}
```
Объединение множеств:
```
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
```
Пересечение множеств:
```
i = a.intersection(b) # i = {2, 5, 8}
```
```
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
```
Заморозка множества:
```
f = frozenset(a) # f = ({1, 2, 3, 5, 8})
```
### Списки

Списки являются ссылочным типом. Т.е. например:
```
list_1 = [1, 2 ,3]
list_2 = list_1     # list_2 = [1, 2 ,3]

list_1[0] = 123       # list_1 = [123, 2, 3], list_2 = [123, 2 ,3]

list_2[1] = 222     # list_1 = [123, 222, 3], list_2 = [123, 222, 3]
```
Удаление элемента списка:
```
list_1.pop()    # Если не указан аргумент, удаляет последний элемент
```
Добавление нового элемента:
```
list_1.insert(<pos>, <value>)
```
Добавление нового элемента в конец:
```
list_1.append(<value>)
```

### Включения
```
my_list = [x for x in range(1, 101) if (x % 10 == 3) or (x % 10 == 6)]

print(my_list)
```

Здесь:
    _x_ - Какой элемент взять
    _for x in range(1, 101)_ - Стандартное описание как в _for_
    _if (x % 10 == 3) or (x % 10 == 6)_ - Условие, при котором включаем элементы в список (необязательное)




Byte of Python
Stepik
