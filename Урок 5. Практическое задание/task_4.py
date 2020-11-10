"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
import random
from timeit import timeit

stand_lst = [random.randrange(0, 1000, 1) for i in range(1000)]

dict_ = {}
for i in range(len(stand_lst)):
    dict_[i] = stand_lst[i]

order_dict = OrderedDict()
for i in range(len(stand_lst)):
    order_dict[i] = stand_lst[i]

def time_(dict_):
    copy_d = dict_.copy()
    dict_.get(0)
    dict_.items()
    dict_.keys()
    dict_.update({1:2})
    dict_.values()

###
print(timeit("time_(dict_)", setup="from __main__ import time_, dict_"))
print(timeit("time_(order_dict)", setup="from __main__ import time_, order_dict"))

# у меня разница получается, примерно, 60 секунд
# не в пользу order_dict
# уже второе задание не в пользу collections
# я что-то не так замеряю?