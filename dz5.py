'''
1. Напишите программу, удаляющую из текста все слова, содержащие ""абв""
'''

with open('DZ5(1).txt', 'r', encoding='utf-8') as f:
    a = ' '.join(filter(lambda x: 'абв' not in x, str(f.read()).split()))
with open('DZ5(1.2).txt', 'w', encoding='utf-8') as q:
    q.write(a)

'''
2. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
'''

import random


def rnd_turn():
    n = random.randint(0, 1)
    if n == 0:
        print('Первым ходит игрок')
    else:
        print('Первым ходит бот')
    return n


def func_player(matches):
    n = 29
    while n > 28 or n < 0:
        n = input('Введите сколько хотите взять конфет: ')
        if n.isdigit():
            n = int(n)
            if n > 28 or n < 0:
                print(f'Вы вязли недопустимое количества конфет! Введите число от 1 до 28: ')
            if n > matches:
                print(f'Вы взяли больше чем осталось конфет!')
                n = 29
        else:
            print(f'Вы ввели недопустимые символы. Введите число от 1 до 28: ')
            n = 29
    return n


def func_bot(matches):
    n = matches % 28
    if n == 0:
        n = random.randint(1, 28)
    return n


matches = 100
turn = rnd_turn()

while matches != 0:
    if turn % 2 == 0:
        print(f'\nХодит игрок. Осталось конфет: {matches}')
        n = func_player(matches)
    elif turn % 2 == 1:
        print(f'\nХодит бот. Осталось конфет: {matches}')
        n = func_bot(matches)
        print('Бот взял', n, 'конфет')
    matches -= n
    if matches == 0:
        if turn % 2 == 0:
            print(f'Победил игрок!')
        else:
            print(f'Победил бот!')
    turn += 1

'''
3. Создайте программу для игры в ""Крестики-нолики"".
'''

board = list(range(1, 10))


def draw_board(x):
    print("-" * 13)
    for i in range(3):
        print("|", board[i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        if player_answer.isdigit():
            player_answer = int(player_answer)
        else:
            print("Некорректный ввод. Введите число?")
            continue
        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_token
            valid = True
        else:
            print("Эта клетка уже занята!")
    else:
        print("Некорректный ввод. Введите число от 1 до 9.")


def check_win(x):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_coord:
        if x[i[0]] == x[i[1]] == x[i[2]]:
            return x[i[0]]
    return False


def main(x):
    counter = 0
    win = False
    while not win:
        draw_board(x)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(x)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)


main(board)

'''
4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
'''

inf = input('Ввод: ')
count = 1
line = ''
for i in range(len(inf) - 1):
    if inf[i] == inf[i + 1]:
        count += 1
        if count > 8:
            line += str(count) + inf[i]
            count = 0
            continue
    else:
        line += str(count) + inf[i]
        count = 1
line += str(count) + inf[i + 1]
print(line)
