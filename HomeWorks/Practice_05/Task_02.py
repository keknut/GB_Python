# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому
# игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота "интеллектом"

# from tkinter import *

# def clicked():
#     lbl.configure(text='Я же просил!')

# window = Tk()
# window.title('Игра в конфеты')
# window.geometry('500x500')

# lbl = Label(window, text="Привет")  
# lbl.grid(column=0, row=0)

# btn = Button(window, text="Не нажимать!", command=clicked)
# btn.grid(column=0, row=1)

# window.mainloop()

import random

candy_sum = 2021
player_list = ['player 1', 'player 2']
first_player = random.choice(player_list)
player_turn = 0
flag = True

print(f'{player_list[0]} vs {player_list[1]}\nFIGHT!\n')

if first_player == player_list[0]:
    second_player = player_list[1]
else:
    second_player = player_list[0]

while candy_sum > 0:
    if flag:
        player_turn = int(input(f'Candys: {candy_sum}\nTurn: {first_player}\nInput candys: '))
        flag = False
        candy_sum -= player_turn
        print('------')
        if candy_sum <= 0:
            print(f'{first_player} win!')
    else:
        player_turn = int(input(f'Candys: {candy_sum}\nTurn: {second_player}\nInput candys: '))
        flag = True
        candy_sum -= player_turn
        print('------')
        if candy_sum <= 0:
            print(f'{second_player} win!')