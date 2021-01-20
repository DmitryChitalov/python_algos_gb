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
from time import perf_counter_ns
from collections import deque

if __name__ == '__main__':
    t_ns = perf_counter_ns()
    my_lst = [i for i in range(1000000)]
    print(f'Заполнение списка: {perf_counter_ns() - t_ns}нсек')
    t_ns = perf_counter_ns()
    my_deque = deque(i for i in range(1000000))
    print(f'Заполнение deque:  {perf_counter_ns() - t_ns}нсек')
    t_ns = perf_counter_ns()
    my_lst.append(34)
    print(f'Добавление одного элемента в конец списка: {perf_counter_ns() - t_ns}нсек')
    t_ns = perf_counter_ns()
    my_deque.append(34)
    print(f'Добавление одного элемента в конец deque:  {perf_counter_ns() - t_ns}нсек')
    t_ns = perf_counter_ns()
    for i in range(10000):
        my_lst.append(i)
    print(f'Добавление 10000 элементов в конец списка: {perf_counter_ns() - t_ns}нсек')
    t_ns = perf_counter_ns()
    for i in range(10000):
        my_deque.append(i)
    print(f'Добавление 10000 элементов в конец deque:  {perf_counter_ns() - t_ns}нсек')
    t_ns = perf_counter_ns()
    for i in range(10000):
        my_lst.insert(0, i)
    print(f'Добавление 10000 элементов в начало списка: {perf_counter_ns() - t_ns}нсек')
    t_ns = perf_counter_ns()
    for i in range(10000):
        my_deque.appendleft(i)
    print(f'Добавление 10000 элементов в начало deque:  {perf_counter_ns() - t_ns}нсек')

"""
скорость работы списка и deque сопоставимы в общих операциях (append),
однако deque показывает значительное увеличение скорости работы на операциях присущих работе очереди (appendleft)
например appendleft при добавлении в начало 10000 элементов работает на два порядка быстрее метода списка insert(0, i) 
"""