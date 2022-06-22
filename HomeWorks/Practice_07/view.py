
# Функция отображения основного меню програмы
def main_menu():
    main_menu_text = '\
_______________\n\
\__Main menu__/\n\
1. Add contact\n\
2. Delete contact\n\
3. View contacts\n\
4. Find contact\n\
5. Exit\n\
---------------'
    print(main_menu_text)

# Функция вывода в консоль всех контактов
# Нумерация автоматическая через enumerate
def print_contacts(contacts):
    print('\
___________________\n\
\__View contacts__/')
    for i, j in enumerate(contacts):
        print(f'{i + 1}. {j["First name"]} {j["Last name"]} {j["Phone"]}')

# Функция поиска контакта
def input_find_contact():
    print('\__Find contact__/')
    first_name = input('First name: ')
    last_name = input('Last name: ')
    return first_name, last_name

def print_find_contact(contacts):
    if len(contacts) > 0:
        print('--find--')
        for element in contacts:
            print(f'{element["count"]}. {element["First name"]} {element["Last name"]}\n{element["Phone"]}')
    else:
        print('---\nNot found!')

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