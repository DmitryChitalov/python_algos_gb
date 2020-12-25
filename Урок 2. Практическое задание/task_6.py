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


def game(number, moves_remain):

    if moves_remain <= 0:
        return f"Ходы закончились! Загаданное число - {number}"

    while True:
        str_in = input("Введите число: ")
        if str_in.isnumeric():
            in_num = int(str_in)
            break

    if in_num == number:
        return f"Число отгадано! Загаданное число - {number}! Осталось ходов - {moves_remain}"

    if number > in_num:
        moves_remain -= 1
        print(f"Неверно! Загаданное число больше {in_num}. Осталось ходов {moves_remain}")
        return game(number, moves_remain)
    else:
        moves_remain -= 1
        print(f"Неверно! Загаданное число меньше {in_num}. Осталось ходов {moves_remain}")
        return game(number, moves_remain)


print(game(randint(0, 100), 10))
