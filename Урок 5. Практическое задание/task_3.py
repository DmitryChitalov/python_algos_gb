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
import timeit
from collections import deque


int_list = list(range(100))
int_deque = deque(range(100))

print(f'pop_end_list - {timeit.timeit(lambda: int_list.pop(), number=100)}')
print(f'pop_end_deque - {timeit.timeit(lambda: int_deque.pop(), number=100)}')
print(f'append_end_list - {timeit.timeit(lambda: int_list.append(11), number=100)}')
print(f'append_end_deque - {timeit.timeit(lambda: int_deque.append(11), number=100)}')
print(f'del_first_list - {timeit.timeit(lambda: int_list.pop(0), number=100)}')
print(f'del_first_deque - {timeit.timeit(lambda: int_deque.popleft(), number=100)}')
print(f'reverse_list - {timeit.timeit(lambda: int_list.reverse(), number=100)}')
print(f'reverse_deque - {timeit.timeit(lambda: int_deque.reverse(), number=100)}')
print(f'append_begin_list - {timeit.timeit(lambda: int_list.insert(0, 11), number=100)}')
print(f'append_begin_deque - {timeit.timeit(lambda: int_deque.appendleft(11), number=100)}')

'''
По итогам замеров, можно сделать вывод, что операции доавления/удаления элементов в начало или в конец выполняются 
быстрее с использованием структуры deque 
pop_end_list - 2.9100000000004123e-05
pop_end_deque - 1.7000000000003124e-05
append_begin_list - 3.2799999999999496e-05
append_begin_deque - 1.7000000000003124e-05
append_end_list - 2.1000000000000185e-05
append_end_deque - 2.0199999999997997e-05
del_first_list - 3.0500000000002747e-05
del_first_deque - 1.6799999999997373e-05
reverse_list - 1.6900000000000248e-05
reverse_deque - 1.659999999999856e-05
'''
