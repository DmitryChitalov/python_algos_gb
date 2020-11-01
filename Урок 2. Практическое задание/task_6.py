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


def guessing_game(max_number=100, attempts_count=10, first_start=True, hidden_num=0):
    """Рекурсивная функция, реализующая игру Угадайка.

    :param max_number: Максимальный предел загадываемых чисел
    :param attempts_count: Количество оставшихся попыток
    :param first_start: Признак первого запуска
    :param hidden_num: Загаданное число, которое будет рекурсивно передаваться
    :return: Вывод интерфейса игры в терминал
    """
    if first_start:
        hidden_num = randint(0, max_number)
        print(f"{'=' * 40}\n Игра в угадайку (числа от 0 до {max_number})\n{'=' * 40}")
    if attempts_count > 0:
        print(f"\nУ вас попыток: {attempts_count}")
    else:
        print(f"\nУвы! Вы проиграли. Вы не отгадали число {hidden_num}")
        return
    try:
        user_num = int(input(f"Введите число от 0 до {max_number}: "))
        if user_num == hidden_num:
            print("\nУра!!! Вы победили!")
            return
        elif user_num < hidden_num:
            print("Ваше число МЕНЬШЕ загаданного...")
        else:
            print("Ваше число БОЛЬШЕ загаданного...")
    except ValueError:
        print("Вы ввели что-то не то. Попробуйте снова...")
        attempts_count += 1
    guessing_game(max_number, attempts_count - 1, False, hidden_num)


#################################
# Старт игры
guessing_game()
