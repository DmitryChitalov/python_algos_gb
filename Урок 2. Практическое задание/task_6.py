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

def iknow(my_num, count=10):
    if count == 0:
        print(f'Число попыток кончилось. Вы не угадали. Загаданное число - {my_num}')
        return False
    num = int(input('Угадай какое число я загадал (от 0 до 100):'))
    if num > my_num:
        print('Мое число меньше')
    elif num < my_num:
        print('Мое число больше')
    elif num == my_num:
        print(f'Вы угадали c {11-count} попытки')
        return True
    iknow(my_num, count-1)


number = random.randint(0, 100)
iknow(number)