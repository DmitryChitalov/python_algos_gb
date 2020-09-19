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

from random import randint


def game(n=randint(1, 100), try_counter=1):
    if try_counter > 10:
        return print(f' You`re loser! correct number is {n}')
    print(f'your try is {try_counter}')
    user_n = int(input('number: '))
    if user_n == n:
        return print('You`re winner')
    elif user_n > n:
        print('incorrect, ur number is bigger')
    elif user_n < n:
        print('incorrect, ur number is smaller')
    try_counter += 1
    return game(n, try_counter)


game()
