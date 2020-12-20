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


def calc():
    text_from_operator = 'Введите операцию (+, -, *, / или q для выхода): '
    operator = input(text_from_operator)
    while operator not in ('+', '-', '*', '/', 'q'):
        print('Вы ввели неверную операцию!')
        operator = input(text_from_operator)
    if operator == 'q':
        print('Cпасибо за пользование программой')
        return
    else:
        try:
            num_1 = float(input('Введите первое число: '))
            num_2 = float(input('Введите второе число: '))
            if operator == '+':
                print(f'{num_1} + {num_2} = {num_1 + num_2}')
            elif operator == '-':
                print(f'{num_1} - {num_2} = {num_1 - num_2}')
            elif operator == '*':
                print(f'{num_1} * {num_2} = {num_1 * num_2}')
            elif operator == '/':
                print(f'{num_1} / {num_2} = {num_1 / num_2}')
        except ValueError:
            print('Вместо числа вы ввели строку, пожалуйста введите число')
        except ZeroDivisionError:
            print('Делитель (второе число) не может быть нулём')
        calc()


if __name__ == "__main__":
    calc()
