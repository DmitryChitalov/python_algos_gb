"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""

from collections import deque
from timeit import timeit
from random import randint


def test_append_list_obj(list_obj, elems_list):
    for num in range(len(elems_list)):
        list_obj.append(elems_list[num])
    return list_obj


def test_insert_list_obj(list_obj, elems_list):
    for num in range(len(elems_list)):
        list_obj.insert(0, elems_list[num])
    return list_obj


def test_append_deque_obj(deque_obj, elems_list):
    for num in range(len(elems_list)):
        deque_obj.append(elems_list[num])
    return deque_obj


def test_appendleft_deque_obj(deque_obj, elems_list):
    for num in range(len(elems_list)):
        deque_obj.appendleft(elems_list[num])
    return deque_obj


def test_pop_with_idx_list_obj(list_obj, num_elems):
    if len(list_obj) > num_elems:
        for num in range(num_elems):
            list_obj.pop(0)
    return list_obj


def test_pop_list_obj(list_obj, num_elems):
    if len(list_obj) > num_elems:
        for num in range(num_elems):
            list_obj.pop()
    return list_obj


def test_popleft_deque_obj(deque_obj, num_elems):
    if len(deque_obj) > num_elems:
        for num in range(num_elems):
            deque_obj.popleft()
    return deque_obj


def test_pop_deque_obj(deque_obj, num_elems):
    if len(deque_obj) > num_elems:
        for num in range(num_elems):
            deque_obj.pop()
    return deque_obj


if __name__ == "__main__":
    test_list = [randint(0, 100) for num in range(10000)]
    test_deque = deque(test_list)
    elems_for_test = [randint(0, 100) for num in range(4)]
    num_elems = randint(100, 1000)

    print("Сравнение эффективности методов insert и appendleft  у list и deque:")
    print(timeit(
        "test_insert_list_obj(test_list, elems_for_test)",
        setup="from __main__ import test_insert_list_obj, test_list, elems_for_test", number=1000)
    )
    print(timeit(
        "test_appendleft_deque_obj(test_deque, elems_for_test)",
        setup="from __main__ import test_appendleft_deque_obj, test_deque, elems_for_test", number=1000)
    )

    print('Сравнение эффективности метода append у list и deque:')
    print(timeit(
        "test_append_list_obj(test_list, elems_for_test)",
        setup="from __main__ import test_append_list_obj, test_list, elems_for_test", number=1000)
    )
    print(timeit(
        "test_append_deque_obj(test_deque, elems_for_test)",
        setup="from __main__ import test_append_deque_obj, test_deque, elems_for_test", number=1000)
    )

    print("Сравнение методов pop и popleft у list и deque:")
    print(timeit(
        "test_pop_with_idx_list_obj(test_list, num_elems)",
        setup="from __main__ import test_pop_with_idx_list_obj, test_list, num_elems", number=1000)
    )
    print(timeit(
        "test_popleft_deque_obj(test_deque, num_elems)",
        setup="from __main__ import test_popleft_deque_obj, test_deque, num_elems", number=1000)
    )

    print("Сравнение метода pop у list и deque:")
    print(timeit(
        "test_pop_list_obj(test_list, num_elems)",
        setup="from __main__ import test_pop_list_obj, test_list, num_elems", number=1000)
    )
    print(timeit(
        "test_pop_deque_obj(test_deque, num_elems)",
        setup="from __main__ import test_pop_deque_obj, test_deque, num_elems", number=1000)
    )

"""
Сравнение эффективности методов у list и аппаратной очереди deque с помощью timeit показало, 
сто информация в документации полностью соотвествует действительности. Медоды pop и append практически не различаются по 
временным затратам. Методы deque, а именно appendleft и popleft на порядок, а то и 2-3 порядка, эффективнее методов list,
таких как insert и pop, с указанием индекса.
"""