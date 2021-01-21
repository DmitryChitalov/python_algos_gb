"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, библиотеки) для оптимизации памяти и
доказать! (наглядно, кодом) их эффективность (на примере профилировщика)
"""

"""
Использование __slots__ для объектов
"""
import numpy as np
from pympler import asizeof


class DefaultObject:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class SlotsObject:
    __slots__ = ('name', 'age', 'address')

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


d1 = DefaultObject("Alex", 42, "-")
d2 = DefaultObject("Boris", 24, "In the middle of nowhere")
s1 = SlotsObject("Alex", 42, "-")
s2 = SlotsObject("Boris", 24, "In the middle of nowhere")

print(f'd1 => {asizeof.asizeof(d1)}')
print(f'd2 => {asizeof.asizeof(d2)}')
print(f's1 => {asizeof.asizeof(s1)}')
print(f's2 => {asizeof.asizeof(s2)}')

"""
Видим, что вариант с использованием __slots__ сокращает потребление памяти почти в 2.5 раза
d1 => 464
d2 => 488
s1 => 200
s2 => 224
"""

"""
использование numpy для работы с массивами
"""
lst = [el for el in range(1000)]
arr = np.array([el for el in range(1000)])
print(f'default list => {asizeof.asizeof(lst)}')
print(f'numpy array => {asizeof.asizeof(arr)}')
"""
Видим, что массив в numpy занимает сильно меньше памяти
default list => 40848
numpy array => 8112
"""
