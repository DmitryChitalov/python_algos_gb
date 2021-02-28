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
import random
from timeit import timeit

def create_list(n=1000): 
    """
    Создаем список на 1000 элементов

    """
    return list(range(1,n+1))

def create_deque(n =1000):
    """
    Создаем очередь из 1000 элементов

    """
    return deque(range(1,n+1))


lst = create_list()
dq = create_deque()

def append_list(lst, n=1000):
    """
    допишем еще 1000 элементов в существующий список

    """
    for _ in range(n):
        lst.append(random.randint(10,99))

    return lst

def append_deque(dq, n=1000):
    """
    допишем еще 1000 элементов в существующаю очередь

    """
    for _ in range(n):
        dq.append(random.randint(10,99))

    return dq

def insert_lst(lst, n =1000):
    """
    Вставим 1000 элементов в начало списка

    """
    for _ in range(n):
        lst.insert(0, random.randint(10,99))

    return lst

def insert_deque(dq, n =1000):
    """
    Вставим 1000 элементов в начало очереди

    """
    for _ in range(n):
        dq.appendleft(random.randint(10,99))

    return dq

def pop_lst(lst, n =500):
    """
    выбрасываем 500 левых элементов из списка

    """
    for _ in range(n):
        lst.pop(0)

    return lst

def pop_deque(dq, n =500):
    """
    выбрасываем 500  левых элементов из очереди

    """
    for _ in range(n):
        dq.popleft()

    return dq    


print('1. Создание списка ',
      timeit('create_list()', 'from __main__ import create_list', number= 1000)
)

print('2. Создание очереди ',
      timeit('create_deque()', 'from __main__ import create_deque', number= 1000)
)


print('3. Добавление в список ',
      timeit('append_list(lst)', 'from __main__ import append_list, lst', number= 1000)
)

print('4. Добавление в очередь ',
      timeit('append_deque(dq)', 'from __main__ import append_deque, dq', number= 1000)
)


print('5. Вставка элементов в список ',
      timeit('insert_lst(lst)', 'from __main__ import insert_lst, lst', number= 100)
)

print('6. Вставка элементов в очередь ',
      timeit('insert_deque(dq)', 'from __main__ import insert_deque, dq', number= 100)
)


print('7. Извлечение элементов из списка ',
      timeit('pop_lst(lst)', 'from __main__ import pop_lst, lst', number= 100)
)

print('8. Извлечение элементов из очереди ',
      timeit('pop_deque(dq)', 'from __main__ import pop_deque, dq', number= 100)
)

"""
 python3 'Урок 5. Практическое задание/task_3.py'
1. Создание списка  0.0414106839998567
2. Создание очереди  0.023753550999572326
3. Добавление в список  3.4000830989998576
4. Добавление в очередь  3.4026173330003076
5. Вставка элементов в список  107.96867230499993
6. Вставка элементов в очередь  0.31481895799970516
7. Извлечение элементов из списка  46.62046087500039
8. Извлечение элементов из очереди  0.0031483709999520215

Действительно очередь несколько превосходит список в операциях добавления и извлечения элементов с левой стороны.
Создание структур происходит за прмерно сопоставимое время - пункты 1 и 2 (в представленном выводе разница в пользу очереди).
Добавление элементов в конце очереди и списка (в правую часть) также проходит за одинаковое время.
Очевидное преимущество очереди на операция добавленя/извлечения в левую часть. Вероятно в очереди оптимизированы операции переиндексации элементов после вставки/извлечения элемента. При этом разница составляет 50-100 раз, что будет заметно на больших объемах данных.

"""