import csv

def csv_write_contacts(data, csv_path):
    with open(csv_path, 'w') as file:
        writer = csv.DictWriter(file, fieldnames = list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def csv_add(data, csv_path):
    with open(csv_path, 'a') as file:
        writer = csv.DictWriter(file, fieldnames = list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
        for row in data:
            writer.writerow(row)

def csv_read(csv_path):
    contacts = []
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            contacts.append(row)
    return contacts

def found_csv(csv_path):
    try:
        file = open(csv_path, 'r')
        file.close()
        return True
    except FileNotFoundError:
        return False