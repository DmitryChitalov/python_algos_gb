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


def get_some(obj, counter):
    if type(obj) == list:
        return [obj.pop(0) for i in range(counter)]
    elif type(obj) == deque:
        return [obj.popleft() for i in range(counter)]
    else:
        return "ошибочка"


def add_some(obj, applet):
    if type(obj) == list:
        [obj.insert(0, i) for i in applet]
        return obj
    elif type(obj) == deque:
        applet.reverse()
        [obj.appendleft(i) for i in applet]
        return obj
    else:
        return "ошибочка"


def get_random(obj, counter):
    return [obj[randint(0, len(obj)-1)] for i in range(counter)]


def ins_random(obj, counter):
    for i in range(counter):
        obj.insert((randint(0, len(obj)-1)), randint(0, 1000))
    return obj


if __name__ == '__main__':
    my_deque = deque(chr(i) for i in range(ord('A'), 1010))
    my_list = [chr(i) for i in range(ord('A'), 1010)]
    # print(my_deque)
    # print(my_list)
    # print(get_some(my_deque, 10))
    # print(get_some(my_list, 10))
    new_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(add_some(my_deque, new_list))
    # print(add_some(my_list, new_list))
    print(timeit(
        'get_some(my_deque, 5)',
        setup='from __main__ import get_some,my_deque',
        number=100))
    print(timeit(
        'get_some(my_list, 5)',
        setup='from __main__ import get_some,my_list',
        number=100))

    print(timeit(
        'add_some(my_deque, new_list)',
        setup='from __main__ import add_some,my_deque,new_list',
        number=100))
    print(timeit(
        'add_some(my_list, new_list)',
        setup='from __main__ import add_some,my_list,new_list',
        number=100))
    """
    Наверное с алфавитом пример не очень удачный, но дек пока побыстрее на выборке раза в полтора
    0.00010330000000000061
    0.00015239999999999698
    На левой вставке дек быстрее списка в 4-5 раз даже не смотря на реверс добавляемого списка чтобы получить 
    одинаковые результаты
    0.00011999999999999511
    0.0005001000000000033
    """
    # print(get_random(my_deque, 10))
    # print(get_random(my_list, 10))
    print(timeit(
        'get_random(my_deque, 1000)',
        setup='from __main__ import get_random,my_deque',
        number=1000))
    print(timeit(
        'get_random(my_list, 1000)',
        setup='from __main__ import get_random,my_list',
        number=1000))
    """
    на операции случайного доступа список немного быстрее дека
    1.0747448
    0.9458411999999998
    """
    # print(ins_random(my_deque, 10))
    # print(ins_random(my_list, 10))
    print(timeit(
        'ins_random(my_deque, 1000)',
        setup='from __main__ import ins_random,my_deque',
        number=100))
    print(timeit(
        'ins_random(my_list, 1000)',
        setup='from __main__ import ins_random,my_list',
        number=100))
    """
    На случайной вставке список опять же быстрее 
    2.2873984000000003
    1.4207976999999996
    информация в документации соответствует дейстивтельности
    """
