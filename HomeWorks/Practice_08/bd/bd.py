employees = [{  'Name' : 'John',
                'Surname' : 'Connor',
                'Age' : '14',
                'Phone' : '+79012345678',
                'Job title' : 'Savior',
                'Salary' : '150'
            },
            {   'Name' : 'Bruce',
                'Surname' : 'Nolan',
                'Age' : '35',
                'Phone' : '5550123',
                'Job title' : 'God',
                'Salary' : 'Infinity'
            },
            {   'Name' : 'Ghost',
                'Surname' : 'Busters',
                'Age' : 'NaN',
                'Phone' : '5552368',
                'Job title' : 'Ghostbusters',
                'Salary' : '600'
            },
            {   'Name' : 'Karl',
                'Surname' : 'T-800',
                'Age' : '46',
                'Phone' : '+18885121984',
                'Job title' : 'Terminator',
                'Salary' : '2000'
            }]

def set_bd(data):
    global employees
    employees = data

def get_bd():
    global employees
    return employees

def add_employee(new_employee):
    global employees
    employees.append(new_employee)

def del_employee(id):
    global employees
    try:
        employees.pop(id - 1)
        return True
    except IndexError:
        return False