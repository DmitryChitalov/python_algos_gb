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


def calculator():

    operation = None
    operand = None

    def operation_input():
        nonlocal operation
        sign = input('Введите операцию (+, -, *, / или 0 для выхода): ')
        if sign in '+-*/0':
            operation = sign
            return
        else:
            print('Ошибка ввода!')
            operation_input()

    def operand_input(side: str):
        nonlocal operand
        oper = input(f'Введите {side} число: ')
        if operation == operator.truediv and side == 'второе' and oper == '0':
            print('Деление на 0 недопустимо! Введите другой делитель!')
            operand_input(side)
        elif oper.isdigit():
            operand = oper
            return
        else:
            print('Вы вместо числа ввели строку (((. Исправьтесь')
            operand_input(side)

    operation_input()

    if operation == '+':
        operation = operator.add
    elif operation == '-':
        operation = operator.sub
    elif operation == '*':
        operation = operator.mul
    elif operation == '/':
        operation = operator.truediv
    elif operation == '0':
        print('Завершение работы!')
        return

    operand_input('первое')
    left_operand = int(operand)

    operand_input('второе')
    right_operand = int(operand)

    print(f'Ваш результат {operation(left_operand, right_operand)}')

    calculator()


if __name__ == '__main__':
    calculator()
