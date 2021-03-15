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


class HexNumber:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return HexNumber(hex(int(self.x, 16) + int(other.x, 16)))

    def __mul__(self, other):
        return HexNumber(hex(int(self.x, 16) * int(other.x, 16)))

    def __str__(self):
        return self.x


a = input('Введите 1-е шестнадцатиричное число: ').upper()
b = input('Введите 2-е шестнадцатиричное число: ').upper()

a_class = HexNumber(str(a))
b_class = HexNumber(str(b))

c_class = a_class + b_class

print(f'сумма: {c_class}')

d_class = a_class * b_class
print(f'произведение: {d_class}')

ddict = defaultdict(str)
ddict[a] = list(a)
ddict[b] = list(b)

print(hex(int(''.join(ddict[a]), 16) + int(''.join(ddict[b]), 16)))
print(hex(int(''.join(ddict[a]), 16) * int(''.join(ddict[b]), 16)))

"""
сделал через ООП.
попытался прикрутить defaultdict, но так не понял зачем
"""
