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


def guess_number(number=None, count=1):
    if number is None:
        number = randint(0, 100)
        print('Загадано число от 0 до 100\nУ вас 10 попыток')
    user_number = int(input('Угадайте число '))
    if count == 10:
        return f'Было загадано число {number}'
    if user_number == number:
        return f'вы угадали число за {count} попыток\nБыло загадано число {number}'
    elif user_number < number:
        print(f'Загаданное число больше, осталось попыток: {10 - count}')
    else:
        print(f'Загаданное число меньше, осталось попыток: {10 - count}')
    count += 1
    return guess_number(number, count)


print(guess_number())
