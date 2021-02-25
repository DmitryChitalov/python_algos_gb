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
import time


def time_decorator(func):
    def timer(*args, **kwargs):
        t_start = time.time()
        result = func(*args, **kwargs)
        t_end = time.time()
        return result, t_end - t_start

    return timer


@time_decorator
def list_func(length):
    result = []
    for i in range(length):
        result.append(i)
    return result


@time_decorator
def dict_func(length):
    result = {}
    for i in range(length):
        result[i] = f'number {i}'
    return result


@time_decorator
def check_dict_key(dict_obj):
    v = dict_obj[6543]
    print(v)


@time_decorator
def check_list_index(list_obj):
    for i in range(len(list_obj)):
        if i == 6543:
            print(list_obj[i])


@time_decorator
def check_dict_value(dict_obj):
    for v in dict_obj.values():
        if v == 'number 6543':
            print(v)


@time_decorator
def check_list_value(list_obj):
    for v in list_obj:
        if v == 6543:
            print(v)


new_list_1, list_time_1 = list_func(10000)
new_dict_1, dict_time_1 = dict_func(10000)
print('Create LIST 10000: ', list_time_1)
print('Create DICT 10000: ', dict_time_1)

new_list_2, list_time_2 = list_func(100000)
new_dict_2, dict_time_2 = dict_func(1000000)
print('Create LIST 100000: ', list_time_2)
print('Create DICT 100000: ', dict_time_2)

new_list_3, list_time_3 = list_func(1000000)
new_dict_3, dict_time_3 = dict_func(1000000)
print('Create LIST 1000000: ', list_time_3)
print('Create DICT 1000000: ', dict_time_3)

# Словарь строится дольше, т.к. необходимо вычислять хеши ключей

print('*********************')

print('Check LIST Index 10000: ', check_list_index(new_list_1)[1])
print('Check DICT Key 10000: ', check_dict_key(new_dict_1)[1])
print('Check LIST Index 100000: ', check_list_index(new_list_2)[1])
print('Check DICT Key 100000: ', check_dict_key(new_dict_2)[1])
print('Check LIST Index 1000000: ', check_list_index(new_list_3)[1])
print('Check DICT Key 1000000: ', check_dict_key(new_dict_3)[1])

# Поиск элемента в словаре по ключу происчходит гораздо быстрее,
# чем поиск в списке по индексу

print('*********************')

print('Check LIST by Value 10000: ', check_list_value(new_list_1)[1])
print('Check DICT by Value 10000: ', check_dict_value(new_dict_1)[1])
print('Check LIST by Value 100000: ', check_list_value(new_list_2)[1])
print('Check DICT by Value 100000: ', check_dict_value(new_dict_2)[1])
print('Check LIST by Value 1000000: ', check_list_value(new_list_3)[1])
print('Check DICT by Value 1000000: ', check_dict_value(new_dict_3)[1])

# Поиск элемента из словаря по значениям происходит дольше,
# чем поиск по значениям в списке