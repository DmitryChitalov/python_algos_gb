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
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

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

import sys
sys.setrecursionlimit(10000)


def add(num1, num2):
    if num2 == 0:
        return num1
    else:
        return add(num1 + 1, num2 - 1)


def sub(num1, num2):
    if num2 == 0:
        return num1
    else:
        return sub(num1 - 1, num2 - 1)


def mult(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    elif num1 == 1:
        return num2
    else:
        return num2 + mult(num1 - 1, num2)


def div(num1, num2):
    if num1 < num2:
        return 0
    elif num2 == 0:
        return ('You cannot divide by zero, dude!')
    else:
        return 1 + div(num1 - num2, num2)




def calc():

    while True:
        user_input = input('Enter +, -, *, / or 0 for exit: ')

        if user_input == '0':
            return ('Farewell!')
        elif user_input == '+':
            num1 = int(input('Enter first number: '))
            num2 = int(input('Enter second number: '))
            print(add(num1, num2))
        elif user_input == '-':
            num1 = int(input('Enter first number: '))
            num2 = int(input('Enter second number: '))
            print(sub(num1, num2))
        elif user_input == '*':
            num1 = int(input('Enter first number: '))
            num2 = int(input('Enter second number: '))
            print(mult(num1, num2))
        elif user_input == '/':
            num1 = int(input('Enter first number: '))
            num2 = int(input('Enter second number: '))
            print(div(num1, num2))
        else:
            print('Try integers instead!')

print(calc())