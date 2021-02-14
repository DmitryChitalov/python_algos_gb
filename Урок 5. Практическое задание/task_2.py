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
"""
	1. вариант
defaultdict(list)
int(, 16)
reduce
2. вариант
class HexNumber:
    __add__
    __mul__
hx = HexNumber
hx + hx
"""
from collections import defaultdict


def def_hex(def_dict, hex_str):
    for i in hex_str:
        def_dict['let_16'].append(i.upper())


def_d1 = defaultdict(list)
def_d2 = defaultdict(list)
def_add = defaultdict(list)
def_mul = defaultdict(list)

print("collections")
v_1 = input("Введите первое число: ")
def_hex(def_d1, v_1)

v_2 = input("Введите второе число: ")
def_hex(def_d2, v_2)

res_add = int(v_1, 16) + int(v_2, 16)
def_hex(def_add, hex(res_add)[2:])
res_mul = int(v_1, 16) * int(v_2, 16)
def_hex(def_mul, hex(res_mul)[2:])

print(f'При сложении {def_d1["let_16"]} и {def_d2["let_16"]} получилось {def_add["let_16"]},'
      f' при умножении {def_mul["let_16"]}')

print("ООП")


class HexNumber:
    def __init__(self, hex_str):
        self.hex_list = [el.upper() for el in hex_str]

    def __add__(self, other):
        res_add = int(''.join(self.hex_list), 16) + int(''.join(other.hex_list), 16)
        return HexNumber(hex(res_add)[2:])

    def __mul__(self, other):
        res_mul = int(''.join(self.hex_list), 16) * int(''.join(other.hex_list), 16)
        return HexNumber(hex(res_mul)[2:])

    def __str__(self):
        return f'{self.hex_list}'


hn1 = HexNumber(input("Введите первое число: "))
hn2 = HexNumber(input("Введите второе число: "))
print(hn1)
print(hn2)
print(hn1 + hn2)
print(hn1 * hn2)
