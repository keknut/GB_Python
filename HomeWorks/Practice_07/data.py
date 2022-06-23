# Переменная содержит данные тестового дата-сета
contacts = [{   'First name' : 'John',
                'Last name' : 'Connor',
                'Phone' : '+79012345678'},
            {   'First name' : 'Bruce',
                'Last name' : 'Nolan',
                'Phone' : '5550123'},
            {   'First name' : 'Ghost',
                'Last name' : 'Busters',
                'Phone' : '5552368'},
            {   'First name' : 'Karl',
                'Last name' : 'T-800',
                'Phone' : '+18885121984'}]

# Функция добавляет новый контакт в переменную contacts
# Вход:
#   -first_name
#   -last_name
#   -Phone
# Возвращает:
#   Словарь с новым контактом
def add_contact(first_name, last_name, phone):
    global contacts
    new_contact = {'First name' : first_name,
                    'Last name' : last_name,
                    'Phone' : phone}
    contacts.append(new_contact)
    new_contact = [new_contact]
    return new_contact

def find_contact(first_name, last_name):
    result = []
    count = 1
    for i in contacts:
        if i['First name'] == first_name or i['Last name'] == last_name:
            result.append({
                'count' : count,
                'First name' : i['First name'],
                'Last name' : i['Last name'],
                'Phone' : i['Phone']})
        count += 1
    return result

def del_contact(id):
    global contacts
    try:
        contacts.pop(id - 1)
        return True
    except IndexError:
        print('This contact is not in the database.')

def get_contacts():
    global contacts
    return contacts

def set_contacts(data):
    global contacts
    contacts = data