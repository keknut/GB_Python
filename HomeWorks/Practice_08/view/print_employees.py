def print_employees(data):
    print('\
____________________\n\
\__View employees__/')
    for i, j in enumerate(data):
        print(f'{i + 1}. {j["Name"]} {j["Surname"]}\n\
Age: {j["Age"]}\n\
Phone: {j["Phone"]}\n\
Job title: {j["Job title"]}\n\
Salary: {j["Salary"]}\n\
--------------------')