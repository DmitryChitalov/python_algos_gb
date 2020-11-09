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


# функция проверки вводимых данных на float:
def check_to_float(text=None):
    while True:
        data = input(text)
        if not data.lstrip('-').replace('.', '', 1).isdigit():
            print('Пожалуйста, повторите ввод: нужно ввести натурально число')
        else:
            """
            Пункт проверки выше допупускает любое количество введённых знаков "минус", 
            поэтому здесь введена дополнительная проверка.
            """
            if data[0] == '-':
                data = data[0] + data.lstrip(data[0])
            return float(data)


# рекурсия:
def rec(nums=[], operation=None):
    while True:
        if len(nums) == 0:
            operation = input('Введите операцию (+, -, *, / или 0 для выхода): ')
        if operation in ('+', '-', '*', '/'):
            if len(nums) < 2:
                nums.append(check_to_float('Введите число: '))
                return rec(nums, operation)

            if operation == '+':
                return nums[0] + nums[1]
            elif operation == '-':
                return nums[0] - nums[1]
            elif operation == '*':
                return nums[0] * nums[1]
            elif operation == '/':
                return nums[0] / nums[1]

        elif operation == '0':
            break
        elif operation not in ('+', '-', '*', '/', '0'):
            print(f'Ошибка ввода, повторите ввод ещё раз.\n')


print(rec())
