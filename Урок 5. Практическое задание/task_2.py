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


number_a = input("Введите первое шестнадцатиричное число: ")
number_b = input("Введите второе шестнадцатиричное число: ")

hex_dict = defaultdict(list)
hex_dict["number_a"] = list(number_a)
hex_dict["number_b"] = list(number_b)

res_plus = int("".join(hex_dict.get("number_a")), 16) + int("".join(hex_dict.get("number_b")), 16)
res_mul = int("".join(hex_dict.get("number_a")), 16) * int("".join(hex_dict.get("number_b")), 16)
print(f"Сумма: {list(str(hex(res_plus))[2:].upper())}")
print(f"Произведение: {list(str(hex(res_mul))[2:].upper())}")


""" Решение с помощью ООП 
    Оставила строки просто чтоб не переводить туда-сюда. Но в принципе можно было hex_number определить как List
"""
class HexNumber:

    hex_number: str

    def __init__(self, i_hex):
        try:
            int(i_hex, 16)
        except ValueError:
            print("Неверное представление шестнадцатиричного числа! ")
            exit()
        self.hex_number = i_hex

    def __add__(self, other):
        return str(hex(int(self.hex_number, 16) + int(other.hex_number, 16)))[2:].upper()

    def __mul__(self, other):
        return str(hex(int(self.hex_number, 16) * int(other.hex_number, 16)))[2:].upper()


hexnum_a = HexNumber(number_a)
hexnum_b = HexNumber(number_b)
print(hexnum_a + hexnum_b)
print(hexnum_a * hexnum_b)

