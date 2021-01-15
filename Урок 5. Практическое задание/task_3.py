"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""
from collections import deque
from timeit import timeit
import cProfile

"""
Создаем простой список и двухстороннею очередь из 1000000 элементов.
Функция по созданию списка нужна чтобы замерить скорость.
"""


def make_list():
    my_lst = []
    for i in range(1000000):
        my_lst.append(i)
    return my_lst


simple_lst = make_list()
deque_lst = deque(make_list())
# simple_lst = [i for i in range(1000000)]
# # print(timeit('[i for i in range(100)]'))
# deque_lst = deque([i for i in range(1000000)])
# print(timeit('deque([i for i in range(100)]'))


""""
Убираем из списка и дека по 300000 елементов слево и справа, замеряем время
"""


def del_right_deq(my_lst):
    for i in range(300000):
        my_lst.pop()
    return my_lst


def del_right_simp(my_lst):
    for i in range(300000):
        my_lst.pop()
    return my_lst


# del_right_simple = """
# for i in range(30):
#     simple_lst.pop()
# """
"""
Не понимаю почему не делаются замеры timeit. Пишет что рор не работает с пустыми листами, но функции 100% отрабатывают.
Тоже самое при создании списков. Выражение для простого списка считает время выполнения, а для деки ошибка. 
В дальнейшем буду использовать cProfile.
"""

# print('Время удаления 3000 элем. слево в deque_lst',
#       timeit('del_right_deq(deque_lst)', setup='from __main__ import del_right_deq, deque_lst', number=10000))
# print('Время удаления 3000 элем. слево в simple_lst',
#       timeit('del_right_simp(simple_lst)', setup='from __main__ import del_right_simp, simple_lst', number=10000))
# print(timeit(del_right_simple, setup='from __main__ import simple_lst', number=10000))


def del_left_deq(my_lst):
    for i in range(30000):
        my_lst.popleft()
    return my_lst


def del_left_simp(my_lst):
    for i in range(30000):
        my_lst.pop(i)
    return my_lst


"""
Далее будут 4 функции, добавление в начало списка и взятие элементов.
"""


def append_left_deq(my_lst):
    for i in range(30000):
        my_lst.appendleft(i)
    return my_lst


def append_left_simp(my_lst):
    for i in range(30000):
        my_lst.insert(i, i)
    return my_lst


def take_index_deq(my_lst):
    my_lst_2 = []
    for i in range(299000, 300000):
        my_lst_2.append(my_lst.index(i))
    return my_lst_2


def take_index_simp(my_lst):
    my_lst_2 = []
    for i in range(299000, 300000):
        my_lst_2.append(my_lst.index(i))
    return my_lst_2


def main():
    make_list()
    deque(make_list())
    del_right_deq(deque_lst)
    del_right_simp(simple_lst)
    del_left_deq(deque_lst)
    del_left_simp(simple_lst)
    append_left_deq(deque_lst)
    append_left_simp(simple_lst)
    take_index_deq(deque_lst)
    take_index_simp(simple_lst)


cProfile.run('main()')
"""
Выводы: если надо удалить или добавить элемент в конец списка, простой список и дек отрабатывают одинаково.
Если надо удалить или добавить элемент в начало списка, дек в разы быстрее. Взятие по индексу примерно одинаковое.
Удаление по индексу в деке не возможно.
Следовательно, если задача связана с деком, очередью, стеком deque лучший выбор, в остальном лучше простой список.
2724014 function calls in 25.138 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   25.138   25.138 <string>:1(<module>)
        1    0.001    0.001    3.358    3.358 task_3.py:101(take_index_deq)
        1    0.001    0.001    3.599    3.599 task_3.py:108(take_index_simp)
        1    0.048    0.048   25.138   25.138 task_3.py:115(main)
        2    0.292    0.146    0.452    0.226 task_3.py:23(make_list)
        1    0.041    0.041    0.063    0.063 task_3.py:43(del_right_deq)
        1    0.046    0.046    0.070    0.070 task_3.py:49(del_right_simp)
        1    0.004    0.004    0.007    0.007 task_3.py:72(del_left_deq)
        1    0.014    0.014    5.924    5.924 task_3.py:78(del_left_simp)
        1    0.004    0.004    0.007    0.007 task_3.py:89(append_left_deq)
        1    0.014    0.014   11.611   11.611 task_3.py:95(append_left_simp)
        1    0.000    0.000   25.138   25.138 {built-in method builtins.exec}
  2002000    0.161    0.000    0.161    0.000 {method 'append' of 'list' objects}
    30000    0.002    0.000    0.002    0.000 {method 'appendleft' of 'collections.deque' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1000    3.356    0.003    3.356    0.003 {method 'index' of 'collections.deque' objects}
     1000    3.597    0.004    3.597    0.004 {method 'index' of 'list' objects}
    30000   11.597    0.000   11.597    0.000 {method 'insert' of 'list' objects}
   300000    0.022    0.000    0.022    0.000 {method 'pop' of 'collections.deque' objects}
   330000    5.935    0.000    5.935    0.000 {method 'pop' of 'list' objects}
    30000    0.002    0.000    0.002    0.000 {method 'popleft' of 'collections.deque' objects}
"""