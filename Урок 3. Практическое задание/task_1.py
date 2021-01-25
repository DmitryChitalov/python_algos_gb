"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""


def measure_time(func):
    import time

    def wrapper_func():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))

    return wrapper_func

@measure_time
def create_list():
    some_list = []
    for i in range(n):
        some_list.append(i)
    return some_list

@measure_time
def create_dict():
    some_dict = {}
    for i in range(n):
       some_dict[i] = i
    return some_dict

@measure_time
def create_list_gen():
    some_list = [i for i in range(n)]
    return some_list\

@measure_time
def create_dict_gen():
    some_dict = {i: i for i in range(n)}
    return some_dict

@measure_time
def get_even_from_list():
    return [el for el in [i for i in range(n)] if el % 2 == 0]

@measure_time
def get_even_from_dict():
    return [el for el in {i: i for i in range(n)} if el % 2 == 0]

@measure_time
def list_index():
    some_list = []
    for i in range(n):
        some_list.append(i)
    return some_list.index(n/2)


@measure_time
def dict_index():
    some_dict = {}
    for i in range(n):
       some_dict[i] = i
    return some_dict[n/2]


n = 1000000

create_list()
create_dict()
create_list_gen()
create_dict_gen()
get_even_from_list()
get_even_from_dict()
list_index()
dict_index()

"""
[*] Время выполнения: 0.11591863632202148 секунд.
[*] Время выполнения: 0.11593317985534668 секунд.
[*] Время выполнения: 0.0709695816040039 секунд.
[*] Время выполнения: 0.1079413890838623 секунд.
[*] Время выполнения: 0.19590234756469727 секунд.
[*] Время выполнения: 0.24485397338867188 секунд.
[*] Время выполнения: 0.16891217231750488 секунд.
[*] Время выполнения: 0.1149289608001709 секунд.


Выводы: 
Заполнение словаря  происходит медленнее, чем списка,
причем это применимо и к генераторам словарей или списков
 требуются дополнительные расходы на хранение хэшей, 
 перебор словаря, так же медленнее, чем перебор списка,
 но операции извлечения элементов происходит значительно быстрее в словарях
"""
