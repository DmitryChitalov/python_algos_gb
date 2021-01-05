"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
import time


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return res

    return wrapper


@benchmark
def init_list():
    lst = []
    for i in range(1000000):
        lst.append(i)
    return lst


@benchmark
def init_dict():
    dict = {}
    for i in range(1000000):
        dict[i] = i
    return dict


@benchmark
def add_to_list(lst):
    for i in range(len(lst), len(lst) + 1000000):
        lst.append(i)


@benchmark
def add_to_dict(dict):
    for i in range(1000000, 2000000):
        dict[i] = i


@benchmark
def get_from_list(lst):
    return lst[1000000]


@benchmark
def get_from_dict(dict):
    return dict.get(1000000)


list = init_list()
dict = init_dict()
add_to_list(list)
add_to_dict(dict)
list_el = get_from_list(list)
dict_el = get_from_dict(dict)

"""
init_list 0.09682416915893555
init_dict 0.1258707046508789
add_to_list 0.08980917930603027
add_to_dict 0.13010907173156738
get_from_list 6.9141387939453125e-06
get_from_dict 1.0967254638671875e-05

Выводы:
1. инициализация быстрее у списка, медленнее у словаря - для словаря требуются расчеты хешей для ключей
2. добавление элементов в список быстрее, медленнее у словаря - для словаря требуются расчеты хешей для ключей
3. выбора элемента по ключу быстрее в словаре, т.к. поиск по ключу(хешу) быстрее, чем в списке 
"""
