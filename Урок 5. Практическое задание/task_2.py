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


# функцию написал сам. Стараюсь "подсматривать" как можно меньше.
# Буду использовать в будущих проектах, т.к. надоело каждый раз писать проверки пользовательского ввода
def get_hex_num(msg='', err=''):
    while True:
        res = input(('Enter HEX number: ', msg)[bool(msg)])
        if res != '':
            if min(['0123456789ABCDEFabcdef'.count(s) for s in res]):
                return res.upper()
        print(('Error!', err)[bool(err)])


nums = {'num1': get_hex_num('Введите первое число в шестнадцатиричной системе счисления: ',
                            'Ошибка, требуется повторный ввод.'),
        'num2': get_hex_num('Введите второе число в шестнадцатиричной системе счисления: ',
                            'Ошибка, требуется повторный ввод.')}

#  Способ с defaultdict
print('\nС использованием defaultdict модуля collections')
nums_def_dict = defaultdict(int, {k: list(v) for k, v in nums.items()})
sum_hex = sum([int(''.join(n), 16) for n in nums_def_dict.values()])
mul_hex = reduce(lambda x, y: x * y, [int(''.join(n), 16) for n in nums_def_dict.values()])
print(f'Сумма: {"%X" % sum_hex}')
print(f'Произведение: {"%X" % mul_hex}')

#  Способ через ООП
print('\nС использованием ООП')


class HexAddMulClass:
    def __init__(self, hex_num):
        self.__hex_num_lst = list(hex_num)

    def __add__(self, other):
        return int(''.join(self.__hex_num_lst), 16) + int(''.join(other.__hex_num_lst), 16)

    def __mul__(self, other):
        return int(''.join(self.__hex_num_lst), 16) * int(''.join(other.__hex_num_lst), 16)


n1 = HexAddMulClass(nums['num1'])
n2 = HexAddMulClass(nums['num2'])
print(f'Сумма: {"%X" % (n1 + n2)}')
print(f'Произведение: {"%X" % (n1 * n2)}')
