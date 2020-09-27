"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import repeat

my_dict = {str(i): i for i in range(100)}
my_order_dict = OrderedDict([(str(i), i) for i in range(100)])


def update_dict():
    copy_dict = my_dict.copy()
    for i, j in copy_dict.items():
        copy_dict[i] = j**2
    return copy_dict


def update_order_dict():
    copy_dict = my_order_dict.copy()
    for i, j in copy_dict.items():
        copy_dict[i] = j**2
    return copy_dict


print(update_dict())
print(update_order_dict())

print("get")
print(repeat("my_dict.get('1')", setup='from __main__ import my_dict', number=10000, repeat=5))
"""[0.0006315999999999995, 0.0006248999999999977, 0.0006238000000000007, 0.0006227000000000003, 0.0006849000000000022]"""

print(repeat("my_order_dict.get('1')", setup='from __main__ import my_order_dict', number=10000, repeat=5))
"""[0.0006303000000000038, 0.0006282000000000024, 0.0008408999999999986, 0.0006306999999999979, 0.0006287999999999988]"""

print("items")
print(repeat("my_dict.items()", setup='from __main__ import my_dict', number=10000, repeat=5))
"""[0.0009653999999999982, 0.0012143000000000015, 0.0015131999999999993, 0.0015037999999999996, 0.0013030000000000055]"""

print(repeat("my_order_dict.items()", setup='from __main__ import my_order_dict', number=10000, repeat=5))
"""[0.0007039999999999963, 0.0006909000000000012, 0.0011952000000000004, 0.0011907999999999988, 0.0013977000000000017]"""

print("values")
print(repeat("my_dict.values()", setup='from __main__ import my_dict', number=10000, repeat=5))
"""[0.0007114000000000009, 0.0007170999999999983, 0.000675000000000002, 0.0006943999999999978, 0.000701299999999995]"""

print(repeat("my_order_dict.values()", setup='from __main__ import my_order_dict', number=10000, repeat=5))
"""[0.0006569000000000019, 0.000697199999999995, 0.0006985999999999937, 0.0006786000000000014, 0.0006832999999999978]"""

print("keys")
print(repeat("my_dict.keys()", setup='from __main__ import my_dict', number=10000, repeat=5))
"""[0.0007390000000000035, 0.0006597999999999951, 0.0006578, 0.0006948999999999983, 0.0007269999999999985]"""

print(repeat("my_order_dict.keys()", setup='from __main__ import my_order_dict', number=10000, repeat=5))
"""[0.0006584999999999994, 0.0006593000000000016, 0.000801099999999999, 0.0009207999999999994, 0.0006564000000000014]"""

print("update")
print(repeat("update_dict()", setup='from __main__ import update_dict', number=10000, repeat=5))
"""[0.26224800000000004, 0.27520010000000006, 0.2762133, 0.26907859999999995, 0.2987994999999999]"""

print(repeat("update_order_dict()", setup='from __main__ import update_order_dict', number=10000, repeat=5))
"""[0.4131841999999999, 0.4339313, 0.4135192000000001, 0.3926227999999998, 0.38545430000000014]"""


"""
OrderedDict не впечатлил.
При выполнении стандартных функций get, items, values, keys примерно одинаковые с обычным словарем.
При выполнении обновления значений по ключу OrderedDict проиграл по времени обычному словарю.
OrderedDict вычеркнул из своего списка колекций для постоянного использования)
"""
