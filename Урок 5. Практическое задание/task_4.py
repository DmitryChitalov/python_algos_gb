"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from timeit import timeit

num = 50000

def_dict = dict()
def_o_dict = OrderedDict()

############################################################
def populate_dict(dict, num):
    for i in range(num):
        dict[-i] = i

def populate_o_dict(o_dict, num):
    for i in range(num):
        o_dict[-i] = i

def get_dict(dict):
    for i in range(len(dict)):
        item = dict.get(i)


def get_o_dict(o_dict):
    for i in range(len(o_dict)):
        item = o_dict.get(i)


def pop_dict(dict):
    for i in range(len(dict)):
        item = dict.popitem()


def pop_o_dict(my_o_dict):
    for i in range(len(my_o_dict)):
        item = my_o_dict.popitem()
############################################################

print(f"populate_dict(def_dict, num): ",
      timeit(f"populate_dict(def_dict, num)", globals=globals(), number=1000))
print(f"populate_o_dict(def_o_dict, num): ",
      timeit(f"populate_o_dict(def_o_dict, num)", globals=globals(), number=1000))

############################################################
my_dict = def_dict.copy()
my_o_dict = def_o_dict.copy()
print(f"get_dict(my_dict): ",
      timeit(f"get_dict(my_dict)", globals=globals(), number=1000))
print(f"get_o_dict(my_o_dict): ",
      timeit(f"get_o_dict(my_o_dict)", globals=globals(), number=1000))

############################################################
my_dict = def_dict.copy()
my_o_dict = def_o_dict.copy()
print(f"pop_dict(my_dict): ",
      timeit(f"pop_dict(my_dict)", globals=globals(), number=1000))
print(f"pop_o_dict(my_o_dict): ",
      timeit(f"pop_o_dict(my_o_dict)", globals=globals(), number=1000))

############################################################
#print(def_dict)
#print(def_o_dict)

'''
populate_dict(def_dict, num):  4.112933316
populate_o_dict(def_o_dict, num):  5.663962055000001
get_dict(my_dict):  2.682989867
get_o_dict(my_o_dict):  2.852375304999999
pop_dict(my_dict):  0.004347088999999471
pop_o_dict(my_o_dict):  0.007390769000000574

Есть подозрение что просто dict работает быстрее OrderedDict во всех случаях

'''
