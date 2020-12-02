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


class Calc:

    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.operator = 0
        self.result = 0

    def start(self):
        user_input = input('Введите через пробел оператор и 2 числа\n(например: * 2 2)' \
                           ' или 0 для выхода: ')
        if user_input != '0':
            try:
                self.operator, self.num1, self.num2 = user_input.split()
                self.num1 = int(self.num1)
                self.num2 = int(self.num2)
            except:
                self.wrong()
            if self.operator == '+':
                self.result = self.sum(self.num1, self.num2)
                self.clean()
            elif self.operator == '-':
                self.result = self.sub(self.num1, self.num2)
                self.clean()
            elif self.operator == '*':
                self.result = self.mult(self.num1, self.num2)
                self.clean()
            elif self.operator == '/':
                self.result = self.div(self.num1, self.num2)
                self.clean()
            else:
                self.wrong()
            print(f'результат - {self.result}')
            self.start()
        else:
            return

    def wrong(self):
        print('Неверный ввод')
        self.start()

    def clean(self):
        self.num1 = 0
        self.num2 = 0
        self.operator = 0

    def sum(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def mult(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        try:
            return round(num1 / num2, 2)
        except ZeroDivisionError:
            return 'Деление на ноль!'


calc = Calc()
calc.start()
