"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


import random


def rec_regen(count, num):
    print(f'Попытка: {coun}')
    answer = int(input('Введите число от 0 до 100: '))
    if count == 10 or answer == num:
        if answer == num:
            print('Верно!')
        print(f'Загаданное число: {numb')
    else:
        if answer > numb:
            print(f'Введите меньше')
        else:
            print(f'Введите больше')
        recur_method(count + 1, num)


rec_regen(1, random.randint(0, 100))