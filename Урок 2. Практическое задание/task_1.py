"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, /
- условие завершения рекурсии - введена операция 0

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def is_digit_old(str_number):
    '''
    Рекурсивная функция для проверки является ли строка целым положительным числом.
    Функция конечно очень крутая, но я вдруг понял, что она бесполезна при проверке
    отрицательных чисел :c
    '''
    allowed_symb = '1234567890'
    if str_number == '':
        return True
    elif str_number[-1] in allowed_symb:
        return is_digit_old(str_number[:-1])
    return False


def clear_digit(str_number):
    '''Рекурсивно очищает число от других символов.'''
    allowed_symb = '1234567890'
    if str_number == '':
        return ''
    elif str_number[-1] in allowed_symb:
        return clear_digit(str_number[:-1]) + str_number[-1]
    return clear_digit(str_number[:-1]) + ''


def check_digit(str_number):
    '''Проверяет является ли строка целым числом.'''
    # Очищаем число от других символов.
    new_number = clear_digit(str_number)
    if str_number[0] == '-':
        new_number = str_number[0] + new_number
    if str_number == new_number:
        return True


def rec_calc():
    operation = input('[?] Введите операцию (+, -, *, / или 0 для выхода): ')
    if operation == '0':
        print('[v] Программа завершена.')
        return
    elif operation in ['+', '-', '*', '/']:
        first_number = input('[1] Введите первое число: ')
        second_number = input('[2] Введите второе число: ')
        if check_digit(first_number) and check_digit(second_number):
            if operation == '+':
                result = int(first_number) + int(second_number)
            elif operation == '-':
                result = int(first_number) - int(second_number)
            elif operation == '*':
                result = int(first_number) * int(second_number)
            else:
                result = int(first_number) / int(second_number)
            print(f'[=] {int(first_number)} {operation} {int(second_number)} = {result}\n')
        else:
            print('[x] Неверный ввод данных.\n')
    else:
        print('[x] Неверный ввод данных.')
    rec_calc()


rec_calc()
