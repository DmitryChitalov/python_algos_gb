"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit


ex1 = {i: i*i for i in range(10000000)}
ex2 = OrderedDict(ex1)


st1 = '''
for i in list(ex1):
    del ex1[i]
'''

st2 = '''
for i in list(ex2):
    del ex2[i]
'''

st3 = '''
for i in range(10000000, 10000000*2):
    ex1[i] = i*3
'''

st4 = '''
for i in range(10000000, 10000000*2):
    ex2[i] = i*3
'''

st5 = '''
for i in range(1000):
    val = ex1[i]
'''

st6 = '''
for i in range(1000):
    val = ex2[i]
'''

print('Удаление элементов')
print('Dict: ', timeit(st1, globals=globals(), number=1))
print('OrderedDict: ', timeit(st2, globals=globals(), number=1))

ex1 = {i: i*i for i in range(10000)}
ex2 = OrderedDict(ex1)

print('Добавление элементов')
print('Dict: ', timeit(st3, globals=globals(), number=1))
print('OrderedDict: ', timeit(st4, globals=globals(), number=1))

ex1 = {i: i*i for i in range(1000)}
ex2 = OrderedDict(ex1)

print('Взятие элемента по ключу: ')
print('Dict: ', timeit(st5, globals=globals()))
print('OrderedDict: ', timeit(st6, globals=globals()))


"""
Удаление элементов
Dict:  0.8832193569999998
OrderedDict:  1.601314584999999
Добавление элементов
Dict:  1.7728807950000007
OrderedDict:  2.2451694349999993
Взятие элемента по ключу: 
Dict:  91.312951803
OrderedDict:  98.90433418299999

Как видно из результатов замеров, все операции в OrderedDict делаются медленнее, чем в обычном Dict. 
Причем по функционалу оба типа абсолютно идентичны, из чего можно сделать вывод, что для версий Python
3.6+ (в которых словарь по умолчанию сортированный) OrderedDict вообще бесполезен.
"""
