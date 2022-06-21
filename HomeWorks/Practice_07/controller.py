import view as v
import data
import csv_worker as csvW

def controller_main():
    csv_path = 'GB_Python\HomeWorks\Practice_07\phone_book.csv'
    program = True
    v.preview()
    if csvW.found_csv(csv_path):
        v.file_found()
        data.set_contacts(csvW.csv_read(csv_path))
    else:
        v.file_not_found()
        csvW.csv_write_contacts(data.get_contacts(), csv_path)
    while program:
        v.main_menu()
        choice = v.main_menu_choice()
        if choice == '1':
            csvW.csv_add(data.add_contact(v.add_contact_first_name(), v.add_contact_last_name(), v.add_contact_phone()), csv_path)
            continue
        if choice == '2':
            data.set_contacts(csvW.csv_read(csv_path))
            data.del_contact(v.del_contact())
            csvW.csv_write_contacts(data.get_contacts(), csv_path)
            continue
        if choice == '3':
            v.print_contacts(csvW.csv_read(csv_path))
            continue
        if choice == '4':
            data.set_contacts(csvW.csv_read(csv_path))
            v.find_contact(data.get_contacts())
            continue
        if choice == '5':
            program = False
            continue