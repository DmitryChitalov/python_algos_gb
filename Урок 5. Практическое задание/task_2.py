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

from collections import namedtuple

num_template = namedtuple("num_template", ["one", "two"])

hex_num = num_template(
    one=list(input("Введите 1-е 16-е число: ").upper()),
    two=list(input("Введите 2-е 16-е число: ").upper())
)

int_num = num_template(
    one=int(''.join(hex_num.one), base=16),
    two=int(''.join(hex_num.two), base=16),
)

sum_num = list(hex(int_num.one + int_num.two)[2:].upper())
mul_num = list(hex(int_num.one * int_num.two)[2:].upper())

print("Решение через collections")
print(f"Сумма чисел - {sum_num}")
print(f"Произведение чисел - {mul_num}")


# Решение через ООП

class HexNumber:
    def __init__(self, num: str):
        self.num = list(num.upper())

    def __str__(self):
        return ''.join(self.num)

    def __add__(self, other):
        if isinstance(other, HexNumber):
            return list(hex(int(''.join(self.num), base=16) + int(''.join(other.num), base=16))[2:].upper())
        else:
            return False

    def __mul__(self, other):
        if isinstance(other, HexNumber):
            return list(hex(int(''.join(self.num), base=16) * int(''.join(other.num), base=16))[2:].upper())
        else:
            return False


print("Решение через ООП")
one_num = HexNumber(input("Введите 1-е 16-е число: "))
two_num = HexNumber(input("Введите 2-е 16-е число: "))
print(f"Сумма чисел - {one_num + two_num}")
print(f"Произведение чисел - {one_num * two_num}")
