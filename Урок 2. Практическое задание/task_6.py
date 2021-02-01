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


def guess_number(number: int, attempt_number: int):
    if attempt_number > 10:
        print(f"Попытки закончились. Было загадано число {number}")
        return
    var_str = input("Введите число от 0 до 100: ")
    while not var_str.isdigit():
        print("Введено не число")
        var_str = input("Введите число от 0 до 100: ")
    var_int = int(var_str)
    if var_int == number:
        print("Верно!!!")
        return
    elif number > var_int:
        print("Загаданное число больше")
    elif number < var_int:
        print("Загаданное число меньше")

    guess_number(number, attempt_number + 1)
    return


current_number = random.randint(0, 100)
guess_number(current_number, 1)
