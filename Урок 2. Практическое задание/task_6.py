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


def guess_process_func(riddle_number, attempts_counter=9):
    # target_num = target_num
    print(f'Осталось {attempts_counter + 1} попыток.')
    user_number = int(input("Отгадайте число от 0 до 100:"))
    if attempts_counter == 0:
        print(f'Число {riddle_number} не угадано! Ваши попытки закончились!')
        return
    elif user_number == riddle_number:
        print(f'Число {riddle_number} угадано!')
        return
    else:
        if user_number > riddle_number:
            print(f'Ваше число больше искомого!')
            attempts_counter -= 1
            guess_process_func(riddle_number, attempts_counter)
        elif user_number < riddle_number:
            print(f'Ваше число меньше искомого!')
            attempts_counter -= 1
            guess_process_func(riddle_number, attempts_counter)


if __name__ == '__main__':
    try:
        guess_process_func(random.randint(0, 100))
    except ValueError:
        print('Ошибка. Вы ввели не число.')
