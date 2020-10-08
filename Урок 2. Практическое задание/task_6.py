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


def guess_number(original_number=random.randint(0, 100), try_count=0):
    input_number = int(input("Введите число от 0 до 100: "))
    if 0 <= input_number <= 100:
        if try_count == 9:
            print(f"Вы проиграли!Количество попыток исчерпано. Загаданное число - {original_number}")
            return
        if input_number == original_number:
            print(f"Вы угадали! Количество попыток составило - {try_count + 1}")
            return
        elif input_number > original_number:
            print("Загаданное число меньше, чем введенное")
            guess_number(original_number, try_count + 1)
        else:
            print("Загаданное число больше, чем введенное")
            guess_number(original_number, try_count + 1)
    else:
        print("Вы ввели число вне диапазона!")
        guess_number(original_number, try_count)


guess_number()
