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


def bench(decor_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        __result = decor_func(*args, **kwargs)
        end = time.time()
        print(f'Время исполнения: {end - start}')
        return __result
    return wrapper


@bench
def fill_list(num):
    completed_list = []
    for i in range(num):
        completed_list.append(i)
    return completed_list


@bench
def fill_dict(num):
    completed_dict = {}
    for i in range(num):
        completed_dict[i] = i
    return completed_dict


@bench
def iterate_list_by_for_loop(_list):
    __elem = 0
    for key in _list:
        __elem = key


@bench
def iterate_dict_by_for_loop(_dict):
    __elem = 0
    for key in _dict:
        __elem = _dict[key]


@bench
def iterate_list_by_for_loop_with_range(_list, size):
    __elem = 0
    for i in range(size):
        __elem = _list[i]


@bench
def iterate_dict_by_for_loop_with_range(_dict, size):
    __elem = 0
    for i in range(size):
        __elem = _dict[i]

@bench
def forloop_dict(dict):
    __count = 0
    for key in dict:
      __count += 1
    return __count
@bench
def forloop_list(list):
    __count = 0
    for elem in list:
        __count += 1
    return __count


print('=====заполнение===')
print('Заполнение словаря')
filled_dict = fill_dict(50000000)
print('========================')
print('Заполнение списка')
filled_list = fill_list(50000000)
print('=====чтение контрукцией for in=======')
print('чтение из словаря')
iterate_dict_by_for_loop(filled_dict)
print('========================')
print('чтение из списка')
iterate_list_by_for_loop(filled_list)
print('==== чтение через range======')
print('чтение из словаря')
iterate_dict_by_for_loop_with_range(filled_dict, 50000000)
print('========================')
print('чтение из списка')
iterate_list_by_for_loop_with_range(filled_list, 50000000)
'''
Заполнение словаря
Время исполнения: 0.1775226593017578
Заполнение списка
Время исполнения: 0.17253923416137695
Заполнение списка происходит быстрее чем словаря, связано это с реализацией добавления нового ключа в словарь
при добавлении нового ключа вычисляется его хэш

Получение значения по ключу из словаря
Время исполнения: 0.0
Получение значения по ключу из списка
Время исполнения: 0.0

Доступ к элементам словаря и списка происходят одинаково по времени

=====заполнение===
Заполнение словаря
Время исполнения: 6.419315576553345
========================
Заполнение списка
Время исполнения: 5.259367227554321


=====чтение контрукцией for in=======
чтение из словаря
Время исполнения: 3.0200047492980957
========================
чтение из списка
Время исполнения: 1.188683271408081


==== чтение через range======
чтение из словаря
Время исполнения: 4.2646050453186035
========================
чтение из списка
Время исполнения: 3.136624336242676
'''