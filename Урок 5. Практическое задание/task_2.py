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


def hex_op():
    number_hex = defaultdict(list)
    number_1 = input("Введите первое натуральное 16 ричное число : ")
    number_hex[1] = list(number_1)
    number_2 = input("Введите второе натуральное 16 ричное число : ")
    number_hex[2] = list(number_2)
    print("Сумма ", hex(int("".join(number_hex.get(1)), 16) + int("".join(number_hex.get(2)), 16)))
    print("Произведение ", hex(int("".join(number_hex.get(1)), 16) * int("".join(number_hex.get(2)), 16)))


hex_op()


class Hex_num:
    __num = ()

    def set_num(self):
        number = input("Введите натуральное 16 ричное число : ")
        self.__num = list(number)

    def get(self):
        return self.__num

    def __add__(self, other):
        return hex(int("".join(self.__num), 16) + int("".join(other.get()), 16))

    def __mul__(self, other):
        return hex(int("".join(self.__num), 16) * int("".join(other.get()), 16))


n1 = Hex_num()
n2 = Hex_num()

n1.set_num()
n2.set_num()

print(f"{n1.get()} + {n2.get()} = {n1 + n2}")
print(f"{n1.get()} * {n2.get()} = {n1 * n2}")
