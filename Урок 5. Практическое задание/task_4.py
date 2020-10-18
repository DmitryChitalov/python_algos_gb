"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from timeit import timeit
from random import randint

list_upto_hund1 = [randint(1, 100) for i in range(100)]
list_upto_th1 = [randint(1, 100) for i in range(1000)]

list_upto_hund2 = [randint(1, 1000) for i in range(100)]
list_upto_th2 = [randint(1, 1000) for i in range(1000)]

test_dict = {}
test_ordereddict = OrderedDict()


def add_dict(in_list):
    for val in in_list:
        if val in test_dict.keys():
            test_dict[val].append(val)
        else:
            test_dict[val] = [val]


def add_ordereddict(in_list):
    for val in in_list:
        if val in test_ordereddict.keys():
            test_ordereddict[val].append(val)
        else:
            test_ordereddict[val] = [val]


def get_dict(val):
    out = test_dict[val]


def get_ordereddict(val):
    out = test_ordereddict[val]

print("Значения до 100")
idx = list_upto_hund1[50]
print("\t\t\t\tdict")
print("timeit функции add_dict: "
    f"{timeit(f'add_dict({list_upto_hund1})', setup='from __main__ import add_dict', number=100000)}")
print("timeit функции get_dict: "
    f"{timeit(f'get_dict({idx})', setup='from __main__ import get_dict', number=100000)}")
print("\t\t\t\tOrderedDict")
print("timeit функции add_ordereddict: "
    f"{timeit(f'add_ordereddict({list_upto_hund1})', setup='from __main__ import add_ordereddict', number=100000)}")
print("timeit функции get_ordereddict: "
    f"{timeit(f'get_ordereddict({idx})', setup='from __main__ import get_ordereddict', number=100000)}")
print("Большее число элементов>")
idx = list_upto_hund2[50]
print("\t\t\t\tdict")
print("timeit функции add_dict: "
    f"{timeit(f'add_dict({list_upto_hund2})', setup='from __main__ import add_dict', number=100000)}")
print("timeit функции get_dict: "
    f"{timeit(f'get_dict({idx})', setup='from __main__ import get_dict', number=100000)}")
print("\t\t\t\tOrderedDict")
print("timeit функции add_ordereddict: "
    f"{timeit(f'add_ordereddict({list_upto_hund2})', setup='from __main__ import add_ordereddict', number=100000)}")
print("timeit функции get_ordereddict: "
    f"{timeit(f'get_ordereddict({idx})', setup='from __main__ import get_ordereddict', number=100000)}")

print("Значения до 1000")
idx = list_upto_th1[50]
print("\t\t\t\tdict")
print("timeit функции add_dict: "
    f"{timeit(f'add_dict({list_upto_th1})', setup='from __main__ import add_dict', number=100000)}")
print("timeit функции get_dict: "
    f"{timeit(f'get_dict({idx})', setup='from __main__ import get_dict', number=100000)}")
print("\t\t\t\tOrderedDict")
print("timeit функции add_ordereddict: "
    f"{timeit(f'add_ordereddict({list_upto_th1})', setup='from __main__ import add_ordereddict', number=100000)}")
print("timeit функции get_ordereddict: "
    f"{timeit(f'get_ordereddict({idx})', setup='from __main__ import get_ordereddict', number=100000)}")
print("Большее число элементов>")
idx = list_upto_th2[50]
print("\t\t\t\tdict")
print("timeit функции add_dict: "
    f"{timeit(f'add_dict({list_upto_th2})', setup='from __main__ import add_dict', number=100000)}")
print("timeit функции get_dict: "
    f"{timeit(f'get_dict({idx})', setup='from __main__ import get_dict', number=100000)}")
print("\t\t\t\tOrderedDict")
print("timeit функции add_ordereddict: "
    f"{timeit(f'add_ordereddict({list_upto_th2})', setup='from __main__ import add_ordereddict', number=100000)}")
print("timeit функции get_ordereddict: "
    f"{timeit(f'get_ordereddict({idx})', setup='from __main__ import get_ordereddict', number=100000)}")

# Значения до 100
# 				dict
# timeit функции add_dict: 3.3517733
# timeit функции get_dict: 0.016108800000000034
# 				OrderedDict
# timeit функции add_ordereddict: 3.0436639
# timeit функции get_ordereddict: 0.018677699999999575
# Большее число элементов>
# 				dict
# timeit функции add_dict: 3.3483327999999997
# timeit функции get_dict: 0.023806500000000952
# 				OrderedDict
# timeit функции add_ordereddict: 3.3020656000000006
# timeit функции get_ordereddict: 0.01735869999999906
# Значения до 1000
# 				dict
# timeit функции add_dict: 31.793442
# timeit функции get_dict: 0.024642700000001128
# 				OrderedDict
# timeit функции add_ordereddict: 32.16741389999999
# timeit функции get_ordereddict: 0.014508899999995606
# Большее число элементов>
# 				dict
# timeit функции add_dict: 32.35347420000001
# timeit функции get_dict: 0.019818799999995917
# 				OrderedDict
# timeit функции add_ordereddict: 32.73662320000001
# timeit функции get_ordereddict: 0.016712100000006558


# Вывод: по результатам работы можно сделать вывод, что OrderedDict лучше получает большие данные чем обычный словарь,
# но при этом уступает в добавлении большой информации. При маленьких объемах данных работает лучше словаря.
