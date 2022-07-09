import tkinter
from tkinter.ttk import Combobox
import time

import requests

def click():
    global link

    text.set(get_valutes_value(link, get_valutes_char_code(link, combo.get())))
    lbl.configure(textvariable=text)

    print(combo.get())

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

link = 'https://www.cbr-xml-daily.ru/daily_json.js'

window = tkinter.Tk()
window.title('Kek')
window.geometry('400x250')

text = tkinter.StringVar()
text.set('Hello where!')

lbl = tkinter.Label(window, textvariable=text)
lbl.grid(column=0, row=0)

btn = tkinter.Button(window, text="Don't click!", bg='pink', fg='red',activebackground='red', command=click)
btn.grid(column=0, row=1)

combo = Combobox(window, values=get_valutes_name(link))
combo.current(1)
combo.grid(column=0, row=2)

text_repeat = tkinter.StringVar()
text_repeat.set('Current')

lbl_ping = tkinter.Label(window, textvariable=text_repeat)
lbl_ping.grid(column=0, row=3)

loop = True

valutes = []

for valute in get_valutes_name(link):
    valutes.append(valute)

for valute in valutes:
    discount = get_valutes_value(link, get_valutes_char_code(link, valute))
    time.sleep(5)
    text_repeat.set(f'{valute}: {discount}')
    time.sleep(5)


window.mainloop()

# valute = {
#     'AUD': {'ID': 'R01010', 'NumCode': '036', 'CharCode': 'AUD', 'Nominal': 1, 'Name': 'Австралийский доллар', 'Value': 36.8358, 'Previous': 36.8062},
#     'AZN': {'ID': 'R01020A', 'NumCode': '944', 'CharCode': 'AZN', 'Nominal': 1, 'Name': 'Азербайджанский манат', 'Value': 31.3667, 'Previous': 31.3869},
#     'GBP': {'ID': 'R01035', 'NumCode': '826', 'CharCode': 'GBP', 'Nominal': 1, 'Name': 'Фунт стерлингов Соединенного королевства', 'Value': 65.2785, 'Previous': 65.3846},
#     'AMD': {'ID': 'R01060', 'NumCode': '051', 'CharCode': 'AMD', 'Nominal': 100, 'Name': 'Армянских драмов', 'Value': 13.0515, 'Previous': 12.9881},
#     'BYN': {'ID': 'R01090B', 'NumCode': '933', 'CharCode': 'BYN', 'Nominal': 1, 'Name': 'Белорусский рубль', 'Value': 21.064, 'Previous': 21.0775},
#     'BGN': {'ID': 'R01100', 'NumCode': '975', 'CharCode': 'BGN', 'Nominal': 1, 'Name': 'Болгарский лев', 'Value': 28.6085, 'Previous': 28.7024},
#     'BRL': {'ID': 'R01115', 'NumCode': '986', 'CharCode': 'BRL', 'Nominal': 1, 'Name': 'Бразильский реал', 'Value': 10.2881, 'Previous': 10.3595},
#     'HUF': {'ID': 'R01135', 'NumCode': '348', 'CharCode': 'HUF', 'Nominal': 100, 'Name': 'Венгерских форинтов', 'Value': 14.028, 'Previous': 14.0131},
#     'HKD': {'ID': 'R01200', 'NumCode': '344', 'CharCode': 'HKD', 'Nominal': 10, 'Name': 'Гонконгских долларов', 'Value': 68.0493, 'Previous': 68.1019},
#     'DKK': {'ID': 'R01215', 'NumCode': '208', 'CharCode': 'DKK', 'Nominal': 10, 'Name': 'Датских крон', 'Value': 75.2167, 'Previous': 75.4675},
#     'USD': {'ID': 'R01235', 'NumCode': '840', 'CharCode': 'USD', 'Nominal': 1, 'Name': 'Доллар США', 'Value': 53.3234, 'Previous': 53.3578},
#     'EUR': {'ID': 'R01239', 'NumCode': '978', 'CharCode': 'EUR', 'Nominal': 1, 'Name': 'Евро', 'Value': 55.964, 'Previous': 55.9886},
#     'INR': {'ID': 'R01270', 'NumCode': '356', 'CharCode': 'INR', 'Nominal': 100, 'Name': 'Индийских рупий', 'Value': 68.2867, 'Previous': 68.3317},
#     'KZT': {'ID': 'R01335', 'NumCode': '398', 'CharCode': 'KZT', 'Nominal': 100, 'Name': 'Казахстанских тенге', 'Value': 11.4721, 'Previous': 11.75},
#     'CAD': {'ID': 'R01350', 'NumCode': '124', 'CharCode': 'CAD', 'Nominal': 1, 'Name': 'Канадский доллар', 'Value': 41.0749, 'Previous': 41.2284},
#     'KGS': {'ID': 'R01370', 'NumCode': '417', 'CharCode': 'KGS', 'Nominal': 100, 'Name': 'Киргизских сомов', 'Value': 67.0723, 'Previous': 67.1131},
#     'CNY': {'ID': 'R01375', 'NumCode': '156', 'CharCode': 'CNY', 'Nominal': 10, 'Name': 'Китайских юаней', 'Value': 80.1826, 'Previous': 80.0483},
#     'MDL': {'ID': 'R01500', 'NumCode': '498', 'CharCode': 'MDL', 'Nominal': 10, 'Name': 'Молдавских леев', 'Value': 27.7107, 'Previous': 27.7638},
#     'NOK': {'ID': 'R01535', 'NumCode': '578', 'CharCode': 'NOK', 'Nominal': 10, 'Name': 'Норвежских крон', 'Value': 53.4153, 'Previous': 53.4417},
#     'PLN': {'ID': 'R01565', 'NumCode': '985', 'CharCode': 'PLN', 'Nominal': 1, 'Name': 'Польский злотый', 'Value': 11.9366, 'Previous': 11.9078},
#     'RON': {'ID': 'R01585F', 'NumCode': '946', 'CharCode': 'RON', 'Nominal': 1, 'Name': 'Румынский лей', 'Value': 11.3684, 'Previous': 11.3363},
#     'XDR': {'ID': 'R01589', 'NumCode': '960', 'CharCode': 'XDR', 'Nominal': 1, 'Name': 'СДР (специальные права заимствования)', 'Value': 71.1014, 'Previous': 71.151},
#     'SGD': {'ID': 'R01625', 'NumCode': '702', 'CharCode': 'SGD', 'Nominal': 1, 'Name': 'Сингапурский доллар', 'Value': 38.3981, 'Previous': 38.4311},
#     'TJS': {'ID': 'R01670', 'NumCode': '972', 'CharCode': 'TJS', 'Nominal': 10, 'Name': 'Таджикских сомони', 'Value': 50.4799, 'Previous': 50.4213},
#     'TRY': {'ID': 'R01700J', 'NumCode': '949', 'CharCode': 'TRY', 'Nominal': 10, 'Name': 'Турецких лир', 'Value': 30.7116, 'Previous': 30.7614},
#     'TMT': {'ID': 'R01710A', 'NumCode': '934', 'CharCode': 'TMT', 'Nominal': 1, 'Name': 'Новый туркменский манат', 'Value': 15.2353, 'Previous': 15.2451},
#     'UZS': {'ID': 'R01717', 'NumCode': '860', 'CharCode': 'UZS', 'Nominal': 10000, 'Name': 'Узбекских сумов', 'Value': 49.236, 'Previous': 49.1909},
#     'UAH': {'ID': 'R01720', 'NumCode': '980', 'CharCode': 'UAH', 'Nominal': 10, 'Name': 'Украинских гривен', 'Value': 18.0589, 'Previous': 18.0641},
#     'CZK': {'ID': 'R01760', 'NumCode': '203', 'CharCode': 'CZK', 'Nominal': 10, 'Name': 'Чешских крон', 'Value': 22.6052, 'Previous': 22.7209},
#     'SEK': {'ID': 'R01770', 'NumCode': '752', 'CharCode': 'SEK', 'Nominal': 10, 'Name': 'Шведских крон', 'Value': 52.4351, 'Previous': 52.469},
#     'CHF': {'ID': 'R01775', 'NumCode': '756', 'CharCode': 'CHF', 'Nominal': 1, 'Name': 'Швейцарский франк', 'Value': 55.5684, 'Previous': 55.1502},
#     'ZAR': {'ID': 'R01810', 'NumCode': '710', 'CharCode': 'ZAR', 'Nominal': 10, 'Name': 'Южноафриканских рэндов', 'Value': 33.4664, 'Previous': 33.3359},
#     'KRW': {'ID': 'R01815', 'NumCode': '410', 'CharCode': 'KRW', 'Nominal': 1000, 'Name': 'Вон Республики Корея', 'Value': 41.0749, 'Previous': 40.9877},
#     'JPY': {'ID': 'R01820', 'NumCode': '392', 'CharCode': 'JPY', 'Nominal': 100, 'Name': 'Японских иен', 'Value': 39.4433, 'Previous': 39.4658}
#     }