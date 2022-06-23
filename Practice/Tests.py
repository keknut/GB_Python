dict = []
print(len(dict))
dict.append(1)
dict.append(1)
dict.append(1)
print(len(dict))
try:
    dict.pop(5)
except IndexError:
    print('This contact is not in the database.')