"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
"""
Копирование словаря на порядок быстрее, чем копирование OrderedDict: 
copy standard_dict: 0.004970299999999997 seconds
copy ordered_dict: 0.0412784 seconds

Проверяю внешнюю функцию len(), чтоб потом иметь возможность использовать ее внутри функций.
Практически одинаковая скорость.
len standard_dict: 0.0005616000000000093 seconds
len ordered_dict: 0.0005780000000000091 seconds

Стандартное добавление значений: new_elem[idx] = value
Стандартная чуть-чуть быстрее.
add items standard_dict: 0.04479570000000001 seconds
add items ordered_dict: 0.0564964 seconds

Добавляю с использованием setdefault()
Аналогично. Разница минимальна
add items standard_dict: 0.0250349 seconds
add items ordered_dict: 0.02723629999999999 seconds

Удаление из словарей. В стандартном словаре немного быстрее 
pop items standard_dict: 0.013190900000000005 seconds
pop items ordered_dict: 0.015443800000000008 seconds

Обновление элементов словаря. В стандартом словаре в 2 раза быстрее.
update items standard_dict: 0.011670499999999973 seconds
update items ordered_dict: 0.025595000000000034 seconds

Вывод: В версиях python3+ точно нет смысла использовать OrderedDict. Эта коллекция проигрывает стандартному словарю.
"""
from collections import OrderedDict
from timeit import timeit

standard_dict = {}
ordered_dict = OrderedDict()


def standard_dict_add1(number):
    len_dict = len(standard_dict)
    for n in range(number):
        standard_dict[len_dict + n] = len_dict**n


def ordered_dict_add1(number):
    len_dict = len(ordered_dict)
    for n in range(number):
        ordered_dict[len_dict + n] = len_dict**n


def standard_dict_add2(number):
    len_dict = len(standard_dict)
    for n in range(len_dict, len_dict + number):
        standard_dict.setdefault(n)


def ordered_dict_add2(number):
    len_dict = len(ordered_dict)
    for n in range(len_dict, len_dict + number):
        ordered_dict.setdefault(n)


def standard_dict_pop(number):
    some_list = []
    for n in range(number):
        some_list =standard_dict.popitem()


def ordered_dict_pop(number):
    some_list = []
    for n in range(number):
        some_list = ordered_dict.popitem()


def st_dict_update(number):
    for n in range(number):
        standard_dict.update({n: 5*n})


def ord_dict_update(number):
    for n in range(number):
        ordered_dict.update({n: 5*n})


for i in range(40):
    standard_dict[i] = (-1)**i * i*3
    ordered_dict[i] = (-1)**i * i*3

print(standard_dict)
print(ordered_dict)

# copy()
print(f"copy standard_dict: {timeit('standard_dict.copy()', globals=globals(), number=10000)} seconds")
print(f"copy ordered_dict: {timeit('ordered_dict.copy()', globals=globals(), number=10000)} seconds")

standard_len = len(standard_dict)
ordered_len = len(ordered_dict)
# len - внешняя функция
print(f"len standard_dict: {timeit('len(standard_dict)', globals=globals(), number=10000)} seconds")
print(f"len ordered_dict: {timeit('len(ordered_dict)', globals=globals(), number=10000)} seconds")
print(len(standard_dict))
number = 7
# добавляем number элементов
print(f"add items standard_dict: {timeit('standard_dict_add1(number)', globals=globals(), number=10000)} seconds")
print(f"add items ordered_dict: {timeit('ordered_dict_add1(number)', globals=globals(), number=10000)} seconds")
print(len(standard_dict))
print(f"add items standard_dict: {timeit('standard_dict_add2(number)', globals=globals(), number=10000)} seconds")
print(f"add items ordered_dict: {timeit('ordered_dict_add2(number)', globals=globals(), number=10000)} seconds")
print(len(standard_dict))
# извлекаем элементы
number = 3
print(f"pop items standard_dict: {timeit('standard_dict_pop(number)', globals=globals(), number=10000)} seconds")
print(f"pop items ordered_dict: {timeit('ordered_dict_pop(number)', globals=globals(), number=10000)} seconds")
print(len(standard_dict))
# обновляем элементы
print(f"update items standard_dict: {timeit('st_dict_update(number)', globals=globals(), number=10000)} seconds")
print(f"update items ordered_dict: {timeit('ord_dict_update(number)', globals=globals(), number=10000)} seconds")
print(len(standard_dict))