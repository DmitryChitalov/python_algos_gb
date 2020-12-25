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


def user_guess():
    user_input = int(input("Угадайте число от 0 до 100: "))
    return user_input


def guess_number(correct_answer, user_try, count):
    print(correct_answer)
    if count == 0:
        print('Количество попыток иссякло! Вы проиграли.')
        exit(0)
    if user_try == correct_answer:
        print(f'Вы угадали! Верное число {correct_answer}')
        exit(0)
    if user_try < correct_answer:
        print('Загаданное число больше! Попробуйте еще!')
        guess_number(correct_answer, user_guess(), count - 1)
    else:
        print('Загаданное число меньше! Попробуйте еще!')
        guess_number(correct_answer, user_guess(), count)


guess_number(random.randint(0,100), user_guess(), 10)
