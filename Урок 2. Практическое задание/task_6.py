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
random_num = random.randint(0, 100)
count = 0


def guess():
    global random_num, count
    if count < 10:
        user_num = int(input(f'введите число: '))
        if user_num == random_num:
            print(f'победа!')
        elif user_num < random_num:
            print(f'бери больше!')
            count += 1
            guess()
        else:
            print(f'бери меньше!')
            count += 1
            guess()
    else:
        print(f'попытки закончились :( загаданное число было {random_num}')
        
        
   guess()
