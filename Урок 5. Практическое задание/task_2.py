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
from collections import defaultdict, deque


"""Решение с использованием defaultdict и deque"""


numbers = defaultdict(deque)

numbers['x'] = deque(input('Введите первое число: '))
numbers['y'] = deque(input('Введите второе число: '))
print(numbers.get('x'))
print(numbers.get('y'))

add = hex(int(''.join(numbers.get('x')), 16) + int(''.join(numbers.get('y')), 16))
print(deque(add[2:].upper()))

mul = hex(int(''.join(numbers.get('x')), 16) * int(''.join(numbers.get('y')), 16))
print(deque(mul[2:].upper()))


"""Решение с использованием ООП"""


class Hexadecimal:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return Hexadecimal(hex(int(self.a, 16) + int(other.a, 16)))

    def __mul__(self, other):
        return Hexadecimal(hex(int(self.a, 16) * int(other.a, 16)))

    def __str__(self):
        return str([i.upper() for i in self.a if i != '0' and i != 'x'])


x = Hexadecimal(input('Введите первое число: '))
y = Hexadecimal(input('Введите второе число: '))
print(x)
print(y)
print(x + y)
print(x * y)
