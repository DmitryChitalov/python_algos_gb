"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
from memory_profiler import profile
from random import randrange


@profile
def get_list_even_elems(list_obj):
    gen_obj = (i for i in list_obj if i % 2 != 0)
    return list(gen_obj)


@profile
def get_list_even_elems2(list_obj):
    even_list = []
    for i in list_obj:
        if i % 2 != 0:
            even_list.append(i)
    return even_list


test_list = [randrange(-100, 100) for i in range(1000)]
get_list_even_elems(test_list)
get_list_even_elems2(test_list)

"""
Использование генератора для создания списка в данном примере 
демонстрирует экономию памяти при решении задачи почти в два раза
"""
