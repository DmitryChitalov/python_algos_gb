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

def calc_data():
    MathCommand = "+-*/"
    UserData = input("Введите операцию (+, -, *, / или 0 для выхода):")
    if UserData == "0":
        return 0
    elif MathCommand.find(UserData[0])>-1:
        try:
            numOne = float(input("Введите первое число:"))
            numTwo = float(input("Введите второе число:"))
            result=0
            if UserData[0] == "+":
                result = numOne+numTwo
                print("Результат сложенияравен: ", result)
            elif UserData[0] == "-":
                result = numOne-numTwo
                print("Результат вычитания равен: ", result)
            elif UserData[0] == "*":
                result = float(numOne)*float(numTwo)
                print("Результат умножения равен: ", result)
            elif UserData[0] == "/":
                if numTwo != 0:
                    result = float(numOne)/float(numTwo)
                    print("Результат деления равен: ", result)
                else:
                    print("Деление на нуль нарушает законы математики и природы.")
        except ValueError:
            print("Введенные данные не являются числами! Соберитесь!")
    calc_data()

calc_data()