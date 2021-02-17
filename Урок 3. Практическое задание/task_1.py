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


def time_count(func):
    import time
    def wrapper(*args):
        start = time.time()
        return_value = func(*args)
        stop = time.time()
        print(f"Время выполнения {func.__name__} {stop - start} секунд.")
        return return_value

    return wrapper


@time_count
def dict_init(length):
    my_dict = dict()
    for idx in range(length):
        my_dict[idx] = idx
    return my_dict


@time_count
def list_init(length):
    my_list = []
    for idx in range(length):
        my_list.append(idx)
    return my_list


@time_count
def copy_dict(dict_arg):
    return dict_arg.copy()


@time_count
def copy_list(list_arg):
    return list_arg.copy()


@time_count
def pop_from_dict(dict_arg):
    for id in range(len(dict_arg)):
        num = dict_arg.pop(id)


@time_count
def pop_from_list(list_arg):
    for id in range(len(list_arg)):
        num = list_arg.pop()


@time_count
def get_from_dict(dict_arg):
    for id in range(len(dict_arg), 1, -1):
        num = dict_arg.get(id)


@time_count
def get_from_list(list_arg):
    for id in range(len(list_arg) - 1, 0, -1):
        num = list_arg.index(id)


n = 10000
my_dict1 = dict_init(n)
my_list1 = list_init(n)
my_dict2 = copy_dict(my_dict1)
my_list2 = copy_list(my_list1)
get_from_dict(my_dict2)
get_from_list(my_list2)
pop_from_dict(my_dict1)
pop_from_list(my_list1)

# n = 10000
# Время выполнения dict_init 0.0010004043579101562 секунд.
# Время выполнения list_init 0.0009989738464355469 секунд.
# Время выполнения copy_dict 0.0 секунд.
# Время выполнения copy_list 0.0 секунд.
# Время выполнения get_from_dict 0.001999378204345703 секунд.
# Время выполнения get_from_list 1.0301456451416016 секунд.
# Время выполнения pop_from_dict 0.0019991397857666016 секунд.
# Время выполнения pop_from_list 0.002001523971557617 секунд.

# при росте N доступ к элементу списка по значению сильно замедляется
# в остальных представленных операциях разница между списком и словарем не велика.
