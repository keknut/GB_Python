import csv

def csv_add(data, csv_path):
    with open(csv_path, 'a') as file:
        writer = csv.DictWriter(file, fieldnames = data.keys(), quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(data)

def csv_read(csv_path):
    contacts = []
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            contacts.append(row)
    return contacts


data = {
    'Name' : 'John',
    'Surname' : 'Connor',
    'Age' : '14',
    'Phone' : '+79012345678',
    'Job title' : 'Savior',
    'Salary' : '150'
    }

csv_path = 'GB_Python\Practice\Tests.csv'

csv_add(data, csv_path)
print(csv_read(csv_path))