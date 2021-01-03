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

"""С применением defaultdict"""
d = defaultdict(list)
d["first"] = list(input("Введите первое шеснадцатиричное число: ").upper())
d["second"] = list(input("Введите второе шеснадцатиричное число: ").upper())
d['sum'] = hex(int(''.join(d['first']),16) + int(''.join(d['second']),16))[2:].upper()
d['mul'] = hex(int(''.join(d['first']),16) * int(''.join(d['second']),16))[2:].upper()
print("Сумма равна: ", d['sum'])
print("Произведение равно: ", d['mul'])

"""С применением ООП"""
class HexNumber:
    def __init__(self, number):
        try:
            self._from_hex = int(number, 16)
        except Exception as e:
            print("Неверное значение: ", e)
            self._from_hex = 0
    def __add__(self, other):
        return hex(self._from_hex + other._from_hex).upper()[2:]
    def __mul__(self, other):
        return hex(self._from_hex * other._from_hex).upper()[2:]

h1 = HexNumber('A2')
h2 = HexNumber('c4f')
print("Сумма равна: ", h1 + h2)
print("Произведение равно: ", h1 * h2)