"""
2.*	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

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
from functools import reduce


def get_int_from_hex_list(hex_number: list) -> int:
    return int(''.join(hex_number), 16)


def without_OOP():
    numbers = defaultdict(list)
    numbers[1] = list(input(f"Введите первое шестнадцатиричное число > "))
    numbers[2] = list(input(f"Введите второе шестнадцатиричное число > "))
    print(*numbers.values())
    print("Сумма: ", format(sum([get_int_from_hex_list(number) for number in numbers.values()]), 'x'))
    print("Произведение: ", format(reduce(lambda result, current: result * current,
                                          [get_int_from_hex_list(number) for number in numbers.values()]), 'x'))


class HexNumber:
    def __init__(self, hex_number: list):
        self.hex_number = hex_number

    def get_int(self) -> int:
        return int(''.join(self.hex_number), 16)

    def __add__(self, other: 'HexNumber') -> 'HexNumber':
        return HexNumber(hex(self.get_int() + other.get_int()))

    def __mul__(self, other: 'HexNumber') -> 'HexNumber':
        return HexNumber(hex(self.get_int() * other.get_int()))

    def __str__(self) -> str:
        return format(self.get_int(), 'x').upper()


def with_OOP():
    first = HexNumber(list(input('Введите первое шестнадцатиричное число: ')))
    second = HexNumber(list(input('Введите второе шестнадцатиричное число: ')))
    print(f'Сумма чисел = {first + second}')
    print(f'Произведение чисел = {first * second}')


without_OOP()
with_OOP()
