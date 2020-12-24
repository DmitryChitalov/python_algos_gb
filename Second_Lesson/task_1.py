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
"""Т.к данная функция ничего не возвращает, а выводит на экран, то return не используем"""
def First_Recursion():
    operation = input("Введите операцию (+, -, *, / или 0 для выхода): ")
    if (operation == '0'):
        print("Конец функции, а соответственно и рекурсии")
    elif (operation in ['+', '-', '*', '/']):
        try:
            first_operand = int(input("Введите первое число: "))
            second_operand = int(input("Введите второе число: "))
        except ValueError:
            print("Вместо числа вы ввели строку. Исправьтесь...")
            First_Recursion()
        if (operation == '+'):
            print("Ваш результат: ", first_operand + second_operand)
        elif (operation == '-'):
            print("Ваш результат: ", first_operand - second_operand)
        elif (operation == '*'):
            print("Ваш результат: ", first_operand * second_operand)
        elif (operation == '/'):
            try:
                first_operand / second_operand
            except ZeroDivisionError:
                print("На 0 делить нельзя.")
            else:
                print("Ваш результат: ", first_operand / second_operand)
        First_Recursion()
    else:
        print("Неверный знак операции.")
        First_Recursion()

First_Recursion()