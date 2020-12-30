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


def guess_rec(number, TTL=0, my_try=1):
    try:
        if my_try > TTL:
            return f"У Вас не получилось угадать - закончились попытки, число: {number}"
        else:
            answer = int(input("Введите целое число от 0 до 100 "))
            if answer == number:
                return f'Вы угадали число - {number}, Поздравляю!'
            else:
                if answer < number:
                    print('Число больше!')
                    return guess_rec(number, TTL, my_try + 1)
                else:
                    print('Число меньше!')
                    return guess_rec(number, TTL, my_try + 1)

    except ValueError:
        return guess_rec(number, TTL, my_try + 1)


TOTAL_TRIES = 10

print(guess_rec(random.randint(0, 100), TOTAL_TRIES))

