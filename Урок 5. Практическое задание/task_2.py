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
from collections import deque

HEX_DICT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
            'D': 13, 'E': 14, 'F': 15,
            0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
            13: 'D', 14: 'E', 15: 'F'}


def hex_input():
    __temp_number = input('Введите число в 16 системе счисления:').upper()
    try:
        int(__temp_number, 16)
        return list(__temp_number)
    except:
        print('Вы ввели неправильное число, оно должно состоять из [0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F]')
        return hex_input()

def hex_sum(first,second):
    __sum = deque()
    __over_digit = 0
    if len(first) < len(second):
        __first, __second = second, first
    else:
        __first, __second = first, second
    while __first:
        if __second:
            __res = HEX_DICT[__first.pop()] + HEX_DICT[__second.pop()] + __over_digit
        else:
            __res = HEX_DICT[__first.pop()] + __over_digit
        __over_digit = 0
        if __res < 16:
            __sum.appendleft(HEX_DICT[__res])
        else:
            __sum.appendleft(HEX_DICT[__res - 16])
            __over_digit = 1
    if __over_digit:
        __sum.appendleft('1')
    return list(__sum)

def hex_multiply(first,second):
    __mult = deque()
    __digits = deque([deque() for _ in range(len(second))])
    __first, __second = first.copy(), second.copy()
    for i in range(len(__second)):
        m = HEX_DICT[__second.pop()]
        for j in range(len(__first) - 1, -1, -1):
            __digits[i].appendleft(m * HEX_DICT[__first[j]])
        for _ in range(i):
            __digits[i].append(0)
    __over_digit = 0
    for _ in range(len(__digits[-1])):
        __res = __over_digit
        for i in range(len(__digits)):
            if __digits[i]:
                __res += __digits[i].pop()
        if __res < 16:
            __mult.appendleft(HEX_DICT[__res])
        else:
            __mult.appendleft(HEX_DICT[__res % 16])
            __over_digit = __res // 16
    if __over_digit:
        __mult.appendleft(HEX_DICT[__over_digit])
    return list(__mult)

print(hex_sum(hex_input(),hex_input()))
print(hex_multiply(hex_input(),hex_input()))

class HexNumber:

    def __init__(self,hexrepr):
        self.hexrepr = hexrepr
        self.decimal = int("".join(hexrepr),16)

    def __add__(self, other):
        if (not isinstance(other, HexNumber)):
            raise ArithmeticError("Попытка операции с не 16 числом")
        return HexNumber(list(format(self.decimal + other.decimal,'X')))

    def __mul__(self, other):
        if (not isinstance(other, HexNumber)):
            raise ArithmeticError("Попытка операции с не 16 числом")
        return HexNumber(list(format(self.decimal * other.decimal,'X')))

    def __str__(self):
        return str(self.hexrepr)

op1 = HexNumber(hex_input())
op2 = HexNumber(hex_input())

print(op1+op2)
print(op1*op2)
