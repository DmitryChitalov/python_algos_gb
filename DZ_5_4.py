"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
import timeit

time_Dict = """
a = {a: a ** 2 for a in range(100000)}
"""
time_OrderedDict = """
from collections import OrderedDict
b = {b: b ** 2 for b in range(100000)}
new_b = OrderedDict(b)
"""

elapsed_time_Dict = timeit.timeit(time_Dict, number=100)
print(f"Время Dict {elapsed_time_Dict}")
elapsed_time_OrderedDict = timeit.timeit(time_OrderedDict, number=100)
print(f"Время OrderedDict {elapsed_time_OrderedDict}")

#  Очевидно что обычный Dict работает быстрее, и к тому же в версии 3.6 сортировка стала по умолчанию
#  Соответственно использование OrderedDict отпадает.
