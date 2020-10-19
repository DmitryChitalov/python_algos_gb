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
import cProfile
import timeit

lst = list(range(20))
deq = deque(range(20))
print('Текущий список: ', lst)
print('Текущая очередь: ', deq, '\n')

# добавление в список и очередь

code_to_test = """ 
lst = list(range(20))
lst.append(135) 
"""


code_to_test1 = """ 
deq = deque(range(20))
deq.append(123)
"""

# deq.appendleft(89563)


print('дабавили в список: ', lst)
print('дабавили в очередь: ', deq, '\n')
# print('дабавили в начало очереди: ', deq)

# убирает в список и очередь

code_to_test2 = """ 
lst = list(range(20))
lst.pop()
"""

code_to_test3 = """ 
deq = deque(range(20))
deq.pop()
"""

#deq.popleft()

print('убирает последний элемент из списока: ', lst)
print('убирает последний элемент из очереди: ', deq, '\n')
# print(''убирает последний элемент из начала очереди: ', deq)


# Разворачивает список и очередь
code_to_test4 = """ 
lst = list(range(20))
lst.reverse()
"""

code_to_test5 = """ 
deq = deque(range(20))
deq.reverse()
"""


print('Разворачивает список ', lst)
print('Разворачивает очередь ', deq, '\n')


# производим замеры
print(timeit.timeit(code_to_test, number=100))
print(timeit.timeit(code_to_test1, 'from __main__ import deque', number=100))

print(timeit.timeit(code_to_test2, number=100))
print(timeit.timeit(code_to_test3, 'from __main__ import deque', number=100))

print(timeit.timeit(code_to_test4, number=100))
print(timeit.timeit(code_to_test5, 'from __main__ import deque', number=100))

# результат

# 4.4999999999975615e-06 5.800000000000249e-06 лист быстрее добавляет,
# интересно,что чем больше повторений тем меньше времени необходимо для выполнения метода

# 2.7300000000000935e-05 3.4100000000002184e-05 лист быстрее убирает

# 5.9000000000000025e-05, 4.309999999999731e-05 реверс очередь делает быстрее



