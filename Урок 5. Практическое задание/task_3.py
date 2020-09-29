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


def list_deque(val):
    deque_list = deque(val)
    deque_list.appendleft('Test_')
    deque_list.appendleft('_Test')
    deque_list.pop()


def list_test(val):
    test_list = list(val)
    test_list.insert(0, 'Test_')
    test_list.append('_Test')
    test_list.pop()


values = 'HowAreYouToday?'
print(values)
print(f'Deque : {timeit("list_deque(values)", setup="from __main__ import list_deque, values", number=1000000)}')
print(f'List : {timeit("list_test(values)", setup="from __main__ import list_test, values", number=1000000)}')

"""
Замеры почти одинаковы, но deque выигравает, когда нужно добавить или удалить данные из списка.
Это становить более заметно при увеличении кодичества повторений кода.
В случаже создания списка list отрабатывает быстрее.
"""