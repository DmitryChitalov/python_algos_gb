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


def guess_num(num , counter):
    print(f'Try №: {counter}')
    answer = int(input('Please enter a number from 1 to 100: '))
    if counter == 10 or num == answer:
        if num == answer:
            print('Congratulations')
        print(f'Right answer is {num}')
    else:
        if answer < num:
            print('Entered number too small')
        else:
            print('Entered number too big')
        guess_num(num, counter + 1)


guess_num(random.randint(0, 100), 1)