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


def rec_quess(i, num):
    user_try = int(input('Enter a number from 1 to 100: \n'))  #запрос числа
    if i == 10 or user_try == num:  # условие завершения
        print(f'The hidden number is {num}')
        if i == 10:
            print('You didn\'t guess')
        elif user_try == num:
            print('It is right answer!')
    else:
        print(f'It\'s your {i} try')
        i += 1
        if user_try > num:
            print(f'The hidden number is less than {user_try}\n')
        else:
            print(f'The hidden number is greater than {user_try}\n')
        rec_quess(i, num)


rec_quess(1, random.randint(0, 100))
