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


class Int16:
    dic_base = defaultdict(str)
    dic_base[0] = '0'
    dic_base[1] = '1'
    dic_base[2] = '2'
    dic_base[3] = '3'
    dic_base[4] = '4'
    dic_base[5] = '5'
    dic_base[6] = '6'
    dic_base[7] = '7'
    dic_base[8] = '8'
    dic_base[9] = '9'
    dic_base[10] = 'A'
    dic_base[11] = 'B'
    dic_base[12] = 'C'
    dic_base[13] = 'D'
    dic_base[14] = 'E'
    dic_base[15] = 'F'

    def __init__(self, num16):
        self.n16 = num16
        self.n = int(num16, 16)

    def __add__(self, other):
        s = self.n + other.n
        s_st = ''
        while s > 0:
            s_st = self.dic_base[s % 16] + s_st
            s = s // 16
        return Int16(s_st)

    def __mul__(self, other):
        s = self.n * other.n
        s_st = ''
        while s > 0:
            s_st = self.dic_base[s % 16] + s_st
            s = s // 16
        return Int16(s_st)

    def __str__(self):
        return self.n16

    def to10(self):
        return self.n


if __name__ == '__main__':
    n1 = Int16('A2')
    n2 = Int16('C4F')
    print(f'{n1} = {n1.to10()}, {n2} = {n2.to10()}')
    print(f'{n1} + {n2} = {n1 + n2}')
    print(f'{n1} * {n2} = {n1 * n2}')
