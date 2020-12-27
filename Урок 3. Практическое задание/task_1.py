"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: если вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

from collections.abc import Sequence as sq
import random
import time


def clock(func):
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()

        result = func(*args, **kwargs)

        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_1st = []
        if args:
            arg_1st.append(
                ', '.join(repr(arg[:5] + ['...'] if isinstance(arg, sq) and not isinstance(arg, str) and len(arg) > 5
                               else (
                    {**{list(arg.keys())[i]: arg[list(arg.keys())[i]] for i in range(3)}, **{3: '...'}}
                    if isinstance(arg, dict) and len(arg.keys()) > 3 else arg)) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_1st.append(', '.join(pairs))
        arg_str = ', '.join(arg_1st)
        print('[%0.8fs] %s(%s)' % (elapsed, name, arg_str))
        return result

    return clocked


@clock
def filling(obj: str, quantity: int):
    if obj == 'list':
        return [random.randrange(-100, 100) for _ in range(quantity)]
    elif obj == 'dict':
        return {i: random.randrange(-100, 100) for i in range(quantity)}


@clock
def copy_obj(obj):
    return obj.copy()


@clock
def clear_obj(obj):
    return obj.clear()


@clock
def get_item(obj, n):
    return obj[n]


if __name__ == '__main__':
    print('Заполнение элементами:')
    # Заполнение списка будет выполняться быстрее, чем заполнение словаря
    list_obj = filling('list', 100000)
    dict_obj = filling('dict', 100000)

    print('\nКопирование объектов:')
    # Копирование списка будет выполняться значительно быстрее
    list_copy = copy_obj(list_obj)
    dict_copy = copy_obj(dict_obj)

    print('\nУдаление всех элементов:')
    # Удаление всех элементов списка так же будет выполняться быстрее
    clear_obj(list_copy)
    clear_obj(dict_copy)

    print('\nПолучение элемента:')
    # Получение элемента по ключу в словаре будет выполняться быстрее, чем по индексу в списке
    get_item(list_obj, 10000)
    get_item(dict_obj, 10000)

    # Все объяснения разных значений скорости выполнение операций с одинаковой сложностью для списка и для словаря
    # сводятся к наличию у словаря хеш-таблицы.
