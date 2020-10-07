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


def riddle(correct_answer: int, tries_left=10):
    if tries_left == 0:
        print(f'Вы проиграли! Загаданное число: {correct_answer}')
        return
    else:
        user_answer = int(input(f'Введите число от 0 до 100: '))
        if user_answer == correct_answer:
            print(f'Поздравляю, вы выиграли!')
        else:
            if user_answer < correct_answer:
                to_print_str = 'меньше'
            else:
                to_print_str = 'больше'
            if tries_left - 1:
                to_print_tries = f'осталось {tries_left - 1}'
            else:
                to_print_tries = 'не осталось'
            print(f'Введенное число {to_print_str} загаданного! У вас {to_print_tries} попыток.')
            riddle(correct_answer, tries_left - 1)


riddle(random.randint(0, 100))
