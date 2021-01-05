"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from random import randint
from timeit import timeit

dct = {i: randint(1, 100) for i in range(100)}
or_dct = OrderedDict({i: randint(1, 100) for i in range(100)})


def func1():
    for key in dct.keys():
        dct[key] += 1


def func2():
    for key in or_dct.keys():
        or_dct[key] += 1


print('Замеры вставки элементов: ')
print(f'Dict update:\t{timeit("dct.update({999: 9999})", setup="from __main__ import dct", number=10000)}')
print(f'OrderedDict update:\t{timeit("or_dct.update({999: 9999})", setup="from __main__ import or_dct", number=10000)}')

"""
Замеры вставки элементов: 
Dict update:	0.002884986999561079
OrderedDict update:	0.004725274000520585
"""

print('Замеры доступа к элементам: ')
print(f'Dict get:\t{timeit("dct.get(30)", setup="from __main__ import dct", number=10000)}')
print(f'OrderedDict get:\t{timeit("or_dct.get(30)", setup="from __main__ import or_dct", number=10000)}')

"""
Замеры доступа к элементам: 
Dict get:	0.0009496410020801704
OrderedDict get:	0.001021346000925405
"""

print(f'Dict func1:\t{timeit("func1()", setup="from __main__ import func1, dct", number=10000)}')
print(f'OrderedDict func2:\t{timeit("func2()", setup="from __main__ import func2, or_dct", number=10000)}')

"""
Dict func1:	0.19215378599983524
OrderedDict func2:	0.21988314400005038
"""

print('Move to end: ')
print(f'Dict:\t{timeit("dct[4] = dct.pop(4)", setup="from __main__ import func1, dct", number=10000)}')
print(f'OrderedDict:\t{timeit("or_dct.move_to_end(4)", setup="from __main__ import func2, or_dct", number=10000)}')

"""
Move to end: 
Dict:	0.0018268919993715826
OrderedDict:	0.0007424750001518987
"""

# По замерам, в большинстве случаев обычный словарь оказался быстрее.
# Исключение составил случай использования метода move_to_end в OrderedDict, которого нет обычном словаре.
# Можно сделать вывод, что применение OrderedDict может быть оправдано, если есть неоходимость менять порядок
# записей в словаре и есть необходимость в использовании отсутсвующего в обычном словаре метода move_to_end.
# В остальных случаях (для последних версиях python, где обычный словарь так же сохраняет порядок элементов)
# в использовании OrderedDict смысла нет.
