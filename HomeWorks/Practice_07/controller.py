import view as v
import data
import csv_worker as csvW
from pathlib import Path

def controller_main():
    # Путь к csv файлу
    csv_path = Path(Path.cwd(), 'phone_book.csv')
    
    # Пока переменная True, программа исполняется
    program = True
    
    # Выводит на консоль превью 
    v.preview()

    # Здесь попытка открыть файл с базой контактов
    # Если не находит файл, создаёт новый с тестовым дата-сетом
    if csvW.found_csv(csv_path):
        v.file_found()
        data.set_contacts(csvW.csv_read(csv_path))
    else:
        v.file_not_found()
        csvW.csv_write_contacts(data.get_contacts(), csv_path)

    # Основное тело программы.
    while program:
        
    # Выводит на консоль главное меню
        v.main_menu()
        # Опрашивает пользователя, какой пункт меню он выбирает
        choice = v.main_menu_choice()

        # Пункт меню "Добавить контакт"
        # Добавляет контакт сразу в файл csv 
        if choice == '1':
            csvW.csv_add(data.add_contact(v.add_contact_first_name(), v.add_contact_last_name(), v.add_contact_phone()), csv_path)
            continue

        # Пункт меню "Удаление контакта"
        # Считывает файл csv, удаляет необходимый контакт по id
        # Перезаписывает файл с новой базой
        if choice == '2':
            data.set_contacts(csvW.csv_read(csv_path))
            data.del_contact(v.del_contact())
            csvW.csv_write_contacts(data.get_contacts(), csv_path)
            continue

        # Пункт меню "Посмотреть контакты"
        # Считывает все контакты из файла csv и выводит на консоль
        if choice == '3':
            v.print_contacts(csvW.csv_read(csv_path))
            continue

        # Пункт меню "Найти контакт"
        # Читает файл csv, ищет совпадения, выводит на консоль
        if choice == '4':
            data.set_contacts(csvW.csv_read(csv_path))
            name = v.input_find_contact()
            v.print_find_contact(data.find_contact(name[0], name[1]))
            continue

        # Пункт меню "Выход"
        # Присваивает переменной False и программа выходит из цикла
        if choice == '5':
            program = False
            continue