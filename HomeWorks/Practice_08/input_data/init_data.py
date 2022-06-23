def input_employee():
    return {
        'Name' : input('______\n\__Input__/\nName: '),
        'Surname' : input('Surname: '),
        'Age' : input('Age: '),
        'Phone' : input('Phone: '),
        'Job title' : input('Job title: '),
        'Salary' : input('Salary: ')}

def input_del_employee():
    return int(input('------\nEnter the ID of the employee to be deleted: '))