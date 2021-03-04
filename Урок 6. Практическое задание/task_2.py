"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""

from memory_profiler import profile


@profile
def my_func_gen(j):
    list_m = [i for i in range(j + 1)]
    return list_m


@profile
def my_func(j):
    list_m = []
    my_list = range(j + 1)
    for i in my_list:
        list_m.append(i)
    return list_m


print(my_func_gen(9999))
print(my_func(9999))
print("При работе итератора в первом случае экономия МЕМ в 2 раза")
