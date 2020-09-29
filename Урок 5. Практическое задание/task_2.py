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
from functools import reduce
from collections import deque, defaultdict


# def str_in_deque(n):
#     deq = deque()
#     for el in n:
#         deq.append(el)
#     return deq


def sum_func(a, b):
    res_list = deque([])
    if len(a) < len(b):
        n = len(b) - len(a)
        my_list = []
        for j in range(n):
            a.insert(0, '0')
        a = my_list + a
    elif len(b) < len(a):
        n = len(a) - len(b)
        my_list = []
        for j in range(n):
            b.insert(0, '0')
        b = my_list + b
    i = len(b) - 1
    one = 0
    for el in a[::-1]:
        r = numbers_1[el] + one + numbers_1[b[i]]
        if r < 16:
            res_list.appendleft(numbers_2[r])
            one = 0
        else:
            r -= 16
            one = 1
            res_list.appendleft(numbers_2[r])
        i -= 1
    return res_list


numbers_1 = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15,
    '10': 16
}
numbers_2 = {
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
    10: 'a',
    11: 'b',
    12: 'c',
    13: 'd',
    14: 'e',
    15: 'f',
    16: '10'
}

print(sum_func(['a', '2'], ['c', '4', 'f']))

# number = ['a2', 'c4f']
# summ = reduce(lambda x, y: int(x, 16) + int(y, 16), number)
# poww = reduce(lambda x, y: int(x, 16) * int(y, 16), number)
# print(hex(summ))
# print(hex(poww))
