# 2. Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
    
#     *Пример:* 
    
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

li = [1, 5, 2, 3, 4, 6, 1, 7]
posl = [li[0]]
[posl.append(li[i]) for i in range(1, len(li)) if li[i] > posl[-1]]
print(posl)