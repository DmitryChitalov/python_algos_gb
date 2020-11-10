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


def input_number(message):
    pass
    res = input(message).strip()
    if not res.isdigit() or int(res) > 100 or int(res) < 0 or int(res) != float(res):
        print("Недопустимый ввод!")
        res = input_number(message)

    return int(res)


def ask_user(my_random, tries_left):
    user_num = input_number("Введите целое число от 0 до 100: ")
    if user_num == my_random:
        print("Вы угадали! У Вас талант!")
        return
    else:
        tries_left -= 1

    if tries_left > 0:
        if user_num > my_random:
            print("Меньше")
        else:
            print("Больше")
        print(f"Попыток осталось {tries_left}")
        ask_user(my_random, tries_left)
    else:
        print(f"Попыток больше нет! Компьютер загадал число {my_random}")


def main():
    pass
    try:
        tries_left = 10
        my_random = random.randint(0, 100)
        ask_user(my_random, tries_left)
        print("Программа завершена!")
    except Exception as ex:
        print(f"Fatal error: {ex}")


if __name__ == "__main__":
    main()
