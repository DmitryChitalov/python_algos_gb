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


def guess_the_number(num=random.randint(0, 100),
                     user_answer=int(input('Try to guess a number from 0 to 100. '
                                           'You have 10 attempts. Enter an integer: ')),
                     i=9):
    if i < 1:
        return print(f'You lost, answer - {num}')
    elif user_answer > num:
        print(f'Your number is greater\ntry again, attempts left {i}')
        return guess_the_number(num, int(input()), i-1)
    elif user_answer < num:
        print(f'Your number is less\ntry again, attempts left {i}')
        return guess_the_number(num, int(input()), i-1)
    else:
        return print(f'Congratulation! You win!\n'
                     f'Your answer - {user_answer}\nRemaining attempts - {i}')


guess_the_number()
