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
########################################################################################################################

from collections import deque


number_one = input('Введите первое шестнадцатиричное число: ')
number_one = deque(number_one)
number_two = input('Введите второе шестнадцатиричное число: ')
number_two = deque(number_two)

result_sum = hex(int(''.join(number_one), 16) + int(''.join(number_two), 16))
print(deque(result_sum[2:].upper()))
result_mul = hex(int(''.join(number_one), 16) * int(''.join(number_two), 16))
print(deque(result_mul[2:].upper()))

########################################################################################################################


class Calculator:

    def __init__(self, one=input('number one: '), two=input('number two: ')):
        self.one = [i.upper() for i in one]
        self.two = [i.upper() for i in two]

    def __add__(self):
        result = hex(int(''.join(self.one), 16) + int(''.join(self.two), 16))
        result = [i.upper() for i in result]
        return result[2:]

    def __mul__(self):
        result = hex(int(''.join(self.one), 16) * int(''.join(self.two), 16))
        result = [i.upper() for i in result]
        return result[2:]


c = Calculator()
print(c.__add__())
print(c.__mul__())





