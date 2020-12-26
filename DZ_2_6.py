"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число."""

import random


def recurs(user_try, num):
    print(f"Попытка №{user_try}")
    if num == 10:
        print("Это последняя попытка! ")
    user_input = input("Введите число ")
    while not user_input.isdigit():
        user_input = input("Нужно ввести число! Введите число ")
    if int(user_input) == num:
        print(f"Молодец! Ты угадал с {user_try} попытки!")
    elif user_try == 10:
        return print(f"---------YOU LOSE------------\n"
                     f"Вот загаданное число {num}")
    else:
        if num < int(user_input):
            print("Загаданное число меньше\n----------------")
            recurs(user_try + 1, num)
        if num > int(user_input):
            print("Загаданное число больше\n----------------")
            recurs(user_try + 1, num)


recurs(1, random.randint(0, 100))
