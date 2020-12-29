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

def guess_the_number(attempt, number):

    print(f'Attempt {attempt}')
    answer = int(input('Please, input the number in range from 0 to 100: '))
    if attempt == 10 or answer == number:
        if answer == number:
            print('Right! You won!')
        print(f'The number is: {number}')

    else:
        if answer > number:
            print(f'The number to be divined is less')
        else:
            print(f'The number to be divined is more')
        guess_the_number(attempt + 1, number)


guess_the_number(1, random.randint(0, 100))