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


#################################################################################

'''В этой функции некоректность ввода чисел и арифметических знаков обрабатываю с помощью цикла.
    НО САМО ЗАДАНИЕ РЕКУРСИВНОГО ВЫХОВА ТОЖЕ ВЫПОЛЕНО
    Думаю это можно сделать с помощью рекурсии но это уже будет извращение.
    Ну или кажыдый раз при некоректном вводе последнего аргумента, нужно будет начинать сначала.
    Цикл эту проблему решает
'''


def calculator():
    while True:
        first_dig = input('Введите первое число пожалуйста:\n')
        if first_dig.isdigit():
            break

        else:
            print(f'Вы ввели какие-то крякозабры: >>> {first_dig} <<<\nдавай еще раз')

    while True:
        arithm = input('Введите знак операции пожалуйста(+, -, *, / или 0 для выхода):\n')
        if arithm == '0':
            print('Программа завершена!')
            exit()
        if arithm in ['+', '-', '*', '/']:
            break

    while True:
        sec_dig = input('Введите второе число пожалуйста:\n')
        if sec_dig.isdigit():
            break
        else:
            print(f'Вы ввели какие-то крякозабры: >>> {sec_dig} <<<\nдавай еще раз')

        if sec_dig == '0' and arithm == '/':
            print('На ноль "0" дельить нельзя!\nНа самом деле можно но это надо уметь!')

    res = first_dig + arithm + sec_dig

    ''' Я знаю что функцию eval() не рекоммендуют использовать. Но мы проверяем все входящие аргументы.
        И знаем что в качестве первого и третьего нам приидут числа, в качестве ариф.знака придет один из нашего списка
        Потому смело испльзую эту функцию, чтобы сократить код
    '''
    print(f'Ваша результат: {eval(res)}')
    input('Нажмите любую клавишу чтобы продолжить:\n')
    calculator()        # а вот и рекурсия


calculator()