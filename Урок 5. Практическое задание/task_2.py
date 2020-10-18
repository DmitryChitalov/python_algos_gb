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

HEX = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
HEX_2_DEC = {HEX[i]: i for i in range(len(HEX))}
DEC_2_HEX = {i: HEX[i] for i in range(len(HEX))}
MY_BASE = 16


# Функции не были перенесены в методы класса для тестов
class HexNum:
    def __init__(self, hex_str):
        self.hex = list(hex_str)
        self.int = hex_2_dec(self.hex)

    def __add__(self, other):
        return HexNum(dec_2_hex(self.int + other.int))

    def __mul__(self, other):
        return HexNum(dec_2_hex(self.int * other.int))


def hex_2_dec(hex_num):
    num = 0
    for item in hex_num:
        num *= MY_BASE
        num += HEX_2_DEC[item]
    return num


def dec_2_hex(dec_num):
    hx_num = deque()
    while dec_num > 0:
        item = dec_num % MY_BASE
        dec_num //= MY_BASE
        hx_num.appendleft(DEC_2_HEX[item])
    return list(hx_num)


hex_arr1 = ['A', '2']
hex_arr2 = ['C', '4', 'F']

print(dec_2_hex(hex_2_dec(hex_arr1) + hex_2_dec(hex_arr2)))
print(dec_2_hex(hex_2_dec(hex_arr1) * hex_2_dec(hex_arr2)))

num1 = HexNum(hex_arr1)
num2 = HexNum(hex_arr2)

num3 = num1 + num2
num4 = num1 * num2

print(num3.hex)
print(num4.hex)
