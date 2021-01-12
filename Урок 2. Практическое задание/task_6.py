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

magic_number = randint(0, 100)


def start_guess(amount, to_guess):
    user_guess = input("Угадайте число: ")

    if amount == 10:
        return f"Попытки исчерпаны, было загадано {to_guess}"
    elif int(user_guess) == to_guess:
        return "Вы угадали!!!"
    elif int(user_guess) < to_guess:
        print("Ваше число меньше загаданного: ")
        print("Число попыток ", amount)
        return start_guess(amount + 1, to_guess)
    elif int(user_guess) > to_guess:
        print("Ваше число больше загаданного: ")
        print("Число попыток ", amount)
        return start_guess(amount + 1, to_guess)


print(start_guess(1, magic_number))