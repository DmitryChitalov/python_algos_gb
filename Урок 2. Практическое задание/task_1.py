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
def calc(boo = True, a = 0):
    z = input('+, -, *, / или 0 для выхода ')
    print(z)
    if z == '0':
        print('конец')
        return
    else:
        if boo == True:
            a = int(input('Введите первое число: '))
            if z == '+':
                a = a + int(input('Введите второе число: '))
            elif z == '-':
                a = a - int(input('Введите второе число: '))
            elif z == '*':
                a = a * int(input('Введите второе число: '))
            elif z == '/':
                a = a * int(input('Введите второе число: '))
            print(a)
            return calc(False, a)
        if boo != True:
            if z == '+':
                a = a + int(input('Введите число: '))
            elif z == '-':
                a = a - int(input('Введите число: '))
            elif z == '*':
                a = a * int(input('Введите число: '))
            elif z == '/':
                a = a * int(input('Введите число: '))
            print(a)
            calc(False, a)


            '''
            нужно срочно оптимизировать!
            дубли = плохо
            нужно запрашивать числа только один раз
            '''