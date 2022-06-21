def main_menu():
    main_menu_text = '\
------\n\
\__Main menu__/\n\
1. Add contact\n\
2. Delete contact\n\
3. View contacts\n\
4. Find contact\n\
5. Exit\n\
------'
    print(main_menu_text)

def print_contacts(contacts):
    print('---\n\__View contacts__/')
    for i, j in enumerate(contacts):
        print(f'{i + 1}. {j["First name"]} {j["Last name"]} {j["Phone"]}')

def find_contact(contacts):
    print('Find contact:')
    first_name = input('First name: ')
    last_name = input('Last name: ')
    print('--Found--')
    find = True
    count = 1
    for i in contacts:
        if i['First name'] == first_name or i['Last name'] == last_name:
            print(f"{count}. {i['First name']} {i['Last name']}\n{i['Phone']}\n----")
            find = False
        count += 1
    if find:
        print('Not found!')

def add_contact_first_name():
    first_name = input('First name: ')
    return first_name

def add_contact_last_name():
    last_name = input('Last name: ')
    return last_name
    
def add_contact_phone():
    phone = input('Phone: ')
    return phone

def del_contact():
    return int(input('Input id: '))

def main_menu_choice():
    return input()

def preview():
    print('------\n\
Starting program...\n\
csv file search...')

def file_found():
    print('File found!')

def file_not_found():
    print('File not found!\n\
Creating a file with a test data set.')