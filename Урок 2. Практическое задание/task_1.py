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
from random import randint, choice
import sys

OPS = {
    "+": lambda x, y: x+y,
    "-": lambda x, y: x-y,
    "*": lambda x, y: x*y,
    "/": lambda x, y: x/y,
    "0": lambda x, y: 0
}


def input_num(nonzero=False):
    while True:
        inp = input("Введите число: ")
        try:
            res = float(inp)
            if not (nonzero and res == 0):
                return res
            else:
                print("Нельзя делить на ноль")
        except ValueError:
            print("Это не число: ", inp)


def input_op():
    while True:
        inp = input("Введите операцию (+, -, *, / или 0 для выхода): ")
        if inp in OPS:
            return inp
        else:
            print("Такой операции нет")

# Первый вариант с последовательностью ввода (op,x,y)
# соответствует требованию задачи
def calc(op=None, x=None, y=None):
    if op is None:
        return calc(input_op(), x, None)
    if op=="0":
        return None
    if x is None:
        return calc(op, input_num(), None)
    y = input_num(nonzero=(True if op == "/" else False))
    res = OPS[op](x,y)
    print(x, op, y, '=', res)
    return calc(None, None, None)

# Второй вариант, у которого последовательность ввода
# (x, op, y) сохраняет результат вычисления как первый
# операнд следующей операции и позволяет, например,
# подсчитывать сумму ряда
def calc2(x=None, op=None, y=None):
    if x is None:
        return calc2(input_num(), None, None)
    if op is None:
        return calc2(x, input_op(), None)
    if op=="0":
        return None
    y = input_num(nonzero=(True if op == "/" else False))
    res = OPS[op](x,y)
    print(x, op, y, '=', res)
    return calc2(res, None, None)

# симулятор пользователя
OPKEYS = list(OPS)
def myinput(prompt):
    if prompt.endswith("): "):
        result = choice(OPKEYS)
    else:
        result = randint(0,5)
    print(prompt, result)
    return result

# Без аргументов запускается вариант 1 в интерактивном режиме
# ... с аргументом "1" вариант 1 в режиме симуляции
# ... с аргументом "2" вариант 2 в интерактивном режиме
# ... c любым другим аргументом вариант 2 в режиме симуляции
if len(sys.argv)<2:
    calc()
else:
    if sys.argv[1]=="1":
        input = myinput
        calc()
    elif sys.argv[1]=="2":
        calc2()
    else:
        input = myinput
        calc2()
