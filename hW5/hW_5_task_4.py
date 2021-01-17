"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
import string
from collections import OrderedDict
import timeit
my_list = [(0,'a'), (1,'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, 'f'), (6,'g'), (7, 'h'), (8,'i'), (9, 'j'), (10,'k'), (11, 'l'), (12, 'm'), (13,'n'), (14,'o'), (15,'p'), (16,'q'), (17,'r'), (18,'s'), (19,'t'), (20,'u'), (21,'v'), (22,'w'), (23,'x'), (24,'y'), (25,'z')]
my_str = (0,'a'), (1,'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, 'f'), (6,'g'), (7, 'h'), (8,'i'), (9, 'j'), (10,'k'), (11, 'l'), (12, 'm'), (13,'n'), (14,'o'), (15,'p'), (16,'q'), (17,'r'), (18,'s'), (19,'t'), (20,'u'), (21,'v'), (22,'w'), (23,'x'), (24,'y'), (25,'z')

# for i in range(0, len(string.ascii_lowercase)):
#     n = i,''.join(string.ascii_lowercase[i])
#     my_list.append(n)


def cr_dict():
    my_dict = dict(my_list)
    return my_dict


def cr_Ord_dict():
    NEW_DICT = OrderedDict(my_list)
    return NEW_DICT


print(timeit.timeit("cr_dict()", setup="from __main__ import cr_dict"))
print(timeit.timeit("cr_Ord_dict()", setup="from __main__ import cr_Ord_dict"))
"""
Создание словаря
1.1237954
2.8072124
"""


my_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
NEW_DICT = OrderedDict([(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, 'f'), (6, 'g'), (7, 'h'), (8, 'i'), (9, 'j'), (10, 'k'), (11, 'l'), (12, 'm'), (13, 'n'), (14, 'o'), (15, 'p'), (16, 'q'), (17, 'r'), (18, 's'), (19, 't'), (20, 'u'), (21, 'v'), (22, 'w'), (23, 'x'), (24, 'y'), (25, 'z')])


def get_dic_keys():
    return my_dict.keys()


def get_Ord_dic_keys():
    return OrderedDict.keys(NEW_DICT)


print(timeit.timeit("get_dic_keys()", setup="from __main__ import get_dic_keys"))
print(timeit.timeit("get_Ord_dic_keys()", setup="from __main__ import get_Ord_dic_keys"))

"""
Получение ключей
0.08434689999999989
0.10215640000000015
"""

up_dic = {26:'A', 27:'B', 28:'C', 29: 'D', 30: 'E'}


def upd_dic_keys():
    for k,v in up_dic.items():
        my_dict[k] = up_dic[k]
    return my_dict


def upd_Ord_dic_keys():
    for k, v in up_dic.items():
        NEW_DICT[k] = up_dic[k]
    return NEW_DICT

# print(upd_dic_keys())
# print(upd_Ord_dic_keys())

print(timeit.timeit("upd_dic_keys()", setup="from __main__ import upd_dic_keys"))
print(timeit.timeit("upd_Ord_dic_keys()", setup="from __main__ import upd_Ord_dic_keys"))

"""
Добавление элементов
0.46162910000000057
0.5183900000000001
"""

"""
Практика показывает, что создание, получение значений и добавление элементов
быстрее выполняется в обычном словаре, чем в OrderedDict
"""