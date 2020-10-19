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

from collections import deque, Counter
from functools import reduce


class HexNum:

    __hex_base = '0123456789ABCDEF'
    
    def __init__(self, hex_num):
        self.hex_num = deque(str(hex_num))
    
    @property
    def hexnum(self):
        return list(self.hex_num)
    
    @property
    def decnum(self):
        return int(str(self), 16)

    def __summ_hex(self, a, b):
        summ = deque()
        overflow = 0
        while len(a) > 0 or len(b) > 0:
            num_a = int(a.pop(), 16) if len(a) > 0 else 0
            num_b = int(b.pop(), 16) if len(b) > 0 else 0
            n = num_a + num_b + overflow
            # string_summ = (self.__hex_base[n % len(self.__hex_base)]) + string_summ
            summ.appendleft(self.__hex_base[n % len(self.__hex_base)])
            overflow = n // len(self.__hex_base)
        if overflow > 0:
            summ.appendleft(self.__hex_base[overflow])
        return summ
    
    def __str__(self):
        return ''.join(self.hex_num)
    
    def __add__(self, b):
        a = self.hex_num.copy()
        b = b.hex_num.copy()
        return HexNum(''.join(self.__summ_hex(a, b)))
    
    def __mul__(self, b):
        a = self.hex_num.copy()
        b = b.hex_num.copy()
        summ_1 = deque()
        overflow = 0
        level = ''
        while len(a) > 0:
            # print(a)
            num_a = int(a.pop(), 16) if len(a) > 0 else 0
            print(num_a)
            b2 = b.copy()
            summ_2 = deque(level)
            while len(b2) > 0:
                # print(b2)
                num_b = int(b2.pop(), 16) if len(b2) > 0 else 0
                print(num_b)
                n = num_a * num_b + overflow
                summ_2.appendleft(self.__hex_base[n % len(self.__hex_base)])
                overflow = n // len(self.__hex_base)
                # string_summ = (self.__hex_base[n % len(self.__hex_base)]) + string_summ
            if overflow > 0:
                summ_2.appendleft(self.__hex_base[overflow])
            summ_1.appendleft(summ_2)
            level += '0'
        # return summ_1
        return ''.join(reduce(self.__summ_hex, summ_1))
        # return summ_1





# a = HexNum('A2')
a = HexNum('a')
b = HexNum('C4F')

print(f"{a} = {a.decnum}")
print(f"{b} = {b.decnum}")

print(a)
print(b)

# tt = deque('A2')
# for i in range(4):
#     print(tt)
#     nn = int(tt.pop(), 16) if len(tt) > 0 else 0
#     print(nn)

# hex_base = '0123456789ABCDEF'
# print(hex_base[30 % 16])

c = b + a
print(c)

print(a)
print(b)
print(a * b)

# aa = Counter(a=0, b=0)
# print(aa)
