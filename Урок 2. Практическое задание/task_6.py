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

print('Игра: Угадай число от 0 до 100!')
number = random.randint(0, 100)
count = 10


def game(a, b):
    if a == 0:
        return print(f'Проиграли! Загаданное число: {b}')
    user_number = int(input(f'Осталось попыток - {a}. Введите число: '))
    if b == user_number:
        return print('Победа!!!')
    elif b < user_number:
        print(f'Ваше число больше загаданного')
        return game(a - 1, b)
    else:
        print(f'Ваше число меньше загаданного')
        return game(a - 1, b)


game(count, number)
