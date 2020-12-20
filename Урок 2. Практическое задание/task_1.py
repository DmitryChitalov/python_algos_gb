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
def sign():
    __temp_sign = input('Введите операцию (+, -, *, / или 0 для выхода):')
    if __temp_sign not in ['/', '*', '+','-','0']:
        print('Вы ввели неправильный символ')
        return sign()
    else:
        return __temp_sign

def first_operand():
    try:
        return int(input('Введите первое число:'))
    except:
        print('Вы ввели не число')
        return first_operand()
def second_operand(divisionflag=False):
    try:
        _temp = int(input('Введите второе число:'))
        if divisionflag and _temp == 0:
            raise ZeroDivisionError
        return _temp
    except ValueError:
        print('Вы ввели не число')
        return second_operand(divisionflag)
    except ZeroDivisionError:
        print('Вы пытаетесь поделить на ноль')
        return second_operand(divisionflag)

def recursion_calc():
    __sign = sign()
    print(__sign)
    __first_operand = first_operand()
    __second_operand = second_operand(__sign == '/')
    if __sign == '+':
        print(f'Ваш результат: {__first_operand + __second_operand}')
    elif __sign == '-':
        print(f'Ваш результат: {__first_operand - __second_operand}')
    elif __sign == '/':
        print(f'Ваш результат: {__first_operand/__second_operand}')
    elif __sign == '*':
        print(f'Ваш результат: {__first_operand*__second_operand}')
    if __sign != '0':
        recursion_calc()
    else:
        return 0

recursion_calc()