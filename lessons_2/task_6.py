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

from random import randrange


def res(count=0, rand_number=randrange(0, 101)):
    if count == 10:
        return rand_number
    user_number = int(input())
    if user_number == rand_number:
        print('win')
        return
    elif user_number < rand_number:
        print('low')
    elif user_number > rand_number:
        print('more')
    count += 1
    return res(count)


res()
