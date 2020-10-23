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

translate = {'0': 0,
             '1': 1,
             '2': 2,
             '3': 3,
             '4': 4,
             '5': 5,
             '6': 6,
             '7': 7,
             '8': 8,
             '9': 9,
             'A': 10,
             'B': 11,
             'C': 12,
             'D': 13,
             'E': 14,
             'F': 15,
             0: '0',
             1: '1',
             2: '2',
             3: '3',
             4: '4',
             5: '5',
             6: '6',
             7: '7',
             8: '8',
             9: '9',
             10: 'A',
             11: 'B',
             12: 'C',
             13: 'D',
             14: 'E',
             15: 'F'}



def add(l1, l2):
    d1 = collections.deque(l1)
    d2 = collections.deque(l2)

    res = collections.deque()
    p = 0
    while d1 and d2:
        el1 = translate[d1.pop()]
        el2 = translate[d2.pop()]
        sum = el1 + el2 + p
        p = sum // 16
        res.appendleft(translate[sum % 16])
    while d1:
        sum = translate[d1.pop()] + p
        res.appendleft(translate[sum % 16])
        p = sum // 16
    while d2:
        sum = translate[d2.pop()] + p
        res.appendleft(translate[sum % 16])
        p = sum // 16
    return res

def mul(l1, l2):
    d1 = collections.deque(l1)
    d2 = collections.deque(l2)

    res = collections.deque()
    p = 0
    while d1 and d2:
        el1 = translate[d1.pop()]
        el2 = translate[d2.pop()]
        mul = el1 * el2 + p
        p = mul // 16
        res.appendleft(translate[mul % 16])
    while d1:
        mul = translate[d1.pop()] + p
        res.appendleft(translate[mul % 16])
        p = mul // 16
    while d2:
        mul = translate[d2.pop()] + p
        res.appendleft(translate[mul % 16])
        p = mul // 16
    return res




l1 = list(input('Введите первое шестнадцатиричное число: ').upper())
l2 = list(input('Введите второе шестнадцатиричное число: ').upper())

print(add(l1, l2))


class Hexadecimal:

    translate = {'0': 0,
                 '1': 1,
                 '2': 2,
                 '3': 3,
                 '4': 4,
                 '5': 5,
                 '6': 6,
                 '7': 7,
                 '8': 8,
                 '9': 9,
                 'A': 10,
                 'B': 11,
                 'C': 12,
                 'D': 13,
                 'E': 14,
                 'F': 15,
                 0: '0',
                 1: '1',
                 2: '2',
                 3: '3',
                 4: '4',
                 5: '5',
                 6: '6',
                 7: '7',
                 8: '8',
                 9: '9',
                 10: 'A',
                 11: 'B',
                 12: 'C',
                 13: 'D',
                 14: 'E',
                 15: 'F'}

    def __init__(self, lst):
        self.lst = lst[:]

    def __str__(self):
        return str(self.lst)

    def __add__(self, other):
        res = []
        p = 0
        for i in range(max(len(self.lst), len(other.lst))):
            el1 = self.lst[-i-1] if i < len(self.lst) else '0'
            el2 = other.lst[-i-1] if i < len(other.lst) else '0'
            sum = translate[el1] + translate[el2] + p
            p = sum // 16
            res.append(translate[sum % 16])
        return Hexadecimal(res[::-1])


    def __mul__(self, other):
        res = Hexadecimal([])
        count = 0
        for el2 in other.lst[::-1]:
            buf = []
            p = 0
            for el1 in self.lst[::-1]:
                m = translate[el1] * translate[el2] + p
                p = m // 16
                buf.append(translate[m % 16])
            if p:
                buf.append(translate[p])
            buf = buf[::-1]
            for i in range(count):
                buf.append(translate[0])
            count += 1
            res = res + Hexadecimal(buf)

        return res


x = list(input('Введите первое шестнадцатиричное число: ').upper())
a = Hexadecimal(x)
y = list(input('Введите второе шестнадцатиричное число: ').upper())
b = Hexadecimal(y)

print(a + b)
print(a * b)

