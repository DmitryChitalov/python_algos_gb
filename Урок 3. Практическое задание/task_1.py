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


def runtime(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f'Время выполнения: {end - start} секунд.')
        return result
    return wrapper


@runtime
def add_list(in_list):
    in_list = [i for i in range(1000000)]
    return in_list


@runtime
def add_dict(in_list):
    in_dict = {i: i for i in range(1000000)}
    return in_dict


@runtime
def del_list(in_list):
    while len(in_list) > 0:
        in_list.pop()


@runtime
def del_dist(in_dict):
    while len(in_dict) > 0:
        in_dict.popitem()


@runtime
def get_element_list(in_list, el):
    return in_list[el]


@runtime
def get_element_dict(in_dict, el):
    return in_dict.get(el)


my_list = add_list(None)
# Время выполнения: 0.04586505889892578 секунд.

my_dict = add_dict(None)
# Время выполнения: 0.08676743507385254 секунд.

print(get_element_list(my_list, 999))
# Время выполнения: 0.0 секунд.

print(get_element_dict(my_dict, 999))
# Время выполнения: 0.0 секунд.

del_list(my_list)
# Время выполнения: 0.15823769569396973 секунд.

del_dist(my_dict)
# Время выполнения: 0.1824629306793213 секунд.

"""
В список и словарь добавил 1 млн. записей.
Заполнение и удаление элементов списка, проходит быстрее чем словаря.
Получение одного значения из списка и словаря в моем случае занимает одинаковое время,
при этом результат довольно странный = 0.0 секунд.
"""
