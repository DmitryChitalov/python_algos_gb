"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""

from collections import deque, namedtuple


def hex_calc_addition(_list):
    result = 0
    for el in _list:
        result += int(''.join(el.value), 16)
    return list(hex(result)[2:].upper())


def hex_calc_multiplication(_list):
    _numbers = deque([])
    for el in _list:
        _numbers.append(int(''.join(el.value), 16))
    return list(hex(_numbers[0] * _numbers[1])[2:].upper())


def hex_calculate():
    my_col = namedtuple('number', 'value')
    numbers = []
    for el in range(0, 2):
        _my_col = my_col(
            value=list(input(f'Введите {el + 1} шестнадцатеричное число: '))
        )
        numbers.append(_my_col)
    operand = input('Что нужно сделать с числом (* или +): ')
    if operand == '*':
        return hex_calc_multiplication(numbers)
    elif operand == '+':
        return hex_calc_addition(numbers)
    else:
        return print('Что-то не так с операндом!')


print(f'Результат: {hex_calculate()}')
