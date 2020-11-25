"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from timeit import timeit
from collections import OrderedDict


def update_dict(el_count):
    new_dict = dict()
    for i in range(el_count):
        new_dict.update({str(i): i})
    return new_dict


def update_ord_dict(el_count):
    new_dict = OrderedDict()
    for i in range(el_count):
        new_dict.update({str(i): i})
    return new_dict


def pop_item_dict(a_dict):
    for i in range(len(a_dict)):
        return a_dict.popitem()


#####
def bench_update_dict(el_count):
    action = f"update_dict({el_count})"
    setup = "from __main__ import update_dict"
    number = 10000
    return timeit(action, setup, number=number, globals=globals())


def bench_update_ord_dict(el_count):
    action = f"update_ord_dict({el_count})"
    setup = "from __main__ import update_ord_dict"
    number = 10000
    return timeit(action, setup, number=number, globals=globals())


def bench_popitem_dict(el_count):
    action = f"pop_item_dict({el_count})"
    setup = 'from __main__ import pop_item_dict'
    number = 10000
    return timeit(action, setup, number=number, globals=globals())


def determinate_fastest(time_dict, time_ord_dict, operation, el_count):
    if time_dict < time_ord_dict:
        print(
            f"При {operation} на {el_count} dict работает быстрее чем ord_dict. \
\ttime_dict: {time_dict} < time_ord_dict: {time_ord_dict}")
    else:
        print(
            f"При {operation} на {el_count} ord_dict работает быстрее чем dict. \
\ttime_ord_dict: {time_ord_dict} < time_dict: {time_dict}")


def main():
    pass
    try:

        update_dict_100 = bench_update_dict(100)
        update_ord_dict_100 = bench_update_ord_dict(100)
        determinate_fastest(update_dict_100, update_ord_dict_100, "update", 100)

        update_dict_1000 = bench_update_dict(1000)
        update_ord_dict_1000 = bench_update_ord_dict(1000)
        determinate_fastest(update_dict_1000, update_ord_dict_1000, "update", 1000)

        update_dict_3000 = bench_update_dict(3000)
        update_ord_dict_3000 = bench_update_ord_dict(3000)
        determinate_fastest(update_dict_3000, update_ord_dict_3000, "update", 100)

        dict_100 = update_dict(100)
        dict_1000 = update_dict(1000)
        dict_3000 = update_dict(3000)
        ord_dict_100 = update_ord_dict(100)
        ord_dict_1000 = update_ord_dict(1000)
        ord_dict_3000 = update_ord_dict(3000)

        time_pop_dict_100 = bench_popitem_dict(dict_100)
        time_pop_ord_dict_100 = bench_popitem_dict(ord_dict_100)
        determinate_fastest(time_pop_dict_100, time_pop_ord_dict_100, "pop item", 100)

        time_pop_dict_1000 = bench_popitem_dict(dict_1000)
        time_pop_ord_dict_1000 = bench_popitem_dict(ord_dict_1000)
        determinate_fastest(time_pop_dict_1000, time_pop_ord_dict_1000, "pop item", 1000)

        time_pop_dict_3000 = bench_popitem_dict(dict_3000)
        time_pop_ord_dict_3000 = bench_popitem_dict(ord_dict_3000)
        determinate_fastest(time_pop_dict_3000, time_pop_ord_dict_3000, "pop item", 3000)

        print("\nПрограмма завершена!")
    except Exception as ex:
        print(f"Fatal error: {ex}")


if __name__ == "__main__":
    main()

"""

Вывод:
В текущей версии python dict работает быстрее order_dict.

При update на 100 dict работает быстрее чем ord_dict. 	time_dict: 0.3230724309996731 < time_ord_dict: 0.40379724699960207
При update на 1000 dict работает быстрее чем ord_dict. 	time_dict: 3.071336254000016 < time_ord_dict: 4.194941380999808
При update на 100 dict работает быстрее чем ord_dict. 	time_dict: 10.074433027999476 < time_ord_dict: 14.581640600000355
При pop item на 100 dict работает быстрее чем ord_dict. 	time_dict: 0.019362731999535754 < time_ord_dict: 0.12150593800015486
При pop item на 1000 dict работает быстрее чем ord_dict. 	time_dict: 0.20666829000037978 < time_ord_dict: 0.9765429160006533
При pop item на 3000 dict работает быстрее чем ord_dict. 	time_dict: 0.6310723599999619 < time_ord_dict: 3.323664978999659
"""