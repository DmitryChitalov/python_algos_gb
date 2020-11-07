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


# import collections
# import functools
#
#
# def calc():
#     nums = collections.defaultdict(list)
#     # defaultdict(<class 'list'>, {'1-A2': ['A', '2'], '2-CF4': ['C', '4', 'F']})
#     for d in range(2):
#         n = input(f'Введите {d + 1}-e натуральное 16 яичное число')
#         nums[f'{d + 1}-{n}'] = list(n)
#     print(nums)
#
#     summ = sum([int(''.join(i), 16) for i in nums.values()])
#     # '%X' число в 16 си (буквы в верхнем регистре)
#     print('Сумма ', list('%X' % summ))
#     #reduce - применение функции к каждому эл коллекции
#     mult = functools.reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in nums.values()])
#     print('Произведение ', list('%X' % mult))
#
#
# calc()
# ---------------------------------seccond---------------------------------
class HexOperation:
    def __init__(self, num_first, num_second):
        self.num_first = num_first
        self.num_second = num_second

    def __add__(self, other):
        return list(hex(int(''.join(self.num_first), 16) + int(''.join(other.num_second), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.num_first), 16) * int(''.join(other.num_second), 16)))[2:]


hex_num_first = list(input('Первое 16 число'))
hex_num_second = list(input('Второе 16 число'))

res_sum = HexOperation(hex_num_first, hex_num_second) + HexOperation(hex_num_first, hex_num_second)
res_mul = HexOperation(hex_num_first, hex_num_second) * HexOperation(hex_num_first, hex_num_second)

print(f'Сумма чисел = {res_sum}\nПроизведение = {res_mul}')
