

def main_menu():
    main_menu_text = '\
_______________\n\
\__Main menu__/\n\
1. Add employee\n\
2. Delete employee\n\
3. View employees\n\
4. Exit\n\
----------------'

    print(main_menu_text)
    return input('Select operation: ')

def end_program():
    print('Program stop')