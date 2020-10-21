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


# Данные для тестирования
some_dict = {'text': [
    [
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
        'Proin sagittis blandit libero sit amet suscipit.'
    ],
    [
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
        'Sed magna nibh, venenatis vitae lorem a, eleifend fermentum tellus.'
    ],
    [
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
        'Nullam maximus est enim, non lobortis elit venenatis interdum.'
    ],
    [
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
        'Proin et velit nunc.'
    ],
    [
        'Aenean mattis mi vitae mi tempus commodo.',
        'Phasellus laoreet velit sit amet pellentesque malesuada.',
        'Donec tempor blandit nisl, in ornare odio facilisis eu.',
        'Donec in neque porta, vehicula augue ut, auctor tortor.',
        'Donec nec nisl nibh.',
        'Sed egestas dictum felis, tincidunt tristique magna dictum ac.',
        'Mauris lectus erat, consectetur a magna et, congue ornare enim.'
    ]
], 'digits': [randint(0, 100) for _ in range(10000)]}

# Добавим еще текста в словарь
# for _ in range(25):
#     some_dict['text'].append(some_dict['text'][randint(0, len(some_dict['text']) - 1)])


########################################
@profile
def func_1():
    v = deepcopy(some_dict)
    print(f"Абзацев: {len(v['text'])}")
    print(f"Чисел: {len(v['digits'])}")


# Выполним профилирование словаря в чистом виде
func_1()


########################################
@profile
def func_2():
    v = helper_zlib.gzcompress(json.dumps(some_dict).encode('utf-8'))
    print(len(v))


# Выполним профилирование словаря с компрессией
func_2()

"""
Использовать сжатие совсем не эффективно
"""


########################################
# def my_deepcopy(obj):
#     if str(type(obj)) == "<class 'dict'>" or str(type(obj)) == "<class 'dict'>":
#         pass
#
#
# @profile
# def func_3():
#     pass
#
#
# #
# # func_3()
# print(str(type(some_dict)))
# print(str(type(some_dict)) == "<class 'dict'>")
