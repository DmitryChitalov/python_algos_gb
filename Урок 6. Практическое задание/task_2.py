"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""

import time
import random
from string import ascii_uppercase

my_str_1 = ''.join(random.choice(ascii_uppercase) for elem in range(1000000))
my_str_2 = ''.join(random.choice(ascii_uppercase) for el in range(1000000))


def my_decorator(function):
    def wrapper(*args, **kwargs):
        t_1 = time.process_time()
        # m_1 = memory_usage()
        function(*args, **kwargs)
        t_2 = time.process_time()
        # m_2 = memory_usage()
        process_time = t_2 - t_1
        # process_memory = m_2[0] - m_1[0]
        # return f'Время выполнения: {process_time}, память: {process_memory}'
        return f'Время выполнения: {process_time}'
    return wrapper

# использование форматирования строк вместо конкатенации(внутри цикла)
#  избегать использование глобальных переменных
#  использовать встроенные функции
# варианты, которые рассматривавли на занятии


@my_decorator
def quick_sort(lst):     # Время выполнения: 0.015625
    if len(lst) <= 1:
        return lst
    else:
        q = random.choice(lst)
        s_lst = []
        m_lst = []
        e_lst = []
        for n in lst:
            if n < q:
                s_lst.append(n)
            elif n > q:
                m_lst.append(n)
            else:
                e_lst.append(n)
        return list(quick_sort(s_lst)) + list(e_lst) + list(quick_sort(m_lst))


@my_decorator
def sorted_list(lst):   # Время выполнения: 0.0
    lst.sort()
    return lst


my_lst = [random.randint(-100, 100) for _ in range(10000)]
print(quick_sort(my_lst))
print(sorted_list(my_lst))
