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

STR_CODE_1 = '''
l = [] 
for i in range(1000): 
    l.append(i)
'''
STR_CODE_2 = '''
from collections import deque
j = deque([])
for i in range(1000): 
    j.append(i)
'''
STR_CODE_3 = '''
l = [] 
for i in range(1000): 
    l.insert(0, i)
'''
STR_CODE_4 = '''
from collections import deque
j = deque([])
for i in range(1000): 
    j.appendleft(i)
'''
STR_CODE_5 = '''
import string
b = list(string.printable)
while b:
    b.pop(0)
'''
STR_CODE_6 = '''
import string
from collections import deque
a = deque(string.printable)
while a:
    a.popleft()
'''
STR_CODE_7 = '''
import string
c = list(string.printable * 3)
c.insert(22, '*')
'''
STR_CODE_8 = '''
import string
from collections import deque
d = deque(string.printable * 3)
d.insert(22, '*')
'''

print(timeit.timeit(STR_CODE_1, number=100000))  #list: Заполнение списка - добавление в конец
print(timeit.timeit(STR_CODE_2, number=100000))  #Deque: Заполнение списка - добавление в конец быстрее, чем в List
print(timeit.timeit(STR_CODE_3, number=100000))  #list: Заполнение списка - добавление в начало
print(timeit.timeit(STR_CODE_4, number=100000))  #Deque: Заполнение списка - добавление в начало значительно быстрее, чем в List
print(timeit.timeit(STR_CODE_5, number=100000))  #list: Удаление элементов с одного конца
print(timeit.timeit(STR_CODE_6, number=100000))  #Deque: Удаление элементов с одного конца быстрее, чем в List
print(timeit.timeit(STR_CODE_7, number=100000))  #list: Вставка элемента в середину списка быстрее, чем в Deque
print(timeit.timeit(STR_CODE_8, number=100000))  ##Deque: Вставка элемента в середину списка