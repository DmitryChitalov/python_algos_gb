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

hidden_n = random.randint(0, 101)


def guess_number(count=0):
    while True:
        try:
            user_answer = int(input('Enter number 0-100: '))
            if not 0 <= user_answer <= 100:
                raise ValueError
        except ValueError:
            print('You should enter a number 0-100')
        else:
            break
    count += 1
    if hidden_n == user_answer:
        return 'You win!'
    elif count == 10:
        return 'You lose'
    elif user_answer < hidden_n:
        print('Your number is less than the hidden number')
        return guess_number(count)
    else:
        print('Your number is greater than the hidden number')
        return guess_number(count)


print(guess_number())
