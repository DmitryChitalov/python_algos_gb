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


def find_time(func):
    import time

    def wrapper_func():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))

    return wrapper_func


@find_time
def create_list():
    some_list = []
    for i in range(n):
        some_list.append(i)
    return some_list


@find_time
def create_dict():
    some_dict = {}
    for i in range(n):
        some_dict[i] = i
    return some_dict


@find_time
def create_list_gen():
    some_list = [i for i in range(n)]
    return some_list


@find_time
def create_dict_gen():
    some_dict = {i: i for i in range(n)}
    return some_dict


@find_time
def get_even_from_list():
    return [el for el in [i for i in range(n)] if el % 2 == 0]


@find_time
def get_even_from_dict():
    return [el for el in {i: i for i in range(n)} if el % 2 == 0]


@find_time
def list_index():
    some_list = []
    for i in range(n):
        some_list.append(i)
    return some_list.index(n / 2)


@find_time
def dict_index():
    some_dict = {}
    for i in range(n):
        some_dict[i] = i
    return some_dict[n / 2]


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
[*] Время выполнения: 0.0690157413482666 секунд.
[*] Время выполнения: 0.08201837539672852 секунд.
[*] Время выполнения: 0.04200935363769531 секунд.
[*] Время выполнения: 0.07802772521972656 секунд.
[*] Время выполнения: 0.09501910209655762 секунд.
[*] Время выполнения: 0.1380314826965332 секунд.
[*] Время выполнения: 0.07600951194763184 секунд.
[*] Время выполнения: 0.07502627372741699 секунд.

Выводы: 
Заполнение словаря  происходит медленнее, чем списка, это применимо и к генераторам словарей или списков.
Перебор словаря, медленнее, чем перебор списка, но операции извлечения элементов происходит значительно быстрее в словарях.
"""
