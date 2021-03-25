"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from timer import timer
from random import randint

NUMBER = 5000


@timer(NUMBER)
def fill_obj(obj, num):
    for item in range(num):
        obj[item] = randint(1, 100)


@timer(NUMBER)
def get_value(obj):
    key = randint(0, len(obj) - 1)
    value = obj.get(key)
    return value


@timer(NUMBER)
def get_keys(obj):
    keys = obj.keys()
    return keys


@timer(NUMBER)
def get_values(obj):
    values = obj.values()
    return values


@timer(NUMBER)
def get_items(obj):
    items = obj.items()
    return items


@timer(NUMBER)
def update_values(obj):
    key = randint(0, len(obj) - 1)
    obj[key] = randint(1, 100)


@timer(NUMBER)
def pop_element(obj):
    key = list(obj.keys())[-1]
    obj.pop(key)


test_dict = dict()
test_ord_dict = OrderedDict()

print('\nЗаполнение:')
print('dict:', end=' ')
fill_obj(test_dict, 5000)
print('ordered_dict:', end=' ')
fill_obj(test_ord_dict, 5000)

# dict: 13.320371900000055
# ordered_dict: 14.01689820000002
# Замеры показывают, что заполнение OrderedDict происходит несколько медленнее, чем заполнение обычного словаря.
# Вероятно, это обусловлено созданием дополнительного функционала для хранения порядка элементов.

print('\nПолучение значения по ключу:')
print('dict:', end=' ')
get_value(test_dict)
print('ordered_dict:', end=' ')
get_value(test_ord_dict)

# dict: 0.004047200000133699
# ordered_dict: 0.004155200000120374
# Значения по ключу из обычного словаря получаются незначительно быстрее, чем из OrderedDict.

print('\nПолучение ключей:')
print('dict:', end=' ')
get_keys(test_dict)
print('ordered_dict:', end=' ')
get_keys(test_ord_dict)

# dict: 0.0007978999999913583
# ordered_dict: 0.0008028999999076802
# Получение списка всех ключей в словаре происходит чуть быстрее, чем в OrderedDict, но разница настолько минимальна,
# что ею можно пренебречь.

print('\nПолучение значений:')
print('dict:', end=' ')
get_values(test_dict)
print('ordered_dict:', end=' ')
get_values(test_ord_dict)

# dict: 0.0008043000002544431
# ordered_dict: 0.0007984000001037828
# Получение списка всех значений в словаре происходит чуть медленнее, чем в OrderedDict,
# но разница настолько минимальна, что ею можно пренебречь.

print('\nПолучение всех элементов:')
print('dict:', end=' ')
get_items(test_dict)
print('ordered_dict:', end=' ')
get_items(test_ord_dict)

# dict: 0.0007941000000073473
# ordered_dict: 0.0007918999999816378
# Получение всех элементов в словаре происходит чуть медленнее, чем в OrderedDict,
# но разница настолько минимальна, что ею можно пренебречь.


print('\nИзменение значения по ключу:')
print('dict:', end=' ')
update_values(test_dict)
print('ordered_dict:', end=' ')
update_values(test_ord_dict)

# dict: 0.006664499999914142
# ordered_dict: 0.006614699999971663
# Изменение значения по ключу в словаре происходит чуть медленнее, чем в OrderedDict,
# но разница настолько минимальна, что ею можно пренебречь.


print('\nИзвлечение элемента по ключу:')
print('dict:', end=' ')
pop_element(test_dict)
print('ordered_dict:', end=' ')
pop_element(test_ord_dict)

# dict: 0.06767839999999836
# ordered_dict: 0.18841310000021494
# Извлечение элемента по ключу в словаре происходит ощутимо быстрее, чем в OrderedDict,
# что обусловлено, вероятно, перестроением порядка индексов элементов после каждого удаления.

# Стоит отметить, что в отличие от обычного словаря OrderedDict имеет метод move_to_end,
# позволяющий перемещать элементы словаря в его конец или начало. Это практически единственное значимое отличие
# от обычных словарей начиная с версии 3.7.

# Таким образом, в настоящее время OrderedDict имеет смысл использовать только в рамках тех библиотек или фреймворков,
# где он используется для реализации какого-то функционала или в версиях Python до 3.7.
# В прочих случаях обычный словарь работает либо быстрее, либо примерно с той же скоростью,
# имеет более читаемое представление и с версии 3.7 сохраняет порядок внесения элементов.

