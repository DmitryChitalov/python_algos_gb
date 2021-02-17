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

hex_numbers = defaultdict(list)
str_number = input("Введите первое шестнадцатеричное число: ")
hex_numbers['hex_number_1'] = list(str_number)
str_number = input("Введите второе шестнадцатеричное число: ")
hex_numbers['hex_number_2'] = list(str_number)

summary = int(''.join(hex_numbers['hex_number_1']), 16) + \
    int(''.join(hex_numbers['hex_number_2']), 16)
print("Сумма = ", list('%X' % summary))
multiplication = int(''.join(hex_numbers['hex_number_1']), 16) * \
    int(''.join(hex_numbers['hex_number_2']), 16)
print("Произведение = ", list('%X' % multiplication))
