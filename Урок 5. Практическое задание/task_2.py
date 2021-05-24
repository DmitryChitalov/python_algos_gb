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
from collections import defaultdict
from functools import reduce


def hex_calc():
    numbers = defaultdict(list)
    input_first = input('Введи первое hex число: ')
    input_second = input('Введи второе hex число: ')
    numbers[f'1={input_first}'] = list(input_first)
    numbers[f'2={input_second}'] = list(input_second)
    print(numbers)
    sum_of_hex = sum([int(''.join(i), 16) for i in numbers.values()])
    print(sum_of_hex)
    print('Сумма :', list('%X' % sum_of_hex))
    multiply_of_hex = reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in numbers.values()])
    print('Произведение: ', list('%X' % multiply_of_hex))


hex_calc()

