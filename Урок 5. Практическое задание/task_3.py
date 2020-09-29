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
import collections

print("исходный list и deque")
list_test = ['A', 'B', 'C', 'D']
print(list_test)
deque_test = collections.deque(list_test)
print(deque_test)
print()

new_list = ['E', 'F', 'J', 'H']

print('тестируем extend')

def extend_list(input_list_1, input_list_2):
    list_test = input_list_1
    new_list = input_list_2
    list_test.extend(new_list)

print(f'тест extend_list: '
      f'{timeit.timeit("extend_list(list_test, new_list)", setup="from __main__ import extend_list, list_test, new_list", number=1000)}')

def extend_deque(input_deque, input_list_2):
    deque_test = input_deque
    new_list = input_list_2
    deque_test.extend(new_list)

print(f'тест extend_deque: '
      f'{timeit.timeit("extend_deque(deque_test, new_list)", setup="from __main__ import extend_deque, deque_test, new_list", number=1000)}')

print('тестируем pop')

def list_pop(list):
    list_test = list
    list_test.pop()

print(f'тест list_pop: '
      f'{timeit.timeit("list_pop(list_test)", setup="from __main__ import list_pop, list_test", number=1000)}')

def deque_pop(input_deque):
    deque_test = input_deque
    deque_test.pop()

print(f'тест deque_pop: '
      f'{timeit.timeit("deque_pop(deque_test)", setup="from __main__ import deque_pop, deque_test", number=1000)}')


print('тестируем insert')

def list_insert(input_list, position=0):
    list_test = input_list
    list_test.insert(position, new_list)

print(f'тест list_insert: '
      f'{timeit.timeit("list_insert(new_list)", setup="from __main__ import list_insert, new_list", number=1000)}')

def deque_insert(input_deque, position=0):
    deque_test = input_deque
    deque_test.insert(position, new_list)

print(f'тест deque_insert: '
      f'{timeit.timeit("deque_insert(new_list)", setup="from __main__ import deque_insert, new_list", number=1000)}')


'''
тестируем extend
тест extend_list: 0.0005660000000000001
тест extend_deque: 0.0006034000000000001
тестируем pop
тест list_pop: 0.0007871999999999998
тест deque_pop: 0.0003725
тестируем insert
тест list_insert: 0.0011376
тест deque_insert: 0.0018411

Исходя из тестов, deque совсем не показал прироста скорости 
выполнения вышеприведенных операций по сравнению с list.

'''