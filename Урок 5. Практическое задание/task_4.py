"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
import timeit

STR_CODE_1 = '''
d = {}
for i in range(5):
    d[i] = i
print(d)
d[3] = 18
print(d)
'''
STR_CODE_2 = '''
import collections
od = collections.OrderedDict()
for i in range(5):
    od[i] = i
print(od)
od[3] = 18
print(od)
'''

print(timeit.timeit(STR_CODE_1, number=10)) #0.0001902350000000004
print(timeit.timeit(STR_CODE_2, number=10)) #0.004831584  OrderedDict медленнее