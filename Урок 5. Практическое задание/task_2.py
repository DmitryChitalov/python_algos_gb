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


"""
Простое решение на ООП
"""


class HexCalc:
    def __init__(self, num1, num2):
        self.num1 = int(''.join(num1), 16)
        self.num2 = int(''.join(num2), 16)

    def hex_sum(self):
        return str(hex(self.num1 + self.num2)[2:]).upper()

    def hex_mtl(self):
        return str(hex(self.num1 * self.num2)[2:]).upper()


numbers = HexCalc(num1=input(f'Введите 1-e HEX число: '), num2=input(f'Введите 2-e HEX число: '))
print(f'Сумма чисел = {numbers.hex_sum()}')
print(f'Сумма чисел = {numbers.hex_mtl()}')


"""
С применением defaultdict
"""


class HexCalcTwo:
    def __init__(self):
        self.numbers = defaultdict()
        self.result_sum = 0
        self.result_mtl = 0
        self.num_input()

    def num_input(self):
        for el in range(2):
            self.numbers[el + 1] = list(input(f'Введите {el + 1}-e HEX число: '))
        return self.numbers

    def hex_sum_two(self):
        self.result_sum = sum([int("".join(el), 16) for el in self.numbers.values()])
        return print(f'Сумма чисел = {str(hex(self.result_sum)[2:]).upper()}')

    def hex_mtl_two(self):
        self.result_mtl = reduce(lambda x, y: x*y, [int("".join(el), 16) for el in self.numbers.values()])
        return print(f'Произведение чисел = {str(hex(self.result_mtl)[2:]).upper()}')


numbers_two = HexCalcTwo()
numbers_two.hex_sum_two()
numbers_two.hex_mtl_two()

