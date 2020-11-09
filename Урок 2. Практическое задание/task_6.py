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

def guess_a_number(attempt, num):

    print(f'It is your {attempt} attempt!')
    user_answer = int(input('Guess a number from 0 to 100: '))

    if attempt == 4:
        print(f'You have no more attempts, dude. The right answer was {num}')
    else:
        if user_answer == num:
            print('Well, that is impressive!')
        elif user_answer > num:
            print('Number you guessed is greater than the right one!')
        else:
            print('Number you guessed is lower than the right one!')
        guess_a_number(attempt + 1, num)

guess_a_number(1, randint(0, 100))


