"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""

import time
import random
from string import ascii_uppercase
from memory_profiler import memory_usage, profile
import numpy as np
import sys


my_str_1 = ''.join(random.choice(ascii_uppercase) for elem in range(1000000))
my_str_2 = ''.join(random.choice(ascii_uppercase) for el in range(1000000))


def my_decorator(function):
    def wrapper(*args, **kwargs):
        t_1 = time.process_time()
        m_1 = memory_usage()
        function(*args, **kwargs)
        t_2 = time.process_time()
        m_2 = memory_usage()
        process_time = t_2 - t_1
        process_memory = m_2[0] - m_1[0]
        return f'Время выполнения: {process_time}, память: {process_memory}'
    return wrapper


@my_decorator
def fill_list():
    return [el for el in range(0, 100000)]


@my_decorator
def fill_list_numpy():
    return np.array([el for el in range(0, 100000)])


@profile()
def full_program():
    print(fill_list())
    print(fill_list_numpy())


if __name__ == '__main__':
    """Python 3.8, x64"""
    full_program()
# использование библиотеки NumPy существенно оптимизирует использование памяти при работе с массивами.

