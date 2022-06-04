# zip

name_list = ['Q', 'W', 'E', 'R', 'T']
index_list = [1, 2, 3, 4, 5]
name_index_list = list(zip(name_list, index_list))
print(name_index_list)

for i, j in zip(name_list, index_list):
    print(i, j)