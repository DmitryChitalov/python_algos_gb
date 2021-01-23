"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, библиотеки) для оптимизации памяти и
доказать! (наглядно, кодом) их эффективность (на примере профилировщика)
"""
from memory_profiler import memory_usage

'''
Применение объектов-генераторов вместо списков позволяет сократить затраты памяти на выполнение программы.
'''


def check_memory(func):
    """
    Функция, позволяющая определить дельту использования памяти между началом и концом программы.
    """

    def start(*args, **kwargs):
        diff_memory = []
        memory_1 = memory_usage()
        print(f'memory_1 - {memory_1}')
        func(*args)
        memory_2 = memory_usage()
        print(f'memory_2 - {memory_2}')
        diff_memory.append(memory_2[0] - memory_1[0])

        print(f'{sum(diff_memory)} MiB')

    return start


@check_memory
def total_multiple(first_num, second_num):
    """
    Написать функцию нахождения общих кратных для двух чисел.
    """
    array = list(range(100000))
    first_multiple = [i for i in array if i % first_num == 0]
    second_multiple = [i for i in first_multiple if i % second_num == 0]
    return second_multiple


total_multiple(13, 25)
'''
memory_1 - [18.58984375]
memory_2 - [18.91015625]
0.3203125 MiB
'''


@check_memory
def total_multiple_gen(first_num, second_num):
    """
    Написать функцию нахождения общих кратных для двух чисел.
    """
    array = (range(100000))
    first_multiple = (i for i in array if i % first_num == 0)
    second_multiple = (i for i in first_multiple if i % second_num == 0)
    return list(second_multiple)


total_multiple_gen(13, 25)
'''
memory_1 - [18.91015625]
memory_2 - [18.91015625]
0.0 MiB'''

'''
Вывод: Инткремент в 0.3203125 MiB при выполнении программы с применением списков против нулевого инкремента для той же
программы, но с применением объектов-генераторов.
'''