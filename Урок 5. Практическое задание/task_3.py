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
from collections import defaultdict
from timeit import timeit

res = defaultdict(list)
# Операции с деком.
dq = deque([i for i in range(1000)])
lst = [i for i in range(10)]

stmts = ('append', 'appendleft', 'index', 'remove')
for stmt in stmts:
    res[f'{stmt}'].append(
        timeit(f"dq.{stmt}(555)",
               setup='from __main__ import dq', number=10000))
stmts = ('count', 'pop', 'popleft', 'rotate', 'reverse', 'copy')
for stmt in stmts:
    res[f'{stmt}'].append(
        timeit(f"dq.{stmt}", setup='from __main__ import dq', number=10000))
stmts = ('extend', 'extendleft')
for stmt in stmts:
    res[f'{stmt}'].append(
        timeit(f"dq.{stmt}({lst})", setup='from __main__ import dq, lst',
               number=1))
res['insert'].append(timeit(f"dq.insert(20, 555)",
                            setup='from __main__ import dq', number=10000))
res['clear'].append(timeit(f"dq.clear",
                           setup='from __main__ import dq', number=10000))

# Операции со списком.
lst = [i for i in range(1000)]
lst_2 = [i for i in range(10)]

stmts = ('append', 'index', 'remove')
for stmt in stmts:
    res[f'{stmt}'].append(
        timeit(f"lst.{stmt}(555)",
               setup='from __main__ import lst', number=10000))
stmts = ('count', 'pop', 'reverse', 'copy')
for stmt in stmts:
    res[f'{stmt}'].append(
        timeit(f"lst.{stmt}", setup='from __main__ import lst', number=10000))
res['extend'].append(timeit(f""
f"lst.extend(lst_2)", setup='from __main__ import lst, lst_2', number=10000))
res['insert'].append(timeit(f"lst.insert(20, 555)",
                            setup = 'from __main__ import lst', number=10000))
res['clear'].append(timeit(f"lst.clear",
                           setup='from __main__ import lst', number=10000))

# Выводим результаты.
for k,v in res.items():
    print(f'Операция {k}:')
    if len(v) == 2:
        print(f'дек: {v[0]:<20f}список: {v[1]:<20f}')
    else:
        print(f'дек: {v[0]:<20f}список: нет аналогичной операции')

"""
Выводы:
- структура "дек" в целом представляет из себя оптимизированный список;
- операции добавления, поиска, вставки элементов и расширения деков
  занимают гораздо меньше времени, чем аналогичные у списков;
- операции удаления: remove быстрее в деках, pop быстрее в списках;
- операции копирования, разворота и очистки деков медленее, чем аналоги
  у списков.
Можно было бы реализовать алгоритмы для списков, повторяющие действия
методов appendleft, popleft, rotate и extendleft. Но вполне очевидно,
что они были бы как минимум не быстрее операций с деками.
Таким образом деки предпочтительнее использовать в случаях, когда
необходима активная работа по добавлению/удалению/поиску элементов, а
списки - когда необходима работа со всей структурой в целом.
"""