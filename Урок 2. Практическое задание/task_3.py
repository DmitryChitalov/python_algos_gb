"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
"""


def is_a_digit(data):
    while not data.isdigit():
        print('Ошибка ввода. Пожалуйста, введите одно целое натуральное число.')
        data = input('Введите число: ')
    return data


def rec(user_input, num=''):
    if len(user_input) != 0:
        num += (user_input[-1])
        return rec(user_input[:-1], num)
    else:
        return num


print(f'Перевернутое число: {rec(is_a_digit(input("Введите число, которое требуется перевернуть: ")))}')
