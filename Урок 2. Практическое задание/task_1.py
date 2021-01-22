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

def rec_calc():
    user_input = input("Please enter operation type +, -, *, / or enter 0 to exit: ")

    if user_input == '0':
        return "Exit program"
    else:
        if user_input in '+-*/':

            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))

                if user_input == '+':
                    result = num1 + num2
                    print(f"Results will be {result}")
                    return rec_calc()

                elif user_input == '-':
                    result = num1 - num2
                    print(f"Results will be {result}")
                    return rec_calc()

                elif user_input == '*':
                    result = num1 * num2
                    print(f"Results will be {result}")
                    return rec_calc()

                elif user_input == '/':
                    if num2 != 0:
                        result = num1 / num2
                        print(f"Results will be {result}")
                    else:
                        print("Can not divide by 0")
                    return rec_calc()

            except ValueError:
                print("Please enter correct symbol")
                return rec_calc()

        else:
            print("You entered incorrect symbol, please try again")
            return rec_calc()


rec_calc()
