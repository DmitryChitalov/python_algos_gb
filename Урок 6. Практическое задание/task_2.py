"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
from collections import namedtuple
import recordclass
from pympler import asizeof

# Список списков с координатами точек
points = []
for i in range(100000):
    points.append([i, i, i])
print(asizeof.asizeof(points))  # 12824456

# Список именованных кортежей с координатами точек
Point = namedtuple('Point', ('x', 'y', 'z'))
points = []
for i in range(100000):
     points.append(Point(i, i, i))
print(asizeof.asizeof(points))  # 11224456

# Список "изменяемых кортежей" с координатами точек
Point = recordclass.recordclass('Point', ('x', 'y', 'z'))
points = []
for i in range(100000):
    points.append(Point(i, i, i))
print(asizeof.asizeof(points))  # 5625192
# Потребление памяти снижено вследствие того, что экземпляры класса
# recordclass не участвуют в механизме циклической сборки мусора.

# Ещё одна вариация класса из модуля recordclass
Point = recordclass.make_dataclass('Point', ('x', 'y', 'z'))
points = []
for i in range(100000):
    points.append(Point(i, i, i))
print(asizeof.asizeof(points))  # 4824464