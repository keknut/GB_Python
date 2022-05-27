# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому
# игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота "интеллектом"

import random

def main_menu():
    text = '1. Player vs Player\n2. Player vs Bot\n3. Exit\n'
    choise = input(f'------\n{text}')
    return choise

def pvp_names():
    print('------')
    first_player = input('Enter the name of the First Player. The default name is Player 1:\n')
    second_player = input('Enter the name of the Second Player. The default name is Player 2:\n')
    if first_player != '':
        player_list[0] = first_player
    if second_player != '':
        player_list[1] = second_player
    return player_list

def pvb_names():
    bots_name = ['Anna', 'Maria', 'David', 'John', 'Simon', 'Alfred', 'Alex']
    player_list[1] = random.choices(bots_name)

    first_player = input('Enter the name of the Player. The default name is Player 1:\n')
    if first_player != '':
        player_list[0] = first_player
    return player_list

def bot_ai(candy_sum, max_turn, first_turn):
    if first_turn:
        if random.randint(1,9) > 6:
            return candy_sum % max_turn
        else:
            return classic_bot_turn(max_turn)
    else:
        return classic_bot_turn(max_turn)

def classic_bot_turn(max_turn):
    return random.randint(1, max_turn)

def pvp_turns(candy_sum, player):
    candy_sum -= int(input(f'Candys: {candy_sum}\nTurn: {player}\nInput candys: '))
    print('------')
    if candy_sum <= 0:
        print(f'{player} win!')
    return candy_sum

def game(candy_sum, player_list):
    

candy_sum = 2021
player_list = ['Player 1', 'Player 2']


player_turn = 0
flag = True
first_bot_turn = False
loop = True

while loop:
    choice = main_menu()
    if choice == '1':
        player_list = pvp_names()
        first_player = random.choice(player_list)
        if first_player == player_list[0]:
            second_player = player_list[1]
        else:
            second_player = player_list[0]
        print(f'{player_list[0]} vs {player_list[1]}\nFIGHT!\n')
    if choice == '2':

    if choice == '3':
        loop = False


if first_player == player_list[0]:
    second_player = player_list[1]
else:
    second_player = player_list[0]
    first_bot_turn = True

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