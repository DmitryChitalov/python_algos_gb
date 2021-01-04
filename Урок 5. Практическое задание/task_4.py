"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

Ответ: все операции в OrderedDict медленнее, чем в обычном словаре, только сортировки
иногда показывают лушие результаты (но довольно редко). Самый неожиданный результат показал
встроенный метод move_to_end, который значительно уступает по скорости сочетанию подобных
действий в словаре.
Свое отставание по скорости OrderedDict по сравнению со словарем уже ничем не
оправдывает и необходимости в нем никакой нет.
"""

from timeit import timeit
from collections import OrderedDict


def update_obj(obj):
    for i in range(10001, 20000):
        obj.update({i: 1})


def get_el(obj):
    for i in range(1000000):
        el = obj[i]


def pop_el(obj):
    for i in range(1000000):
        obj.pop(i)


def copy_obj(obj):
    return obj.copy()


def move_obj(obj):
    if isinstance(obj, dict):
        for i in range(1000000):
            obj.update({i: obj.pop(i)})
    if isinstance(obj, OrderedDict):
        for i in range(1000000):
            obj.move_to_end(i)


def sorted_obj1(obj):
    return {i: obj[i] for i in sorted(obj)}


def sorted_obj2(obj):
    return {i: j for i, j in sorted(obj.items(), key=lambda x: x[1])}


if __name__ == '__main__':
    a = {j: i for i, j in enumerate(range(1000000))}
    b = OrderedDict(a)
    print('Обновление:')
    print(timeit('update_obj(a1)', setup='a1 = a.copy()', number=100, globals=globals()))
    print(timeit('update_obj(b1)', setup='b1 = b.copy()', number=100, globals=globals()))
    print('\nПолучение элемента по ключу:')
    print(timeit('get_el(a)', number=1, globals=globals()))
    print(timeit('get_el(b)', number=1, globals=globals()))
    print('\nУдаление элементов по ключу:')
    print(timeit('pop_el(a1)', setup='a1 = a.copy()', number=1, globals=globals()))
    print(timeit('pop_el(b1)', setup='b1 = b.copy()', number=1, globals=globals()))
    print('\nКопирование:')
    print(timeit('copy_obj(a)', number=10, globals=globals()))
    print(timeit('copy_obj(b)', number=10, globals=globals()))
    print('\nПеремещение элемента из левой части в правую:')
    print(timeit('move_obj(a)', number=1, globals=globals()))
    print(timeit('move_obj(b)', number=1, globals=globals()))
    print('\nСортировка по ключам:')
    print(timeit('sorted_obj1(a)', number=1, globals=globals()))
    print(timeit('sorted_obj1(b)', number=1, globals=globals()))
    print('\nСортировка по значениям:')
    print(timeit('sorted_obj1(a)', number=1, globals=globals()))
    print(timeit('sorted_obj1(b)', number=1, globals=globals()))
