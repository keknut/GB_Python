import csv

def csv_write_contacts(data):
    with open('GB_Python\Practice\phone_book.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames = list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def csv_add(data):
    with open('GB_Python\Practice\phone_book.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames = list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
        for row in data:
            writer.writerow(row)


def csv_read():
    contacts = []
    with open('GB_Python\Practice\phone_book.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            contacts.append(row)
    return contacts

contacts = [{   'First name' : 'Jhon',
                'Last name' : 'Smith',
                'Phone' : '+79012345678'},
            {   'First name' : 'Simon',
                'Last name' : 'Red',
                'Phone' : '+79012312312'},
            {   'First name' : 'Samantha',
                'Last name' : 'Scarlett',
                'Phone' : '+79'},
            {   'First name' : 'Jhon',
                'Last name' : 'Scarlett',
                'Phone' : '+7987'}]

new_contact = [{   'First name' : 'Jhon',
                'Last name' : 'Connor',
                'Phone' : '+7901222222'}]

csv_write_contacts(contacts)
csv_add(new_contact)
print(csv_read())