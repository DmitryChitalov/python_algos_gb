"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""

from random import randint
from copy import deepcopy
from memory_profiler import profile
import helper_zlib
import json
import numpy


# Данные для тестирования
some_str_list = [
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    'Pellentesque imperdiet facilisis leo, cursus ullamcorper elit malesuada sed.',
    'Aenean bibendum sem quis sollicitudin eleifend.',
    'Quisque aliquam ligula ipsum, eget mattis nibh elementum eget.',
    'Phasellus non sollicitudin ipsum, ut tempus nibh.',
    'Pellentesque ut mauris at diam lacinia egestas.',
    'Ut viverra quis nunc at rhoncus.',
    'Vestibulum facilisis ac neque in sagittis.',
    'Mauris eu dictum velit, sed semper turpis.',
    'Integer porttitor luctus accumsan.',
    'Nunc vulputate tincidunt posuere.',
    'Cras arcu tortor, consectetur ut ornare sit amet, malesuada sed justo.',
    'Donec lacus dolor, hendrerit id pretium at, condimentum eget massa.',
    'Proin sagittis blandit libero sit amet suscipit.',
    'Nullam faucibus sollicitudin nisi, ut posuere lorem tristique id.',
    'Suspendisse id vestibulum justo, vitae ornare elit.',
    'Quisque accumsan sagittis pulvinar.',
    'Aliquam id quam volutpat, dictum neque vel, egestas nunc.',
    'Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.',
    'Vestibulum non nisi ut elit tempus luctus.',
    'Vestibulum tempor molestie ipsum ut bibendum.',
    'Proin sagittis ex nec mi faucibus tristique.',
    'Praesent egestas lectus a libero rhoncus, ut rutrum tellus condimentum.',
    'Proin quis pulvinar tortor.',
    'Sed magna nibh, venenatis vitae lorem a, eleifend fermentum tellus.',
    'Suspendisse laoreet feugiat diam in luctus.',
    'Praesent interdum finibus elit nec auctor.',
    'Vivamus fermentum eros a lectus ornare maximus.',
    'Curabitur sit amet aliquam dolor.',
    'Sed quis elementum massa.',
    'Pellentesque luctus, neque nec sollicitudin ornare, ligula erat odio, at finibus metus turpis nec dui.',
    'Aliquam blandit diam vel elit pellentesque rhoncus fringilla ac metus.',
    'Morbi consectetur justo a enim aliquet, quis malesuada sapien malesuada.',
    'Curabitur mollis ac felis finibus convallis.',
    'Donec id tellus mattis, pellentesque risus sit amet, semper eros.',
    'Nam non rhoncus velit.',
    'Nunc nec odio et magna ultricies suscipit ut at risus.',
    'Praesent at dolor et nunc pulvinar tempor eu in dui.',
    'Aliquam at lobortis sapien.',
    'Mauris ac finibus enim, et scelerisque nulla.',
    'Nullam maximus est enim, non lobortis elit venenatis interdum.',
    'Proin tincidunt facilisis nibh, et eleifend purus rhoncus vitae.',
    'Nam sed ex arcu.',
    'Donec et rutrum urna.',
    'Nunc a magna tincidunt, aliquam massa non, laoreet neque.',
    'Quisque nisi turpis, scelerisque semper bibendum in, vehicula id purus.',
    'Aliquam sollicitudin condimentum nulla ut sagittis.',
    'Praesent consequat odio eget mauris luctus viverra.',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    'Cras laoreet bibendum dolor, at imperdiet ipsum interdum sit amet.',
    'Morbi facilisis viverra tincidunt.',
    'Proin et velit nunc.',
    'Aenean mattis mi vitae mi tempus commodo.',
    'Phasellus laoreet velit sit amet pellentesque malesuada.',
    'Donec tempor blandit nisl, in ornare odio facilisis eu.',
    'Donec in neque porta, vehicula augue ut, auctor tortor.',
    'Donec nec nisl nibh.',
    'Sed egestas dictum felis, tincidunt tristique magna dictum ac.',
    'Mauris lectus erat, consectetur a magna et, congue ornare enim.'
]

# Добавим еще текста в список
max_i = len(some_str_list) - 1
for _ in range(100000):
    some_str_list.append(some_str_list[randint(0, max_i)])

# Сгенерим еще список из случайных чисел
some_int_list = [randint(0, 1000) for _ in range(1000000)]


########################################
"""
Эксперимент 1. Сжатие данных.
Была мысль попробовать како-либо зжатие данных, для временного хранения в памяти:
Решил попробовать сериализацию и компрессия.
"""


@profile
def func_1():
    """Простое копирование списка
    """
    v1 = deepcopy(some_str_list)
    print(f"Предложений: {len(v1)}")
    v2 = deepcopy(some_int_list)
    print(f"Чисел: {len(v2)}")
    del v1
    del v2
    return


@profile
def func_2():
    """Сериализация списка и компрессия
    """
    json1 = json.dumps(some_str_list).encode('utf-8')
    print(len(json1))
    v1 = helper_zlib.gzcompress(json1)
    print(len(v1))
    json2 = json.dumps(some_int_list).encode('utf-8')
    print(len(json2))
    v2 = helper_zlib.gzcompress(json2)
    print(len(v2))
    del json1
    del json2
    del v1
    del v2
    return


# Выполним профилирование списка в чистом виде
func_1()

# Выполним профилирование списка с компрессией
func_2()

"""
Вывод:
Использовать сериализацию и/или сжатие совсем не эффективно.
"""


########################################
"""
Профилировка памяти с использованием:
    - списков list
    - массивов numpy.array
    - кортежей tuple

Python 3.8.5
ОС: Linux Mint 20 x64
"""


@profile
def gen_list():
    lst1 = deepcopy(some_int_list)
    print(len(lst1))
    lst2 = deepcopy(some_str_list)
    print(len(lst2))
    del lst1
    del lst2
    return


@profile
def gen_array():
    arr1 = numpy.array(some_int_list)
    print(len(arr1))
    arr2 = numpy.array(some_str_list)
    print(len(arr2))
    del arr1
    del arr2
    return


@profile
def gen_tuple():
    tpl1 = tuple(some_int_list)
    print(len(tpl1))
    tpl2 = tuple(some_str_list)
    print(len(tpl2))
    del tpl1
    del tpl2
    return



# Генерация списка
gen_list()
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   155     64.1 MiB     64.1 MiB           1   @profile
   156                                         def gen_list():
   157     72.0 MiB      7.8 MiB           1       lst1 = deepcopy(some_int_list)
   158     72.0 MiB      0.0 MiB           1       print(len(lst1))
   159     72.6 MiB      0.6 MiB           1       lst2 = deepcopy(some_str_list)
   160     72.6 MiB      0.0 MiB           1       print(len(lst2))
   161     65.1 MiB     -7.5 MiB           1       del lst1
   162     64.3 MiB     -0.8 MiB           1       del lst2
   163     64.3 MiB      0.0 MiB           1       return
"""

# Генерация массива numpy
gen_array()
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   166     64.3 MiB     64.3 MiB           1   @profile
   167                                         def gen_array():
   168     71.6 MiB      7.2 MiB           1       arr1 = numpy.array(some_int_list)
   169     71.6 MiB      0.0 MiB           1       print(len(arr1))
   170    110.5 MiB     38.9 MiB           1       arr2 = numpy.array(some_str_list)
   171    110.5 MiB      0.0 MiB           1       print(len(arr2))
   172    110.5 MiB      0.0 MiB           1       del arr1
   173     71.7 MiB    -38.8 MiB           1       del arr2
   174     71.7 MiB      0.0 MiB           1       return
"""

# Генерация кортежа
gen_tuple()
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   177     64.0 MiB     64.0 MiB           1   @profile
   178                                         def gen_tuple():
   179     71.7 MiB      7.7 MiB           1       tpl1 = tuple(some_int_list)
   180     71.7 MiB      0.0 MiB           1       print(len(tpl1))
   181     72.5 MiB      0.8 MiB           1       tpl2 = tuple(some_str_list)
   182     72.5 MiB      0.0 MiB           1       print(len(tpl2))
   183     64.9 MiB     -7.5 MiB           1       del tpl1
   184     64.2 MiB     -0.8 MiB           1       del tpl2
   185     64.2 MiB      0.0 MiB           1       return
"""

"""
Вывод:
Объем анимаемой памяти зависит от типа данных.
Если целые числа, то numpy.array - лучше, но этот модуль очень плохо хранит строки.
Кортежи занимают примерно тот же объем что и списки, числа чуть лучше, строки чуть хуже.
"""

"""
Была еще мысль хранить временные переменные в базах данных, таких как Redis, но реализовывать не стал.
Больше никаких вариантов найти не смог.
"""
