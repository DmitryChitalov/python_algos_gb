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


class Calculator:
    def __init__(self, number_1, number_2, signal):
        self.number_1 = number_1
        self.number_2 = number_2
        self.signal = signal

    def recursive_calc(self):
        if self.signal == '0':
            return
        elif self.signal == '*':
            self.number_1 = self.number_1 * self.number_2
        elif self.signal == '/':
            try:
                self.number_1 = self.number_1 / self.number_2
            except ZeroDivisionError:
                print('Деление на 0 запрещено')
                self.number_2 = input_number('корректное')
                return self.recursive_calc()
        elif self.signal == '-':
            self.number_1 = self.number_1 - self.number_2
        elif self.signal == '+':
            self.number_1 = self.number_1 + self.number_2
        print(f'Ваш результат: {self.number_1}')
        self.number_2 = input_number('следующее')
        self.signal = input_signal()
        return self.recursive_calc()


def input_signal():
    signals = ['/', '*', '-', '+', '0']
    signal = input('Введите действие *, /, -, +, или 0 для выхода: ')
    if signal not in signals:
        return input_signal()
    return signal


def input_number(n):
    try:
        number = float(input(f'Введите {n} число: '))
    except ValueError:
        print('Введено недопустимое значение')
        return input_number(n)
    return number


number_1 = input_number('первое')
number_2 = input_number('второе')
signal = input_signal()
calc = Calculator(number_1, number_2, signal)
calc.recursive_calc()
