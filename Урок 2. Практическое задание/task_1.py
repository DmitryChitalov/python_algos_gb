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
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

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

def recursion_math_operation():

    menu_input = input('Please enter math operation: + , -,  *, /,   or "0" for exit program: ')

    if menu_input == '0':
        return 'Exit program'

    else:
        if menu_input == '+' or menu_input == '-' or menu_input == '*' or menu_input == '/':
            try:
                frst_number = int(input('Please enter first number: '))
                scnd_number = int(input('Please enter second number: '))

                if menu_input == '+':
                    result = frst_number + scnd_number
                    print(f'{frst_number} + {scnd_number} = {result}')
                    return  recursion_math_operation()

                elif menu_input == '-':
                    result = frst_number - scnd_number
                    print(f'{frst_number} - {scnd_number} = {result}')
                    return recursion_math_operation()

                elif menu_input == '*':
                    result = frst_number * scnd_number
                    print(f'{frst_number} * {scnd_number} = {result}')
                    return recursion_math_operation()

                elif menu_input == '/':
                    if scnd_number != 0:
                        result = frst_number / scnd_number
                        print(f'{frst_number} / {scnd_number} = {result}')
                        return recursion_math_operation()
                    else:
                        print(f'Error! Division by zero!')


            except ValueError:
                print('Error! Value error! Check that you enter numbers (3-digits)! ')
                return recursion_math_operation()

            except:
                print('Unknow Error! Try again.')
                return  recursion_math_operation()
        else:

            print(f'Error!')
            return recursion_math_operation()

print('Welcome to program "Math operation with recursion function"')
recursion_math_operation()