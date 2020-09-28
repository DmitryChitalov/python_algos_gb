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


def guess_number(hidden_number, user_number=-1, move=10):
    try:
        user_number = int(input('\nВведите целое число:'))
    except ValueError:
        print('Введено некорректное значение')
        return guess_number(hidden_number, user_number, move)

    if user_number == hidden_number:
        return print('Вы отгадали')

    else:
        if move > 1:
            move -= 1
            if user_number > hidden_number:
                print(f'Ваше число больше загаданного, осталось попыток: {move}')

            elif user_number < hidden_number:
                print(f'Ваше число меньше загаданного, осталось попыток: {move}')

            else:
                print(f'ОШИБКА!: Непредвиденная ситуация')

            return guess_number(hidden_number, user_number, move)

        else:
            print(f'Вы не отгадали, загаданное число: {hidden_number}')


rand_number = randint(0, 100)
print('Отгадайте число от 0 до 100')
guess_number(rand_number)
