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

def ugaday():
    guesses_made = 0
    name = input('Привет! Как тебя зовут?\n')
    number = random.randint(0, 100)
    print('Отлично, {0}, я загадал число между 1 и 30. Сможешь угадать?'.format(name))

    if guesses_made < 10:
        guess = int(input('Введи число: '))
        guesses_made += 1
        return 0

        if guess < number:
            print('Твое число меньше того, что я загадал.')

        if guess > number:
            print('Твое число больше загаданного мной.')

        if guess == number:
            return 0

    if guess == number:
        print('Ух ты, {0}! Ты угадал мое число, использовав {1} попыток!'.format(name, guesses_made))
    else:
       print('А вот и не угадал! Я загадал число {0}'.format(number))




ugaday()
