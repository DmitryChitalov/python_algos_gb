"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit


def add_reg_dict(num):
    regular_dict = {}
    for i in range(num):
        regular_dict[i] = i
    return regular_dict


def add_ordered_dict(num):
    ordered_dict = OrderedDict()
    for i in range(num):
        ordered_dict[i] = i
    return ordered_dict


n = 1000000
dict_reg = add_reg_dict(n)
dict_ord = add_ordered_dict(n)


def del_el_dict_reg(num):
    for i in range(1, n):
        dict_reg.pop(i)


def del_el_dict_ord(num):
    for i in range(n):
        dict_ord.pop(i)


print(f"Добавление элементов в обычный dict" 
      f" {timeit('add_reg_dict(n)', 'from __main__ import add_reg_dict, n', number=1)}")
print(f"Добавление элементов в OrderedDict"
      f" {timeit('add_ordered_dict(n)', 'from __main__ import add_ordered_dict, n', number=1)}")
print(f"Удаление элементов из обычного dict"
      f" {timeit('del_el_dict_reg(n)', 'from __main__ import del_el_dict_reg, n, dict_reg', number=1)}")
print(f"Удаление элементов из OrderedDict"
      f" {timeit('del_el_dict_ord(n)', 'from __main__ import del_el_dict_ord, n, dict_ord', number=1)}")

"""
Для n = 10000000
Добавление элементов в обычный dict 1.1831708999999995
Добавление элементов в OrderedDict 2.1390211
Удаление элементов из обычного dict 1.9369309000000001
Удаление элементов из OrderedDict 4.309243499999999

По замерам видно, что добавление элементов в обычный словарь в 2 раза быстрее чем в OrderedDict
Удаление элементов, так же быстрее в 2 раза
Вывод: Изпользование коллекции OrderedDict нецелесообразно, так как нет теперь необходимости заказывать вид словаря,
начиная с Python 3.6 словари упорядоченные

"""