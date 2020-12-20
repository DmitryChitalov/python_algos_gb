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


def natural_input():
    __natural = input('Введите число от 0 до 100: ')
    try:
        __natural = int(__natural)
        assert __natural>0 and __natural<100
        return __natural
    except ValueError:
        print('Вы ввели не число')
        return natural_input()
    except AssertionError:
        print('Вы ввели число вне диапазона')
        return natural_input()

def guess_game(riddle,answer,tries = 10):
    if riddle == answer:
        print(f'Вы отгадали число {riddle}')
    elif tries == 0:
        print(f'Вы не отгадали число {riddle}')
    else:
        if(riddle>answer):
            print('Загаданное число больше чем предложенное')
        else:
            print('Загаданное число меньше чем предложенное')
        print(f'У вас осталось попыток: {tries-1}')
        guess_game(riddle, natural_input(), tries-1)

guess_game(randint(0,100),natural_input())