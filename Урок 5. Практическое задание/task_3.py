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

my_list = [i ** 2 for i in range(1, 100)]
my_list_2 = my_list[:]
deque_list = deque(my_list_2)


def get_element(some_list):
    for i in some_list:
        i += 1


def rotate(some_list, number):
    for i in range(number):
        some_list.insert(0, some_list.pop())


print('Время на перебор элементов и добавления им + 1 без deque:')
print(timeit('get_element(my_list)',
             'from __main__ import get_element, my_list'))
print('Время на перебор элементов и добавления им + 1 с deque:')
print(timeit('get_element(deque_list)',
             'from __main__ import get_element, deque_list'))

print('Время на смещение 5 элементов без deque:')
print(timeit('rotate(my_list, 5)',
             'from __main__ import rotate, my_list'))
print('Время на смещение 5 элементов с deque:')
print(timeit('deque_list.rotate(5)',
             'from __main__ import deque_list'))

print('Время на добавление 100 чисел в начало списка без deque:')
print(timeit('''
for i in range(100):
    my_list.insert(0, i)
''', 'from __main__ import my_list', number=2000))
print('Время на добавление 100 чисел в начало списка с deque:')
print(timeit('''
for i in range(100):
    deque_list.appendleft(i)
''', 'from __main__ import deque_list', number=2000))

print('Время на удаление 100 чисел в начале списка без deque:')
print(timeit('''
for i in range(100):
    my_list.pop(0)
''', 'from __main__ import my_list', number=1500))
print('Время на удаление 100 чисел в начале списка с deque:')
print(timeit('''
for i in range(100):
    deque_list.popleft()
''', 'from __main__ import deque_list', number=1500))

# Время на перебор элементов и добавления им + 1 без deque:
# 3.5831839000000003
# Время на перебор элементов и добавления им + 1 с deque:
# 3.6272144999999996
# Время на смещение 5 элементов без deque:
# 0.9418541000000005
# Время на смещение 5 элементов с deque:
# 0.08567140000000073
# Время на добавление 100 чисел в начало списка без deque:
# 8.4956226
# Время на добавление 100 чисел в начало списка с deque:
# 0.00997249999999994
# Время на удаление 100 чисел в начале списка без deque:
# 5.7363836999999975
# Время на удаление 100 чисел в начале списка с deque:
# 0.006995599999999769
# Операции с deque значительно быстрее
# кроме операций по перебору каждого элемента
