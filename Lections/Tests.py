dictionary = {  'up':'up',
                'left':'left',
                'right':'right',
                'bottom':'bottom'   
}
path = "test.txt"

with open(path, 'w') as dataWrite:
    for i in dictionary.items():
        dataWrite.write(f'{i}\n')

with open(path, 'r') as dataRead:
    allData = dataRead.read()
print(allData)