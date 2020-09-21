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

def find_number(target_num, attempt = 9):
    target_num = target_num
    print(f'осталось {attempt+1} попыток')
    user_num = int(input("введите число от 0 до 100:"))
    if user_num == target_num:
        print(f'число {target_num} угадано')
        return
    if attempt ==0:
        print(f'число {target_num} не угадано')
        return
    if user_num > target_num:
        print(f'ваше число больше искомого')
        attempt -= 1
        find_number(target_num, attempt)
    if user_num < target_num:
        print(f'ваше число меньше искомого')
        attempt -= 1
        find_number(target_num, attempt)


find_number(random.randint(0,100))