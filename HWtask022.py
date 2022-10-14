# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока, 
# делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента 
# достаются сделавшему последний ход. Сколько конфет нужно взять первому 
# игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
game_mode = int(input('Выберите режим игры: 1 - human, 2 - bot, 3 - skynet: '))
gamer1 = input('Введите имя первого игрока: ')
if game_mode == 1: gamer2 = input('Введите имя второго игрока: ')
if game_mode == 2: gamer2 = 'Bot'
if game_mode == 3: gamer2 = 'Skynet'

# формируем очередность игроков 
list_gamers = [gamer1, gamer2]
list_gamers[0] = random.choice(list_gamers)
if list_gamers[0] == gamer1:
    list_gamers[1] = gamer2
else: list_gamers[1] = gamer1
print('Играют в Конфеты: ', gamer1, ' и ', gamer2, '. Первым будет ходить - ', list_gamers[0])
print('За ход можно взять не больше 28 конфет')

# играем
rest_candy = 100
rest = 28
move_g = 0
print('Остаток конфет на столе: ', rest_candy)
while rest_candy>0:
    print('Ход', move_g+1,'- Игрок', list_gamers[move_g%2], 'возьми конфет:')
    if list_gamers[move_g%2] == 'Bot':
        count_candy = random.randint(1, rest)
        print(count_candy)
    elif list_gamers[move_g%2] == 'Skynet':
        if rest_candy < 29: count_candy = rest_candy
        elif 29 < rest_candy < 57: count_candy = rest_candy-29
        elif 57 < rest_candy < 85: count_candy = rest_candy-28-29
        else: count_candy = random.randint(1, rest)
        print(count_candy)
    else:    
        count_candy = int(input())
        while count_candy > 28 or count_candy < 0 or count_candy > rest_candy:
            count_candy = int(input('Неверное число, попробуй еще раз: '))
    rest_candy -= count_candy
    rest = min(29, rest_candy)
    print('Остаток конфет на столе: ', rest_candy)
    move_g +=1
print('Победил игрок', list_gamers[move_g%2-1])