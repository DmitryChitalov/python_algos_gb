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


def my_calc():
    operation = input("Введите операцию (+, -, *, / или 0 для выхода): ")
    if operation.strip() == '0':
        print("Программа закрыта")

    elif operation.strip() == '+':
        number_1 = input("Введите первое число ")
        number_2 = input("Введите второе число ")
        print("Сумма равна: ", int(number_2.strip()) + int(number_1.strip()))
        my_calc()

    elif operation.strip() == '-':
        number_1 = input("Введите первое число ")
        number_2 = input("Введите второе число ")
        print("Разнмца равна: ", int(number_1.strip()) - int(number_2.strip()))
        my_calc()

    elif operation.strip() == '*':
        number_1 = input("Введите первое число ")
        number_2 = input("Введите второе число ")
        print("Произведение равно: ", int(number_2.strip()) * int(number_1.strip()))
        my_calc()

    elif operation.strip() == '/':
        number_1 = input("Введите первое число ")
        number_2 = input("Введите второе число ")
        if int(number_2.strip()) == 0:
            print("На ноль делить нельзя")
            my_calc()
        else:
            print("Частное равно: ", int(number_1.strip()) / int(number_2.strip()))
            my_calc()

    else:
        print("Вы ввели недопустимый символ, попробуйте еще раз")
        my_calc()


my_calc()
