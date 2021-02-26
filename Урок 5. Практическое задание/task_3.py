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

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""

from collections import deque
from timeit import timeit


class Test1:
    list_1: list
    deque_1: deque
    elements_count: int

    def initialize_test_input(self, elements_count: int):
        self.elements_count = elements_count
        self.list_1 = list(range(self.elements_count))
        self.deque_1 = deque(self.list_1)

    def list_append(self):
        self.list_1.append(1)

    def deque_append(self):
        self.deque_1.append(1)

    def list_insert_left(self):
        self.list_1.insert(0, 1)

    def deque_insert_left(self):
        self.deque_1.appendleft(1)

    def list_extend(self):
        self.list_1.extend(list(range(20)))

    def deque_extend(self):
        self.deque_1.extend(list(range(20)))

    def list_extend_left(self):
        for el in list(range(20)):
            self.list_1.insert(0, el)

    def deque_extend_left(self):
        self.deque_1.extendleft(list(range(20)))

    def list_pop(self):
        el = self.list_1.pop()

    def deque_pop(self):
        el = self.deque_1.pop()

    def list_popleft(self):
        el = self.list_1.pop(0)

    def deque_popleft(self):
        el = self.deque_1.popleft()

    def list_reverse(self):
        result = self.list_1.reverse()

    def deque_reverse(self):
        result = self.deque_1.reverse()

    def time_test(self, func_name: str, times: int):
        self.initialize_test_input(times)
        func_name_1 = f"self.{func_name}()"
        print(func_name_1, timeit(func_name_1, number=times, globals=locals()))


test1 = Test1()
for func_name in ['list_append', 'deque_append', 'list_insert_left', 'deque_insert_left', 'list_extend',
                  'deque_extend', 'list_extend_left', 'deque_extend_left', 'list_pop', 'deque_pop', 'list_popleft',
                  'deque_popleft', 'list_reverse', 'deque_reverse']:
    test1.time_test(func_name, 10000)

'''
self.list_append()          0.004230400000000009
self.deque_append()         0.0045752999999999905

self.list_insert_left()     0.15227200000000002
self.deque_insert_left()    0.0026702999999999866 - ЗАМЕТНО БЫСТРЕЕ

self.list_extend()          0.014710100000000004
self.deque_extend()         0.013276800000000033

self.list_extend_left()     19.6150791
self.deque_extend_left()    0.011968500000001825 - ЗАМЕТНО БЫСТРЕЕ

self.list_pop()             0.0027250000000016428
self.deque_pop()            0.002873199999999798

self.list_popleft()         0.023959000000001396
self.deque_popleft()        0.0025615999999999417 - ЗАМЕТНО БЫСТРЕЕ

self.list_reverse()         0.06519750000000002 - ЗАМЕТНО БЫСТРЕЕ
self.deque_reverse()        0.13360700000000136 

Выше мы можем видеть операции и занимаемое время на 10000 повторах, 
выводы следуют из времени выполнения схожих операций.
Заметные преимущества Deque на операциях: insert_left, extend_left, popleft
Явные недостатки Deque: более медленное выполнение reverse
'''
