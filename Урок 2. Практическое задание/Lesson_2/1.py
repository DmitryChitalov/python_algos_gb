Введите операцию (+, -, *, / или 0 для выхода):
"""	"""

def calc():
    operation = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if operation == '0':
        print('Программа завершена')
        return
    elif operation in ('+','-','*','/'):
        try:
            print(number(operation))
        except ZeroDivisionError:
            print('На 0 делить нельзя, исправьтесь')
        return calc()

    else:
        print('Данную операцию программа не поддерживает, повторите попытку')
        return calc()


def number(operation):
    try:
        num_1 = int(input('Введите первое число:'))
        num_2 = int(input('Введите первое число:'))
    except ValueError:
        print('Вы вместо числа ввели строку (((. Исправьтесь')
        return number(operation)
    return eval(str(num_1) + operation + str(num_2))


calc()