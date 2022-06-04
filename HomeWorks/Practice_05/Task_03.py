# Создайте программу для игры в "Крестики-нолики".

from tkinter import *

from GB_Python.HomeWorks.Practice_05.Task_02 import game

window = Tk()
window.title('Крестики-Нолики')
game_run = True
field = [] #переменная хранит в себе кнопки в двумерном списке 
player_turns = True #переменная для передачи хода другому игроку

# Функция нажатия на кнопку new game
# Обнуляет все кнопки, перекрашивает в цвет по умолчанию
# Обнуляет ход игроков, чтобы крестики начинали всегда первыми
def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global player_turns
    player_turns = True

# Функция нажатия на кнопку.
# При нажатии на кнопку, фонкуия определяет чей сейчас ход
# и отрисовывет на кнопке необходимый символ 'X' или 'O'
# Проверяет. не победил ли текущий игрок.
# Если победил, красит нужные кнопки в зелёный цвет. 
# Затем передаёт ход другому игроку
def click(row, col):
    global player_turns
    if game_run and field[row][col]['text'] == ' ':
        if player_turns:
            field[row][col]['text'] = 'X'
            check_win('X')
            player_turns = False
        else:
            field[row][col]['text'] = 'O'
            check_win('O')
            player_turns = True

# Функция проверяет, победил ли игрок.
# Проверяет линии, обращаясь к функции check_line
# Если да, закрашивает необходимые кнопки в зелёный.
def check_win(smb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)

# Подфункция проверки линий. Проверяет, есть ли три одинаковых символа в один ряд.
# Если да, красит нужные кнопки в зелёный.
def check_line(a1,a2,a3,smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'green'
        global game_run
        game_run = False

# Цикл заполняет окно кнопками без текста или маркеров.
for row in range(3):
    line = []
    for col in range(3):
        button = Button(window, text=' ', width=4, height=2, 
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)

# Создание кнопки new_game
new_button = Button(window, text='new game', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
window.mainloop()