"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""
"""
a) Список заполняется быстрее. 
   Не заполняется хеши ключей + способ заполнения с использованием list comprehensions оптимальнее
b) Перебор словаря - медленнее. Вытаскиваются элементы по ключу быстрее.  
   Просто один элемент вытаскивался слишком быстро. Поэтому пришлось обернуть в цикл и сделать замер уже его. 
"""
import time


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func_result = func(*args, **kwargs)
        end_time = time.time()
        return func_result, end_time - start_time

    return wrapper


@time_decorator
def list_populate(num: int):
    """Заполнение списка"""
    test_list = [round(x * 1.03 - 2017, 2) for x in range(num)]
    return test_list


@time_decorator
def dict_populate(num: int):
    """Заполнение словаря"""
    test_dict = {}
    for dig in range(num):
        test_dict.setdefault(dig, round(dig * 1.03 - 2017, 2))
    return test_dict


@time_decorator
def get_list_els(i_list):
    """Вытаскиваем каждый 7ой элемент списка в список."""
    return [i_list[i] for i in range(len(i_list)) if i % 7 == 0]


@time_decorator
def get_dict_els(i_dict):
    ''"""Вытаскиваем каждый 7ой элемент словаря в список"""
    return [i_dict[i] for i in range(len(i_dict)) if i % 7 == 0]


@time_decorator
def list_sum(i_list, start_el, end_el):
    """Подсчет суммы опр среза элементов списка. Специально не используются встроенные функции"""
    res = 0
    for el in i_list[start_el:end_el]:
        res += el
    # print(res)
    return res


@time_decorator
def dict_sum(i_dict, start_el, end_el):
    """Подсчет суммы опр среза элементов словаря. Специально не используются встроенные функции"""
    res = 0
    for el in range(start_el, end_el):
        res += i_dict[el]
    # print(res)
    return res


def get_list_value(i_list, el):
    return i_list[el]


def get_dict_value(i_dict, el):
    return i_dict[el]


@time_decorator
def get_list_value_cycle(i_list, max_el):
    i = 0
    while i < max_el:
        if i % 22 == 0:
            get_list_value(i_list, i)
        i += 1


# исключила функцию len поэтому ввела второй параметр.
@time_decorator
def get_dict_value_cycle(i_dict, max_el):
    i = 0
    while i < max_el:
        if i % 22 == 0:
            get_list_value(i_dict, i)
        i += 1


test_list1, test_time = list_populate(30000)
print("list_populate(30000)", test_time)
test_dict1, test_time = dict_populate(30000)
print("dict_populate(30000)", test_time)
print("Формируем спискок из каждого 7ого элемента ")
print("get_list_els", get_list_els(test_list1)[1])
print("get_dict_els", get_dict_els(test_dict1)[1])
print("list_sum [1024:8856]", list_sum(test_list1, 1024, 8856)[1])
print("dict_sum [1024:8856]", dict_sum(test_dict1, 1024, 8856)[1])
print("get_list_value_cycle(test_list1, 20000)", get_list_value_cycle(test_list1, 20000))
print("get_dict_value_cycle(test_dict1, 20000)", get_dict_value_cycle(test_dict1, 20000))





test_list2, test_time = list_populate(300000)
print("list_populate(30000)", test_time)
test_dict2, test_time = dict_populate(300000)
print("dict_populate(30000)", test_time)
print("Формируем спискок из каждого 7ого элемента ")
print("get_list_els", get_list_els(test_list2)[1])
print("get_dict_els", get_dict_els(test_dict2)[1])
print("list_sum [1024:18856]", list_sum(test_list2, 1024, 18856)[1])
print("dict_sum [1024:18856]", dict_sum(test_dict2, 1024, 18856)[1])
print("get_list_value_cycle(test_list2, 200000)", get_list_value_cycle(test_list2, 200000))
print("get_dict_value_cycle(test_dict2, 200000)", get_dict_value_cycle(test_dict2, 200000))
