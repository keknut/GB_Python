import requests

def get_valutes_name(link):
    list = []
    data = requests.get(link).json()
    for elem in data['Valute'].values():
        list.append(elem['Name'])
    return list

def get_valutes_char_code(link, name):
    data = requests.get(link).json()
    for elem in data['Valute'].values():
        if elem['Name'] == name:
            return elem['CharCode']

def get_valutes_value(link, char_code):
    data = requests.get(link).json()
    return data['Valute'][char_code]['Value']