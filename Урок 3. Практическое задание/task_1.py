import time
import random
"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""


def time_check(func):
    def it_func(*args):
        start_time = time.time()
        f = func(*args)
        end_time = time.time()
        res_time = end_time - start_time
        print("--- {:.4f} seconds ---".format(res_time))
        return f
    return it_func


@time_check
def fill_list(lst, n=30000):    # Сложность: O(N) - заполнения списка 30тыс элементами
    for i in range(1, n + 1):                   # O(N)
        lst.append(random.randint(1, n*2))      # O(1)
    print('Заполнение списка:')
    return lst


@time_check
def fill_dict(dct, n=30000):    # Сложность: O(N) - заполнения словаря 30тыс элементами
    for i in range(1, n + 1):               # O(N)
        dct[random.randint(1, n*2)] = 0     # O(1)
    print('Заполнение словаря:')
    return dct


@time_check
def operation_dict(dct):    # сложность: O(N) - линейная
    x = 0
    for key in dct:           # O(n)
        if key in dct:        # O(1)
            dct[key] += 1     # O(1)
    print('Перебор ключей в словаре: ')
    return x


@time_check
def operation_lst(lst):     # Сложность: O(N^2) - квадратичная
    x = 0
    for i in lst:               # O(N)
        if i in lst:            # O(N)
            lst[x] += 1         # O(1)
        x += 1
    print('Перебор элементов списка:')
    return x


@time_check
def operation_dict_2(dct1, dct2):       # Сложность: O(N) - линейная
    dct3 = {}                           # O(1)
    for key, value in dct1.items():     # O(N)
        if key in dct2.keys():          # O(1)
            dct3[key] = value           # O(1)
    len_d = len(dct3)                   # O(1)
    print(f'Перебор ключей в одном словаре и проверка их вхождений ({len_d}) в другом:')    # O(1)
    return len_d                        # O(1)


@time_check
def operation_list_2(lst1, lst2):   # Сложность: O(N^2) - квадратичная
    lst3 = []                   # O(1)
    for el in lst1:             # O(N)
        if el in lst2:          # O(N)
            lst3.append(el)     # O(1)
    len_lst = len(lst3)         # O(1)
    print(f'Перебор элементов в одном списке и проверка их вхождений ({len_lst}) в другом:')    # O(1)
    return len_lst              # O(1)


"""Создание пустых списков и словарей"""
list1, list2 = [], []
dict1, dict2 = {}, {}

"""Заполнение списков и словарей"""
fill_list(list1)
fill_dict(dict1)
fill_list(list2)
fill_dict(dict2)

"""Операции над ними"""
operation_dict(dict1)
operation_lst(list1)
operation_dict_2(dict1, dict2)
operation_list_2(list1, list2)

"""Вывод: Заполнение списков и словарей происходит примерно за одинаковое время, так как сложность 
   выполнения алгоритмов равна и составляет O(N).
   А вот операции над списками заняли гораздо больше времени, чем аналогичные операции над словарями, 
   так как в списке для сравнения приходится перебирать все элементы, и сложность этого процесса составляет
   O(N^2), а в словаре производится поиск по ключу, что гораздо быстрее и сложность составляет O(N).
   В остальном, операции добавления элементов, присваивание и изменение значений, занимают равное
   время как для списков, так и для словарей."""
