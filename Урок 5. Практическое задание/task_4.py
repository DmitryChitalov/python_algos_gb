"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
import timeit

dict_example = {x: str(x) for x in range(10)}
ordered_dict_example = OrderedDict([(0,'0'), (1,'1'), (2,'2'), (3,'3'), (4,'4'), (5,'5'),
                                    (6,'6'), (7,'7'), (8,'8'), (9,'9')])


help(ordered_dict_example)

print("Время ordered_dict_example.items()",
      timeit.timeit("ordered_dict_example.items()", "from __main__ import ordered_dict_example", number=100))
print("Время dict_example.items()",
      timeit.timeit("dict_example.items()", "from __main__ import dict_example", number=100))

print("Время ordered_dict_example.values()",
      timeit.timeit("ordered_dict_example.values()", "from __main__ import ordered_dict_example", number=100))
print("Время dict_example.values()",
      timeit.timeit("dict_example.values()", "from __main__ import dict_example", number=100))

print("Время ordered_dict_example.keys()",
      timeit.timeit("ordered_dict_example.keys()", "from __main__ import ordered_dict_example", number=100))
print("Время dict_example.keys()",
      timeit.timeit("dict_example.keys()", "from __main__ import dict_example", number=100))

print("Время ordered_dict_example.update()",
      timeit.timeit("ordered_dict_example.update(a=1)", "from __main__ import ordered_dict_example", number=100))
print("Время dict_example.update()",
      timeit.timeit("dict_example.update(a=1)", "from __main__ import dict_example", number=100))

"""
В целом dict из стандартной библиотеки работает или быстрее или с тем же временем, что и OrderedDict
из модуля collections
"""
