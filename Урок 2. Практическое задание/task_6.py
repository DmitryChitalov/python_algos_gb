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


def try_to_guess(num, count):
    if count == 10:
        return print(f'You did not guess. Number of try is {count}')
    user_num = int(input('Enter your number: '))

    if user_num == num:
        return print(f'You are right ! Number of try is {count}')
    elif user_num > num:
        print(f'You are wrong, your number is bigger.')
    elif user_num < num:
        print(f'You are wrong, your number is smaller.')
    count += 1

    return try_to_guess(num, count)


some_num = random.randint(0, 100)
try_to_guess(some_num, 0)