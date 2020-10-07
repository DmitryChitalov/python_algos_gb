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


def guess():

    target = random.randint(0, 100)
    user_number = None
    max_tries = 10

    def number_input():
        nonlocal user_number
        inp = input('Введите число от 0 до 100: ')
        if inp.isdigit():
            user_number = inp
            return
        else:
            print('Вы вместо числа ввели строку (((. Исправьтесь')
            number_input()

    def game(tries):
        nonlocal user_number
        if tries == 0:
            print(f'Вы проиграли! Было загадано число {target}')
            return
        else:
            number_input()
            user_number = int(user_number)
            if user_number == target:
                print(f'Отгадали! Верный ответ {target}')
                return
            else:
                hint = 'больше' if user_number > target else 'меньше'
                print(f'Ваше число {hint} загаданного')
                print(f'Осталось попыток: {tries - 1}')
                game(tries - 1)

    game(max_tries)


if __name__ == '__main__':

    guess()
