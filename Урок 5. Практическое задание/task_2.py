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

import collections, functools

def calc_num(numbers):
    summ_numbers = sum([int(''.join(i), 16) for i in numbers.values()])
    print("Сумма: ", list('%X' % summ_numbers))

    mul_numbers = functools.reduce(lambda x, y: x * y, [int(''.join(i), 16) for i in numbers.values()])
    print("Произведение: ", list('%X' % mul_numbers))

numbers = collections.defaultdict(list)
for i in range(2):
    el = input(f"Введите {i+1}-е натуральное шестнадцатиричное число: ")
    numbers[f"{i+1}-{el}"] = list(el)

calc_num(numbers)