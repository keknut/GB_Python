import csv
from pathlib import Path

def check_csv(csv_path):
    try:
        file = open(csv_path, 'r')
        file.close()
        return True
    except FileNotFoundError:
        return False

def csv_add(data, csv_path):
    with open(csv_path, 'a') as file:
        writer = csv.DictWriter(file, fieldnames = list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(data)

def csv_read(csv_path):
    employees = []
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append(row)
    return employees

def csv_write_contacts(data, csv_path):
    with open(csv_path, 'w') as file:
        writer = csv.DictWriter(file, fieldnames = list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def csv_path():
    return Path(Path.cwd(), 'GB_Python', 'HomeWorks', 'Practice_08', 'DB_employees.csv')
