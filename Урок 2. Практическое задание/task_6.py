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

number_random = random.randint(0, 100)


def number_ser(count, number_random):
    try:
        number = input("Введите число: ")
        if count > 10 or number_random == int(number):
            if number_random == int(number):
                print('Вы угадали! Поздравляем!')
            return print(f'Загаданное число {number_random}')
        else:
            if number_random > int(number):
                print(f'Введенное Вами число меньше загаданного!')
            elif number_random < int(number):
                print(f'Введенное Вами число больше загаданного!')
    
            number_ser(count + 1, number_random)

    except ValueError:
        print("Вы ввели не число, пожалуйста, введите число")
        number_ser(count + 1, number_random)
    

number_ser(1, number_random)
