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


def guess_number_game(random_number, attempts):
    if attempts == 0:
        print('Простите, но вы проиграли. Правильный ответ:', random_number)
    else:
        user_num = int(input(f'Попробуйте угадать число: '))
        if user_num == random_number:
            print(f'Поздравляем! Вы угадали число с {11 - attempts} раза')
        elif user_num > random_number:
            print(f'Многовато будет. У вас осталось {attempts - 1} попыток\n')
            return guess_number_game(random_number, attempts - 1)
        else:
            print(f'Маловато будет. У вас осталось {attempts - 1} попыток\n')
            return guess_number_game(random_number, attempts - 1)


rand_num = random.randint(0, 100)
print(rand_num)
guess_number_game(rand_num, 10)
