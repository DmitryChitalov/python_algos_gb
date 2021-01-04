"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from random import randint
from timeit import timeit


def test_get_dict(dict_obj):
    for num in range(len(dict_obj)-1):
        dict_obj.get(num)


def test_get_ordered_dict(ordered_dict_obj):
    for num in range(len(ordered_dict_obj) - 1):
        ordered_dict_obj.get(num)


def test_popitem_dict(dict_obj, num_items):
    if len(dict_obj) > num_items:
        for num in range(num_items):
            dict_obj.popitem()


def test_popitem_ordered_dict(ordered_dict_obj, num_items):
    if len(ordered_dict_obj) > num_items:
        for num in range(num_items):
            ordered_dict_obj.popitem()


def test_keys_values_items_dict(dict_obj):
    keys = dict_obj.keys()
    values = dict_obj.values()
    items = dict_obj.items()


def test_keys_values_items_ordered_dict(ordered_dict_obj):
    keys = ordered_dict_obj.keys()
    values = ordered_dict_obj.values()
    items = ordered_dict_obj.items()


if __name__ == "__main__":
    test_dict = {}
    num_elems = randint(1000, 10000)
    for num in range(num_elems):
        test_dict[num] = num
    items_for_ordered_dict = test_dict.items()
    test_ordered_dict = OrderedDict(list(items_for_ordered_dict))
    num_items = randint(100, 1000)

    print("Сравнение эффективности метода get у dict и OrderedDict")
    print(timeit("test_get_dict(test_dict)", setup="from __main__ import test_get_dict, test_dict", number=1000))
    print(timeit(
        "test_get_ordered_dict(test_ordered_dict)",
        setup="from __main__ import test_get_ordered_dict, test_ordered_dict", number=1000
        )
    )

    print("Сравнение эффективности метода popitem у dict и OrderedDict")
    print(
        timeit(
            "test_popitem_dict(test_dict, num_items)",
            setup="from __main__ import test_popitem_dict, test_dict, num_items", number=1000
        )
    )
    print(timeit(
        "test_popitem_ordered_dict(test_ordered_dict, num_items)",
        setup="from __main__ import test_popitem_ordered_dict, test_ordered_dict, num_items", number=1000
        )
    )

    print("Сравнение эффективности методов keys, values и items у dict и OrderedDict")
    print(
        timeit(
            "test_keys_values_items_dict(test_dict)",
            setup="from __main__ import test_keys_values_items_dict, test_dict", number=1000
        )
    )
    print(timeit(
        "test_keys_values_items_ordered_dict(test_ordered_dict)",
        setup="from __main__ import test_keys_values_items_ordered_dict, test_ordered_dict", number=1000
    )
    )

"""
Сравнение методов dict и OrderedDict с помощью timeit показало, что значительных различий по эффективности нет.
А это значит, что от использования OrderedDict вполне можно отказаться в пользу обычного словаря.
"""


