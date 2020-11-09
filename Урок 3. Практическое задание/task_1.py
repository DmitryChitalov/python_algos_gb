"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
from time import time
from random import randint

dict_1, list_1 = {}, []


def time_count(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        out = func(*args, **kwargs)
        end_time = time()
        print(f'Время выполнения: {end_time - start_time} секунд.')
        return out
    return wrapper


@time_count
def dict_filling(dict_obj):
    for i in range(3000):
        dict_obj[f'Element_{i}'] = randint(1, 100)
    print(dict_1)


@time_count
def dict_out(dict_obj):
    for k in dict_obj.keys():
        print(f'{k}: {dict_obj[k]}.', end=' ')
    print()


@time_count
def dict_search_by_val(dict_obj, val):
    found = False
    for k in dict_obj.keys():
        if dict_obj[k] == val:
            print(f'Значение {val} найдено по ключу {k}.')
            found = True
    if not found:
        print('Искомое значение не найдено.')


@time_count
def list_filling(list_obj):
    for i in range(3000):
        list_obj.append(randint(1, 100))
    print(list_1)


@time_count
def list_out(list_obj):
    for i in list_obj:
        print(i, end=' ')
    print()


@time_count
def list_search(list_obj, val):
    found = False
    for i in range(len(list_obj)):
        if list_obj[i] == val:
            print(f'Значение {val} найдено на позиции {i} в списке.')
            found = True
    if not found:
        print('Искомое значение не найдено.')


# Словари:
print(f'Заполнение словаря:')
dict_filling(dict_1)

print(f'\nВывод из словаря:')
dict_out(dict_1)

print(f'\nПоиск значения "9" по словарю:')
dict_search_by_val(dict_1, 9)

print()

# Списки:
print(f'Заполнение списка:')
list_filling(list_1)

print(f'\nВывод из списка:')
list_out(list_1)

print(f'\nПоиск значения "9" по списку:')
list_search(list_1, 9)

print()

'''
Наблюдения и выводы:
Операции по заполнению и выводу элементов со словарями занимают больше времени, чем со списками.
Операция поиска занимает примерно одинаковое количество времени.
'''
