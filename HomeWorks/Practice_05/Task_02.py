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


# Функция основного меню.
# Выводит в консоль основное меню игры
def main_menu():
    text = '1. Player vs Player\n2. Player vs Bot\n3. Exit\n'
    choise = input(f'------\n{text}')
    return choise

# Функция ввода имени двух игроков.
# Если не ввести имя.будет присвоено имя по умолчанию.
def pvp_names():
    player_list = ['Player 1', 'Player 2']
    print('------')
    first_player = input('Enter the name of the First Player. The default name is \'Player 1\':\n')
    second_player = input('Enter the name of the Second Player. The default name is \'Player 2\':\n')
    if first_player != '':
        player_list[0] = first_player
    if second_player != '':
        player_list[1] = second_player
    return player_list

# Функция ввода имени при игре с ботом.
# Имя боту присваивается случайное из списка.
def pvb_names():
    player_list = ['Player 1', 'Player 2']
    bots_name = ['Anna', 'Maria', 'David', 'John', 'Simon', 'Alfred', 'Alex']
    player_list[1] = ''.join(random.choices(bots_name)).replace('[', '').replace('\'', '')

    first_player = input('Enter the name of the Player. The default name is \'Player 1\':\n')
    if first_player != '':
        player_list[0] = first_player
    return player_list

# Функция первого хода для бота.
# С вероятностью 30% сходит неправильно
# и бота можно будет выиграть.
def first_bot_turn(candy_sum, max_turn):
    if random.randint(1,9) > 6:
        return candy_sum % max_turn
    else:
        return classic_bot_turn(max_turn)

# Функция лассического хода бота.
# Просто случайное число от 1 до максимального возможного хода.
def classic_bot_turn(max_turn):
    return random.randint(1, max_turn)

# Функция ходов в игре.
# принимает на вход:
#         -текущее количество конфет
#         -имя игрока
#         -настройки бота
# *Player vs Player:
#     Выводит в консоль текущее количество конфет и спрашивает игрока,
#     сколько конфет в этот ход он забирает.
# *Player vs Bot:
#     Выводи на консоль текущее количество конфет.
#     Если ходит бот, выводит как он сходил.
#     Если игрок, выводит текущее количество конфет и как игрок хочет сходить.
def game_turns(candy_sum, player, bot_settings):
    turn = 0
    if bot_settings['bot'] and bot_settings['bot_turn']:
        if bot_settings['first_turn']:
            turn = first_bot_turn(candy_sum, max_turn=28)
            print(f'Candys: {candy_sum}\nTurn: {player}\nInput candys: {turn}')
            candy_sum -= turn
        else:
            turn = classic_bot_turn(max_turn=28)
            print(f'Candys: {candy_sum}\nTurn: {player}\nInput candys: {turn}')
            candy_sum -= turn
    else:
        candy_sum -= int(input(f'Candys: {candy_sum}\nTurn: {player}\nInput candys: '))
    print('------')
    if candy_sum <= 0:
        print(f'{player} win!')
    return candy_sum

# Функция игры.
# Принимает на вход:
#     -текущее количество конфет
#     -имя первого игрока
#     -имя второго игрока
#     -настройки бота
def game(candy_sum, first_player, second_player, bot_settings):
    turns = True
    while candy_sum > 0:
        if turns:
            if bot_settings['bot'] and bot_settings['bot_turn']:
                candy_sum = game_turns(candy_sum, first_player, bot_settings)
                if bot_settings['first_turn']:
                    bot_settings['first_turn'] = False
                    bot_settings['bot_turn'] = False
                else:
                    bot_settings['bot_turn'] = False
            else:
                candy_sum = game_turns(candy_sum, first_player, bot_settings)
                if bot_settings['bot']:
                    bot_settings['bot_turn'] = True
            if candy_sum <= 0:
                continue
            turns = False
            continue
        else:
            if bot_settings['bot'] and bot_settings['bot_turn']:
                candy_sum = game_turns(candy_sum, second_player, bot_settings)
                bot_settings['bot_turn'] = False
            else:
                candy_sum = game_turns(candy_sum, second_player, bot_settings)
                if bot_settings['bot']:
                    bot_settings['bot_turn'] = True
            if candy_sum <= 0:
                continue
            turns = True
            continue

    

candy_sum = 2021 #изначальное количество конфет
player_list = ['Player 1', 'Player 2'] #имена игроков по умолчанию
main_menu_loop = True #переменная выхода из игры
bot_settings = { #настройки бота
    'bot' : False, #настройка наличия бота в игре
    'first_turn' : True, #первый ход у бота
    'first_player' : True, #первый игрок бот
    'bot_turn' : True #нужна для определения, ходит ли сейчас бот
    }

# Основное меню игры.
# Первый ход определяется случайно при любом режиме игры
while main_menu_loop:
    choice = main_menu()

    if choice == '1':
        player_list = pvp_names()
        first_player = random.choice(player_list)
        if first_player == player_list[0]:
            second_player = player_list[1]
        else:
            second_player = player_list[0]
        print(f'{player_list[0]} vs {player_list[1]}\nFIGHT!\n')
        game(candy_sum, first_player, second_player,bot_settings)

    if choice == '2':
        bot_settings['bot'] = True
        player_list = pvb_names()
        first_player = random.choice(player_list)
        if first_player == player_list[0]:
            second_player = player_list[1]
            bot_settings['first_turn'] = False
            bot_settings['first_player'] = False
            bot_settings['bot_turn'] = False
        else:
            second_player = player_list[0]
        print(f'{player_list[0]} vs {player_list[1]}\nFIGHT!\n')
        game(candy_sum, first_player, second_player,bot_settings)

    if choice == '3':
        main_menu_loop = False
        continue