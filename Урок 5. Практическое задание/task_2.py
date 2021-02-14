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
from functools import reduce

try:
    hex1 = input("Введите первое hex число: ")
    hex1_check = int(hex1, 16)
    hex2 = input("Введите второе hex число: ")
    hex2_check = int(hex2, 16)
except ValueError:
    print("Введено не hex число")
    exit(0)

var = input("Введите 1 для выбора варианта через collections или 2 для варианта через ООП ")

if var == "1":

    hex_dict = defaultdict(list)
    hex_dict["H1-" + hex1] = list(hex1.upper())
    hex_dict["H2-" + hex2] = list(hex2.upper())

    print("Первое число: ", hex_dict["H1-" + hex1])
    print("Второе число: ", hex_dict["H2-" + hex2])

    sum_all = sum([int("".join(i), 16) for i in hex_dict.values()])
    mult_all = reduce(lambda x, y: x * y, [int("".join(i), 16) for i in hex_dict.values()])

    print(f"Сумма  чисел:  {list('%X' % sum_all)}")
    print(f"Произведение чисел {list('%X' % mult_all)}")


elif var == "2":

    print("\nРеализация через ООП:")

    class HexNumbers:

        def __init__(self, hexn):
            self.hex = list(hexn.upper())

        def __str__(self):
            return str(self.hex)

        def __add__(self, other):
            tmp_sum = int("".join(self.hex), 16) + int("".join(other.hex), 16)
            return HexNumbers(str('%X' % tmp_sum))

        def __mul__(self, other):
            tmp_mult = int("".join(self.hex), 16) * int("".join(other.hex), 16)
            return HexNumbers(str('%X' % tmp_mult))

    hex_class1 = HexNumbers(hex1)
    hex_class2 = HexNumbers(hex2)

    print(f"Первое число: {hex_class1}")
    print(f"Второе число: {hex_class2}")
    sum_all = hex_class1 + hex_class2
    mult_all = hex_class1 * hex_class2
    print(f"Сумма  чисел: {sum_all}")
    print(f"Произведение чисел: {mult_all}")

else:
    print("Неверный вариант. Завершение работы")
