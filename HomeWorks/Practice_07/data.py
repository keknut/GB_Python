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

def add_contact(first_name, last_name, phone):
    global contacts
    new_contact = {'First name' : first_name,
                    'Last name' : last_name,
                    'Phone' : phone}
    contacts.append(new_contact)
    new_contact = [new_contact]
    return new_contact

def del_contact(id):
    global contacts
    contacts.pop(id - 1)

def get_contacts():
    global contacts
    return contacts

def set_contacts(data):
    global contacts
    contacts = data