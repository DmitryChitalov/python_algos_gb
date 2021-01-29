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

import operator

def first_valid_number_input(a):
    try:
        return int(a)
    except ValueError:
        print('Вы ввели не число, исправьте')
        return False

def valid_operator_input(a, ops):
    try:
        return ops[a]
    except KeyError:
        print('Вы ввели неверную операцию, исправьте')
        return False

def second_valid_number_input(a, o, b):
    try:
        ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
        return ops[o](int(a), int(b))
    except ZeroDivisionError:
        print('Делить на 0 нельзя, введите число, отличное от 0')
        return False


def operations():
    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, "0": "0"}

    operation = input('Введите операцию (+, -, *, / или 0 для выхода):')

    while not valid_operator_input(operation, ops):
        operation = input('Введите операцию (+, -, *, / или 0 для выхода):')

    while valid_operator_input(operation, ops):

        if operation == '0':
            print('Закончили')
            break
        else:
            first_number = input('Введите первое число:')
            while valid_number_input(first_number):

                second_number = input('Введите второе число:')

                while second_valid_number_input(first_number, operation, second_number):
                    print(operation_check(first_number, operation, second_number))

                    return operations()


