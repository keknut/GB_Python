
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

# Функция поиска контакта.
# Спрашивает у пользователя Имя и Фамилию
# Одно из полей может быть пустым. Чувствительна к регистру.
def input_find_contact():
    print('\__Find contact__/')
    first_name = input('First name: ')
    last_name = input('Last name: ')
    return first_name, last_name

# Выводит на консоль найденные контакты и их id в базе.
def print_find_contact(contacts):
    if len(contacts) > 0:
        print('--find--')
        for element in contacts:
            print(f'{element["count"]}. {element["First name"]} {element["Last name"]}\n{element["Phone"]}')
    # Если контакт не найден, выводит в консоль соответствующее сообщение
    else:
        print('---\nNot found!')

# Функция спрашивает пользователя имя при добавлении нового контакта и возвращает его.
def add_contact():
    first_name = input('First name: ')
    last_name = input('Last name: ')
    phone = input('Phone: ')
    new_contact = {
        'First name' : first_name,
        'Last name' : last_name,
        'Phone' : phone
    }
    return new_contact

# Функция спрашивает id удаляемого контакта и возвращает его
def del_contact():
    return int(input('\
____________________\n\
\__delete contact__/\n\
Input id: '))

# Выводит на консоль статус удаляемого контакта.
# В случае успеха пишет, что контакт удалён
# В случае неудачи, пишет что контакт не найден
def del_contact_status(status):
    if status:
        print('Contact deleted.')
    else:
        print('This contact is not in the database.')

# Функция выбора пункта меню. Возвращает введённое пользователем значение
def main_menu_choice():
    return input()

# Превью программы
def preview():
    print('------\n\
Starting program...\n\
csv file search...')

# Сообщение в консоль, если файл csv был найден
def file_found():
    print('File found!')

# Сообщение в консоль, если файл csv не был найден
def file_not_found():
    print('File not found!\n\
Creating a file with a test data set.')