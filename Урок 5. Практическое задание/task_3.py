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
# Создаем лист
l_list = ['Nornikel','VTB','GPB','SBERB','ROGA I KOPYTA']
# Создаем deque с таким же набором данных как и в l_list
l_deque = deque(l_list)
# Создадим такие же объекты для 2 теста
l_list2 = ['Nornikel','VTB','GPB','SBERB','ROGA I KOPYTA']
l_deque2 = deque(l_list2)
# Первая операция - Добавление элемента в начало
# в list
def addelem_list ():
    l_list.insert(len(l_list), 'ROSBANK') # O(1)
# в Deque
def addelem_deq ():
    l_deque.appendleft('ROSBANK')        # O(1)

#Вторая операция - Добавление элемента в середину
# в list
def addelem_list2():
    # Определим середину.
    l_avg = int(len(l_list2)/2)
    # И вставим в середину.
    l_list2.insert(l_avg, 'VEB-RF')
# в deque
def addelem_deq2():
    # Определим середину
    l_avg_d = len(l_deque2)
    l_deque2.insert(l_avg_d,'VEB_RF')

print("------------------Первый тест--------------------")
print(len(l_list))
print(len(l_deque))
addelem_list()
addelem_deq()
print('addelem_list',timeit(f'addelem_list()',globals=globals()))
print('addelem_deq',timeit(f'addelem_deq()',globals=globals()))
print(len(l_list))
print(len(l_deque))
print("------------------Конец первого теста--------------------")
# Вывод: как на практике так и в документации, при одинаковой операции (Добавление элемента в начало списка) метод из deque
# показывает себя быстрее, на кокнкретном примере 0.20 против 0.12 При этом сложность алгоритмов - одинаковая.
print("------------------Второй тест--------------------")
print(len(l_list2))
print(len(l_deque2))
addelem_list2()
addelem_deq2()
print('addelem_list2', timeit(f'addelem_list2()', globals = globals()))
print('addelem_deq2', timeit(f'addelem_deq2()', globals = globals()))
print(len(l_list2))
print(len(l_deque2))
print("------------------Конец второго теста--------------------")
# Вывод: как на практике так и в документации, вставка с помощью метода insert в deque работает очень долго, по сравнению с вставкой в list.
