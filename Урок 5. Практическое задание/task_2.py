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


class HexDigit:
    def __init__(self, number):
        self.digits = list(number)

    def __str__(self):
        return ''.join(self.digits)

    def __add__(self, other):
        return hex(int(self) + int(other))

    def __mul__(self, other):
        return hex(int(self) * int(other))

    def __int__(self):
        return int(str(self), 16)


class HexOperations:
    def __init__(self, operandA, operandB):
        self.operands = defaultdict(HexDigit)
        self.operands['A'] = operandA
        self.operands['B'] = operandB

    def sum_operands(self):
        return self.operands['A'] + self.operands['B']

    def mul_operands(self):
        return self.operands['A'] * self.operands['B']

d1 = HexDigit("A2")
d2 = HexDigit("C4F")
hex_operation = HexOperations(d1, d2)

print(hex_operation.mul_operands())