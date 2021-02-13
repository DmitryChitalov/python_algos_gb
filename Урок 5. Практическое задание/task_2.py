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
import collections
import functools


def hex_calc(in_dict):
    v_sum = sum([int(''.join(i), 16) for i in in_dict.values()])
    print('Sum is {:x}'.format(v_sum))

    v_mul = functools.reduce((lambda a, b: a * b), [int(''.join(i), 16) for i in in_dict.values()])
    print('Mult is {:x}'.format(v_mul))


class MyHex:
    def __init__(self, in_hex=None):
        if in_hex != None:
            self.value = int(in_hex, 16)
        else:
            self.value = 0

    def set_str_val(self, in_val):
        self.value = int(in_val, 16)

    def get_int_val(self):
        return self.value

    def get_str_val(self):
        return '{:x}'.format(self.value)

    def sum_hex(self, in_hex):
        return MyHex('{:x}'.format(self.value + in_hex.get_int_val()))

    def mul_hex(self, in_hex):
        return MyHex('{:x}'.format(self.value * in_hex.get_int_val()))


v1 = MyHex()
v2 = MyHex()
res = MyHex()

nums_list = collections.defaultdict(list)
for n in range(2):
    print('Input hex value ' + str(n + 1) + ':')
    num = input()
    nums_list[f'{n + 1}'] = list(num)
    if n == 0:
        v1.set_str_val(num)
    else:
        v2.set_str_val(num)

hex_calc(nums_list)
res = v1.sum_hex(v2)
print(res.get_str_val())
res = v1.mul_hex(v2)
print(res.get_str_val())
