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


from random import randint, choice
from collections import deque
from timeit import timeit


def get_random_item(seq):
    return choice(seq)


def pop_r(seq):
    if type(seq) == list or type(seq) == deque:
        for i in range(len(seq)):
            seq.pop()


def pop_l(seq):
    if type(seq) == deque:
        for i in range(len(seq)):
            seq.popleft()
    elif type(seq) == list:
        for i in range(len(seq)):
            seq.pop(0)


def append_r(seq, n):
    if type(seq) == list:
        for i in range(n):
            seq.append(i)
    elif type(seq) == deque:
        for i in range(n):
            seq.append(i)


def append_l(seq, n):
    if type(seq) == deque:
        for i in range(n):
            seq.appendleft(i)
    elif type(seq) == list:
        for i in range(n):
            seq.insert(0, i)


def rev(seq):
    if type(seq) == list or type(seq) == deque:
        seq.reverse()


#  1000
lst_1000 = [randint(0, 10000000) for n in range(1000)]
dq_1000 = deque([randint(0, 10000000) for n in range(1000)])

#  10000
lst_10000 = [randint(0, 10000000) for n in range(10000)]
dq_10000 = deque([randint(0, 10000000) for n in range(10000)])

#  20000
lst_20000 = [randint(0, 10000000) for n in range(20000)]
dq_20000 = deque([randint(0, 10000000) for n in range(20000)])

num_iter = 1000
num_ins = 50

print('1000 элементов')
print('ДЕК, случайный элемент:')
print(timeit('get_random_item(dq_1000.copy())', number=num_iter, globals=globals()))
print('СПИСОК, случайный элемент:')
print(timeit('get_random_item(lst_1000.copy())', number=num_iter, globals=globals()))

print('ДЕК, вставка справа:')
print(timeit('append_r(dq_1000.copy(), num_ins)', number=num_iter, globals=globals()))
print('СПИСОК, вставка справа:')
print(timeit('append_r(lst_1000.copy(), num_ins)', number=num_iter, globals=globals()))

print('ДЕК, вставка слева:')
print(timeit('append_l(dq_1000.copy(), num_ins)', number=num_iter, globals=globals()))
print('СПИСОК, вставка слева:')
print(timeit('append_l(lst_1000.copy(), num_ins)', number=num_iter, globals=globals()))

print('ДЕК, извлечение справа:')
print(timeit('pop_r(dq_1000.copy())', number=num_iter, globals=globals()))
print('СПИСОК, извлечение справа:')
print(timeit('pop_r(lst_1000.copy())', number=num_iter, globals=globals()))

print('ДЕК, извлечение слева:')
print(timeit('pop_l(dq_1000.copy())', number=num_iter, globals=globals()))
print('СПИСОК, извлечение слева:')
print(timeit('pop_l(lst_1000.copy())', number=num_iter, globals=globals()))

print('ДЕК, разворот:')
print(timeit('rev(dq_1000.copy())', number=num_iter, globals=globals()))
print('СПИСОК, разворот:')
print(timeit('rev(lst_1000.copy())', number=num_iter, globals=globals()))

print(f'\n10000 элементов')
print('ДЕК, случайный элемент:')
print(timeit('get_random_item(dq_10000.copy())', number=num_iter, globals=globals()))
print('СПИСОК, случайный элемент:')
print(timeit('get_random_item(lst_10000.copy())', number=num_iter, globals=globals()))

print('ДЕК, вставка справа:')
print(timeit('append_r(dq_10000.copy(), num_ins)', number=num_iter, globals=globals()))
print('СПИСОК, вставка справа:')
print(timeit('append_r(lst_10000.copy(), num_ins)', number=num_iter, globals=globals()))

print('ДЕК, вставка слева:')
print(timeit('append_l(dq_10000.copy(), num_ins)', number=num_iter, globals=globals()))
print('СПИСОК, вставка слева:')
print(timeit('append_l(lst_10000.copy(), num_ins)', number=num_iter, globals=globals()))

print('ДЕК, извлечение справа:')
print(timeit('pop_r(dq_10000.copy())', number=num_iter, globals=globals()))
print('СПИСОК, извлечение справа:')
print(timeit('pop_r(lst_10000.copy())', number=num_iter, globals=globals()))

print('ДЕК, извлечение слева:')
print(timeit('pop_l(dq_10000.copy())', number=num_iter, globals=globals()))
print('СПИСОК, извлечение слева:')
print(timeit('pop_l(lst_10000.copy())', number=num_iter, globals=globals()))

print('ДЕК, разворот:')
print(timeit('rev(dq_10000.copy())', number=num_iter, globals=globals()))
print('СПИСОК, разворот:')
print(timeit('rev(lst_10000.copy())', number=num_iter, globals=globals()))

print(f'\n20000 элементов')
print('ДЕК, случайный элемент:')
print(timeit('get_random_item(dq_20000.copy())', number=num_iter, globals=globals()))
print('СПИСОК, случайный элемент:')
print(timeit('get_random_item(lst_20000.copy())', number=num_iter, globals=globals()))

print('ДЕК, вставка справа:')
print(timeit('append_r(dq_20000.copy(), num_ins)', number=num_iter, globals=globals()))
print('СПИСОК, вставка справа:')
print(timeit('append_r(lst_20000.copy(), num_ins)', number=num_iter, globals=globals()))

print('ДЕК, вставка слева:')
print(timeit('append_l(dq_20000.copy(), num_ins)', number=num_iter, globals=globals()))
print('СПИСОК, вставка слева:')
print(timeit('append_l(lst_20000.copy(), num_ins)', number=num_iter, globals=globals()))

print('ДЕК, извлечение справа:')
print(timeit('pop_r(dq_20000.copy())', number=num_iter, globals=globals()))
print('СПИСОК, извлечение справа:')
print(timeit('pop_r(lst_20000.copy())', number=num_iter, globals=globals()))

print('ДЕК, извлечение слева:')
print(timeit('pop_l(dq_20000.copy())', number=num_iter, globals=globals()))
print('СПИСОК, извлечение слева:')
print(timeit('pop_l(lst_20000.copy())', number=num_iter, globals=globals()))

print('ДЕК, разворот:')
print(timeit('rev(dq_20000.copy())', number=num_iter, globals=globals()))
print('СПИСОК, разворот:')
print(timeit('rev(lst_20000.copy())', number=num_iter, globals=globals()))

"""
1000 элементов
ДЕК, случайный элемент:
0.00483076000091387
СПИСОК, случайный элемент:
0.0033230799999728333
ДЕК, вставка справа:
0.009726952999699279
СПИСОК, вставка справа:
0.008362421000128961
ДЕК, вставка слева:
0.009516228001302807
СПИСОК, вставка слева:
0.03734532900125487
ДЕК, извлечение справа:
0.08515043800070998
СПИСОК, извлечение справа:
0.07906793700021808
ДЕК, извлечение слева:
0.07499666200055799
СПИСОК, извлечение слева:
0.1808424869996088
ДЕК, разворот:
0.005741028999182163
СПИСОК, разворот:
0.0024333279998245416

10000 элементов
ДЕК, случайный элемент:
0.05282353100119508
СПИСОК, случайный элемент:
0.030626924999523908
ДЕК, вставка справа:
0.05345642899919767
СПИСОК, вставка справа:
0.03433755199876032
ДЕК, вставка слева:
0.05901346300015575
СПИСОК, вставка слева:
0.37573687800068
ДЕК, извлечение справа:
0.7432634099986899
СПИСОК, извлечение справа:
0.8338423900004273
ДЕК, извлечение слева:
0.7591953539995302
СПИСОК, извлечение слева:
10.75368207900101
ДЕК, разворот:
0.07532222400004684
СПИСОК, разворот:
0.033783822000259534

20000 элементов
ДЕК, случайный элемент:
0.12427018800008227
СПИСОК, случайный элемент:
0.05333015199903457
ДЕК, вставка справа:
0.11811009200027911
СПИСОК, вставка справа:
0.06002755699955742
ДЕК, вставка слева:
0.11472977500125126
СПИСОК, вставка слева:
0.6267125760005001
ДЕК, извлечение справа:
1.6355078350006806
СПИСОК, извлечение справа:
1.6456527819991607
ДЕК, извлечение слева:
1.4987270569999964
СПИСОК, извлечение слева:
41.477201398000034
ДЕК, разворот:
0.1281853989985393
СПИСОК, разворот:
0.06680907000009029

sys.version
'3.8.7 (default, Jan 26 2021, 14:08:34) \n[GCC 9.3.0]'

Из результатов замеров видно, что списки в выборе случайного элемента значительно быстрее дека.
reverse у списков тоже быстрее.
Так-же можно заметить, что у списка операции вставки/извлечения слева гораздо медленнее, чем аналогичные справа,
чего не скажешь о деке, в котором 'левые' и 'правые' операции выполняются примерно за одинаковое время.
В целом e у дека операции вставки/извлечения быстрее или примерно рабны аналогичным у списка.
"""
