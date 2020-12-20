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

from random import randrange


def guessing_game(num, number_of_attempts=10):
    guess_num = num
    if number_of_attempts == 0:
        print('Попытки закончились. Вы проиграли')
        return
    else:
        try:
            print(f'Программа загадала случайное число. У вас есть {number_of_attempts} попыток, чтобы отгадать его')
            user_num = int(input(f'Ведите свой вариант: '))
            if user_num == guess_num:
                print(f'Позравляю с победой! Загаданное число было {guess_num}')
                return
            elif user_num > guess_num:
                number_of_attempts -= 1
                print('Введённое число больше загаданного')
                guessing_game(num, number_of_attempts)
            elif user_num < guess_num:
                number_of_attempts -= 1
                print('Введённое число меньше загаданного')
                guessing_game(num, number_of_attempts)
        except ValueError:
            print('Вместо числа вы введи строку. Пожалуйста введите число')
        guessing_game(num, number_of_attempts)


if __name__ == '__main__':
    num = randrange(100)
    guessing_game(num)
