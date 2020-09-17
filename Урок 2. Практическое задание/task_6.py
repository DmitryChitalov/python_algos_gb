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


def start_game():
    """
    функция предлагает пользователю сыграть, проверяет правельность ввода, запускает или заканчивает игру
    """
    try:
        start = input(f'Хотите сыграть в игру "Угадай число"? \n'
                      f' для начала игры введите "1", для выхода "0": ')

        assert start in ['0', '1']

        if start == '1':
            main(generator_number())
            start_game()
        else:
            print('Досвидания')
            return
    except Exception as e:
        print('Ошибка ввода')
        return start_game()


def input_number():
    """
    функция запрашивает у пользователя натуральное число, проверяет правельность ввода, возвращяет введенное число
    :return: int
    """
    try:
        number = int(input('Введите натуральное число от 0 до 100: '))
        assert 0 <= number <= 100
        return number
    except Exception as e:
        print("Ошибка ввода")
        return input_number()


def generator_number():
    """
    функция генерирует случайное число от 0 до 100 и возвращяет его
    :return: int
    """
    return random.randint(0, 101)


def checking_number(hid_num, us_num):
    """
    функция проверяет числа на совпадения,выдает результат, подсказки и возвращяет Bool
    :return: boolean
    """
    if us_num == hid_num:
        print(f'Вы угадали число {hid_num}')
        return False
    elif us_num > hid_num:
        print('Загаданное число меньше')
        return True
    else:
        print('Загаданное число больше')
        return True


def main(hidden_number, count=10):
    """
     функция запускает игру, получает загаданное число и управляет игрой
     """
    user_number = input_number()
    flag = checking_number(hidden_number, user_number)
    if flag is False:
        return
    if count == 1:
        print(f'Вы проиграли, это было число {hidden_number}')
        return
    count -= 1
    print(f'У Вас осталось {count} попыток')
    main(hidden_number, count)


if __name__ == '__main__':
    start_game()
