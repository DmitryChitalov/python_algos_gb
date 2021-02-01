"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit


def create_dict():
    result = dict()
    for i in range(100000):
        result[str(i)] = i
    return result


def create_ordered_dict():
    result = OrderedDict()
    for i in range(100000):
        result[str(i)] = i
    return result


def for_keys_values(dct):
    for key, value in dct.items():
        a = key
        b = value


def sort_items(dct):
    return sorted(dct.items())


def popitem(dct):
    for i in range(1000):
        a = dct.popitem()


def get_key(dct):
    for i in range(1000):
        dct.get(str(i))


def update_dict(dct, dct_2):
    dct.update(dct_2)


origin_dict = create_dict()
ordered_dict = create_ordered_dict()

print('  dict: ', timeit("create_dict()", globals=globals(), number=100))
print('o_dict: ', timeit("create_ordered_dict()", globals=globals(),
                         number=100))
print('-' * 100)
print('  dict: ',
      timeit("for_keys_values(origin_dict)", globals=globals(), number=100))
print('o_dict: ', timeit("for_keys_values(ordered_dict)", globals=globals(),
                         number=100))
print('-' * 100)
print('  dict: ',
      timeit("sort_items(origin_dict)", globals=globals(), number=100))
print('o_dict: ', timeit("sort_items(ordered_dict)", globals=globals(),
                         number=100))
print('-' * 100)
print('  dict: ', timeit("popitem(origin_dict)", globals=globals(), number=100))
print('o_dict: ', timeit("popitem(ordered_dict)", globals=globals(),
                         number=100))
print('-' * 100)
print('  dict: ', timeit("get_key(origin_dict)", globals=globals(), number=100))
print('o_dict: ', timeit("get_key(ordered_dict)", globals=globals(),
                         number=100))
print('-' * 100)
print('  dict: ', timeit("update_dict(origin_dict, {str(1000-i): i for i in "
                         "range(1000)})", globals=globals(),
                         number=100))
print('o_dict: ', timeit("update_dict(ordered_dict, {str(1000-i): i for i in "
                         "range(1000)})", globals=globals(),
                         number=100))
"""
По всем замерам OrderedDict работает так же или чуть дольше

  dict:  5.2275438
o_dict:  5.990125000000001
----------------------------------------------------------------------------------------------------
  dict:  0.6738821999999995
o_dict:  1.4320080999999991
----------------------------------------------------------------------------------------------------
  dict:  1.3318435000000015
o_dict:  2.3124968
----------------------------------------------------------------------------------------------------
  dict:  0.019395299999999338
o_dict:  0.034350400000001
----------------------------------------------------------------------------------------------------
  dict:  0.0488346999999969
o_dict:  0.04566649999999939
----------------------------------------------------------------------------------------------------
  dict:  0.05173819999999907
o_dict:  0.06469639999999899

Для версий python старше 3.7 смысла в его использовании нет
"""
