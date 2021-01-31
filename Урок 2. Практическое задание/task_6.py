"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Базовый случай здесь - угадали число или закончились попытки
"""


from random import randint

secret_number = randint(0, 100)


def guessing_game(count, secret_number):
    user_number = int(input('Угадате число от 1 до 100: '))
    if count == 10:
        print(f'Количество попыток исчерпано, загаданное число: {secret_number}')

    elif user_number == secret_number:
        print(f'Поздравляем, вы угадали с  {count} попытки!, Загаданное число: {secret_number}')

    elif int(user_number) < secret_number:
        print('Число меньше загаданного: ')
        print(f'Попытка № {count + 1} ')
        return guessing_game(count + 1, secret_number)

    elif int(user_number) > secret_number:
        print("Ваше число больше загаданного: ")
        print("Попытка №", count + 1)
        return guessing_game(count + 1, secret_number)


guessing_game(1, secret_number)
