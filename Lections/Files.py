colors = ['red', 'green', 'blue']
path = 'file.txt'
data = open(path, 'a')
data.writelines(colors)
data.close()