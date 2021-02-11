"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from timeit import timeit
from collections import OrderedDict

num = 100000
my_dict1 = dict()
for i in range(num):
    my_dict1[num] = num
my_o_dict1 = OrderedDict()
for i in range(num):
    my_dict1[num] = num


# print(type(my_o_dict), my_o_dict)

def fill_dict(num):
    my_dict = dict()
    for i in range(num):
        my_dict[num] = num


def fill_o_dict(num):
    my_dict = OrderedDict()
    for i in range(num):
        my_dict[num] = num


def get_dict(my_dict):
    for i in range(len(my_dict)):
        item = my_dict.get(i)


def get_o_dict(my_o_dict):
    for i in range(len(my_o_dict)):
        item = my_o_dict.get(i)


def pop_dict(my_dict):
    for i in range(len(my_dict)):
        item = my_dict.popitem()


def pop_o_dict(my_o_dict):
    for i in range(len(my_o_dict)):
        item = my_o_dict.popitem()


# fill
print(f"fill_dict({num}): ",
      timeit(f"fill_dict({num})", globals=globals(), number=1000))
print(f"fill_o_dict({num}): ",
      timeit(f"fill_o_dict({num})", globals=globals(), number=1000))
print()
# get
print(f"get_dict(my_dict1): ",
      timeit(f"get_dict(my_dict1)", globals=globals(), number=1000))
print(f"get_o_dict(my_o_dict1): ",
      timeit(f"get_o_dict(my_o_dict1)", globals=globals(), number=1000))
print()
# pop
print(f"pop_o_dict(my_dict1): ",
      timeit(f"pop_dict(my_dict1)", globals=globals(), number=1000))
print(f"pop_o_dict(my_o_dict1): ",
      timeit(f"pop_o_dict(my_o_dict1)", globals=globals(), number=1000))
print()
# update
my_dict2 = dict()
for i in range(num):
    my_dict1[num] = num + 1
my_o_dict2 = OrderedDict()
print(f"my_dict2.update(my_dict1): ",
      timeit(f"my_dict2.update(my_dict1)", globals=globals(), number=1000))
print(f"my_o_dict2.update(my_o_dict1): ",
      timeit(f"my_o_dict2.update(my_o_dict1)", globals=globals(), number=1000))

'''
Измерения проведены для словарей размерностью 100000.
Проверено 4 операции: заполнение, get, pop, update:

fill_dict(100000):  12.592965600000001
fill_o_dict(100000):  16.2605351

get_dict(my_dict1):  0.0012946999999989828
get_o_dict(my_o_dict1):  0.0009121000000007484

pop_o_dict(my_dict1):  0.000940699999997463
pop_o_dict(my_o_dict1):  0.0009411999999997533

my_dict2.update(my_dict1):  0.00015780000000020777
my_o_dict2.update(my_o_dict1):  0.09757450000000034

На Update обычный словарь существенно быстрее, на get обычный словарь чуть 
медленнее. Остальные операции отрабатывают примерно с одной скоростью для 
обычного словаря и OrderedDict.
Вывод:
Использование OrderedDict в поздних версиях Python не имеет смысла.
'''
