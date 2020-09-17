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

win_number = random.randint(0, 100)

def guess_number(attempts):
    if attempts == 0:
        return print(f'You Lose! Correct number is {win_number}')

    you_number = input('Введите число от 0 до 100:\n')

    try:
        int_you_number = int(you_number)
    except ValueError:
        print('Wrong number!')
        return guess_number(attempts - 1)

    if int_you_number == win_number:
        return print('You Win!')
    elif int_you_number > win_number:
        print('Your number is bigger!')
        return guess_number(attempts - 1)
    elif int_you_number < win_number:
        print('Your number is less!')
        return guess_number(attempts - 1)

guess_number(10)