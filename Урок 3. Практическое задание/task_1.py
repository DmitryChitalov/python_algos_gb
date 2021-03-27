"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
from functools import wraps
from time import perf_counter
import sys


def timer(fun):
    @wraps(fun)
    def wrapper_timer(*args):
        t0 = perf_counter()
        ret = fun(*args)
        dt = perf_counter() - t0
        a0 = args[0]
        # Чтобы, если аргументом является массив,
        # печаталась бы только его длина
        try:
            desc = f"(<{len(a0)}>,...)"
        except TypeError:
            desc = f"({a0},...)"
        print(f"{fun.__name__}{desc}: {dt:.4f} s")
        return ret
    return wrapper_timer


# Проверим скорость заполнения списка и словаря
# с помощью for и list comprehension
@timer
def fill_list(n):
    ret = []
    for i in range(n):
        ret.append(i)


@timer
def fill_list_comp(n):
    [i for i in range(n)]


if sys.argv[1] == "1":
    for k in (4, 5, 6, 7):
        fill_list(10**k)
    for k in (4, 5, 6, 7):
        fill_list_comp(10**k)

# Результаты:
# fill_list(10000,...): 0.0008 s
# fill_list(100000,...): 0.0075 s
# fill_list(1000000,...): 0.0737 s
# fill_list(10000000,...): 0.7417 s
#
# fill_list_comp(10000,...): 0.0004 s
# fill_list_comp(100000,...): 0.0044 s
# fill_list_comp(1000000,...): 0.0478 s
# fill_list_comp(10000000,...): 0.4943 s
#
# Видно, что list comprehension дает почти двукратное ускорение
# для списков. Это можно объяснить возможностью заранее выделить
# пямять для итогового списка и избежать перераспределения памяти.


@timer
def fill_dict(n):
    ret = {}
    for i in range(n):
        ret[i] = True


@timer
def fill_dict_comp(n):
    {i: True for i in range(n)}


if sys.argv[1] == "2":
    for k in (4, 5, 6, 7):
        fill_dict(10**k)
    for k in (4, 5, 6, 7):
        fill_dict_comp(10**k)

# Результаты:
# fill_dict(10000,...): 0.0006 s
# fill_dict(100000,...): 0.0083 s
# fill_dict(1000000,...): 0.1145 s
# fill_dict(10000000,...): 1.0419 s
#
# fill_dict_comp(10000,...): 0.0006 s
# fill_dict_comp(100000,...): 0.0081 s
# fill_dict_comp(1000000,...): 0.0985 s
# fill_dict_comp(10000000,...): 0.9942 s

# То, что list comprehension не приводит к ускорению
# заполнения словаря говорит о том, что перераспределение
# памяти происходит в любом случае, т.к. размер
# хеш-таблицы словаря изменяется из-за коллизий,
# которые невозможно предугадать заранее.

# Время заполнения словаря с ключами в виде целых чисел
# отличается от времени заполнения равного по размеру списка
# всего на четверть. Поскольку для целого n справедливо
# условие hash(n)==n, при заполнении последовательностью
# range() dict и list становятся алгоритмически эквивалентны.
#
# Проверим, как изменится время заполнения для строчных ключей:


@timer
def fill_list_str(n):
    ret = []
    for i in range(n):
        ret.append(str(i))


@timer
def fill_dict_str(n):
    ret = {}
    for i in range(n):
        ret[str(i)] = True


if sys.argv[1] == "3":
    for k in (4, 5, 6, 7):
        fill_list_str(10**k)
    for k in (4, 5, 6, 7):
        fill_dict_str(10**k)

# fill_list(10000,...): 0.0023 s
# fill_list(100000,...): 0.0270 s
# fill_list(1000000,...): 0.3104 s
# fill_list(10000000,...): 2.6481 s
#
# fill_dict(10000,...): 0.0027 s
# fill_dict(100000,...): 0.0339 s
# fill_dict(1000000,...): 0.4624 s
# fill_dict(10000000,...): 5.8220 s

# Теперь разница составляет уже два раза.
# Предположительно это связано с большей вероятностью
# коллизий и, соответственно, большим необходимым
# объемом памяти:
#
# >>> n=10000000
# >>> len(set(hash(i) % n for i in range(n)))
# 10000000
# >>> len(set(hash(str(i)) % n for i in range(n)))
# 6319569


@timer
def remove_first(lst):
    lst.pop(0)


@timer
def insert_first(lst):
    lst.insert(0, 0)


if sys.argv[1] == "4":
    for k in (4, 5, 6, 7):
        lst = list(range(10**k))
        remove_first(lst)
    for k in (4, 5, 6, 7):
        lst = list(range(10**k))
        insert_first(lst)

# remove_first(<9999>,...): 0.0000 s
# remove_first(<99999>,...): 0.0001 s
# remove_first(<999999>,...): 0.0012 s
# remove_first(<9999999>,...): 0.0123 s
# insert_first(<10001>,...): 0.0000 s
# insert_first(<100001>,...): 0.0001 s
# insert_first(<1000001>,...): 0.0053 s
# insert_first(<10000001>,...): 0.0130 s
#
# Время удаления и добавления элемента в начало списка
# пропорционально его длине из-за того, что такое
# удаление вызывает перемещение блока памяти.


@timer
def list_append(lst):
    lst.append(0)


@timer
def list_pop(lst):
    lst.pop()


@timer
def dict_insert(d):
    d[0] = 0


@timer
def dict_del(d):
    del d[0]


if sys.argv[1] == "5":
    n = 10000000
    lst = list(range(n))
    d = {i: True for i in range(n)}
    list_append(lst)
    list_pop(lst)
    dict_insert(d)
    dict_del(d)

# list.append(), list.pop(), dict[] и dict[]= по очевидной
# причине дают близкое к нулю время
#
# list_append(<10000001>,...): 0.0003 s
# list_pop(<10000000>,...): 0.0000 s
# dict_insert(<10000000>,...): 0.0000 s
# dict_del(<9999999>,...): 0.0000 s
