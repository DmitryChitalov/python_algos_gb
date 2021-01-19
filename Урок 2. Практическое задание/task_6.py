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


def check_num(number, attempts):
    try:
        check_num.i += 1
    except AttributeError:
        check_num.i = 1
    while True:
        try:
            ans = int(input(f'Отгадайте число от 1 до 100 (Попытка {check_num.i} из {attempts}): '))
        except ValueError:
            print('Нужно ввести целое число от 1 до 100!')
            ans = 101
        if 1 <= ans <= 100:
            break
    if check_num.i == attempts:
        return number
    else:
        if ans < number:
            print('Больше!')

        elif ans > number:
            print('Меньше!')
        if ans == number:
            print('Верно!')
            return number
        return check_num(number, attempts)


print(f'Загаданное число: {check_num(randint(1, 100), 10)}')
