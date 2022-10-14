# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока, 
# делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента 
# достаются сделавшему последний ход. Сколько конфет нужно взять первому 
# игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

gamer1 = input('Введите имя первого игрока: ')
gamer2 = input('Введите имя второго игрока: ')

# формируем очередность игроков 
list_gamers = [gamer1, gamer2]
list_gamers[0] = random.choice(list_gamers)
if list_gamers[0] == gamer1:
    list_gamers[1] = gamer2
else: list_gamers[1] = gamer1
print('Играют в Конфеты: ', gamer1, ' и ', gamer2, '. Первым будет ходить - ', list_gamers[0])
print('За ход можно взять не больше 28 конфет')

# проводим раунд и передаем ход другому игроку
def move_candy(move_g, rest):
    if rest == 0: 
        return move_g
    print('Игрок', list_gamers[move_g], ': возьми конфет:')
    count_candy = int(input())
    if count_candy > 28 or count_candy < 0 or count_candy > rest:
        count_candy = int(input('Неверное число, попробуй еще раз:'))
    rest_candy = rest - count_candy
    move_g += 1
    print('Остаток конфер на столе: ', rest_candy) 
    move_candy(move_g%2, rest_candy)
  
# играем
rest_candy = 202
print('Остаток конфер на столе: ', rest_candy)
move_gamer = 0
# while rest_candy > 0: 
move_candy(move_gamer, rest_candy)

print('Победил ', list_gamers[move_gamer%2])