import view
import bd
import input_data


def run():
    view.preview()
    if bd.check_csv(bd.csv_path()):
        view.file_found()
    else:
        view.file_not_found()
        bd.csv_write_contacts(bd.get_bd(), bd.csv_path())

    while True:
        user_select = view.main_menu()
        if user_select == '1':
            bd.csv_add(input_data.input_employee())
        if user_select == '2':
            bd.set_bd(bd.csv_read(bd.csv_path()))
            if bd.del_employee(input_data.input_del_employee()):
                print('Employee removed from database.')
                bd.csv_write_contacts(bd.get_bd(), bd.csv_path())
            else:
                print('The employee is not in the database.')
        if user_select == '3':
            view.print_employees(bd.csv_read(bd.csv_path()))
        if user_select == '4':
            view.end_program()
            break