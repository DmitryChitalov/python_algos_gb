"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

from random import randint
from numpy import array
import memory_profiler
from pympler import asizeof
from memory_profiler import profile
from recordclass import recordclass
import sys

"""
Блок 1  yield vs return

Здесь мы меняем return на yield, делая ленивые вычисления
return - Выполнение заняло 0.5703125 Mib, меньше 1 мб . func_1 2044448 байта озу, т.е 2 мегабайта через asizeof
yield - Выполнение заняло 0.00390625 Mib . func_2 4000528 байта озу, т.е 4 мегабайта через asizeof

Yield действительно занимает меньше ОЗУ через @profile, но больше через asizeof

Декорированные функции надо запускать по очереди, иначе вторая функция не показывает,сколько памяти потребляет
"""


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff

    return wrapper


@decor
def func_1(nums):
    new_arr = [nums[i] for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


mygen, mem_diff = func_1(list(range(100000)))
print(f"Выполнение заняло {mem_diff} Mib")
print('func_1', asizeof.asizeof(func_1(list(range(100000)))))


@decor
def func_2(nums):
    new_arr = [nums[i] for i in range(len(nums)) if nums[i] % 2 == 0]
    yield new_arr


mygen2, mem_diff = func_2(list(range(100000)))
print(f"Выполнение заняло {mem_diff} Mib")
print('func_2', asizeof.asizeof(func_2(list(range(100000)))))

print()

print('Блок 2____________________________________________________')

"""
Блок 2  - numpy vs list

В методах оптимизации памяти сказано - используйте биб-ку numpy, она потребляет меньше памяти.
lst - 1.5 MiB
numpy.array - 0.8 MiB
Так и есть. К тому же она еще и меньше места занимает при испл. asizeof:
lst - 1206288 байт
numpy.array - 200120 байт ( в 6 раз меньше)

"""


@profile
def lst():
    lst_obj = [randint(-100, 100) for _ in range(50000)]
    print('lst_obj list', asizeof.asizeof(lst_obj))
    return lst_obj


@profile
def numparray():
    lst_obj = array([randint(-100, 100) for _ in range(50000)])
    print('lst_obj numpy array', asizeof.asizeof(lst_obj))
    return lst_obj


lst()
numparray()

print('Блок 3____________________________________________________')
"""
Блок 3  - recordclass vs list и другие
Идея была в том, чтобы использовать менее затратные по памяти структуры данных.
В рез-те теста получилось, что recordclass на маленьких числах занимает больше всего памяти, при подсчете
через asizeof.

asizeof:
lst_ob 216 байт
tupl 160 байт
dct_ob 496 байт
set_ob 312 байт
record 768 байт

getsizeof:
Объём занимаемой объектом list памяти: 120 байт(а)
Объём занимаемой объектом tupl памяти: 64 байт(а)
Объём занимаемой объектом dict памяти: 232 байт(а)
Объём занимаемой объектом set памяти: 216 байт(а)
Объём занимаемой объектом recordclass памяти: 48 байт(а)

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   110     31.2 MiB     31.2 MiB           1   @profile
   111                                         def lst():
   112     31.2 MiB      0.0 MiB           1       lst_ob = [1, 2, 3]
   113     31.2 MiB      0.0 MiB           1       tupl = (1, 2, 3,)
   114     31.2 MiB      0.0 MiB           1       dct_ob = {'x': 1, 'y': 2, 'z': 3}
   115     31.2 MiB      0.0 MiB           1       set_ob = {1,2,3}
   116     31.2 MiB      0.0 MiB           1       var_1 = recordclass('var_1', ('x', 'y', 'z'))
   117     31.2 MiB      0.0 MiB           1       record = var_1(x=1, y=2, z=3)
   118     31.2 MiB      0.0 MiB           1       print('lst_ob',asizeof.asizeof(lst_ob))
   119     31.2 MiB      0.0 MiB           1       print('tupl',asizeof.asizeof(tupl))
   120     31.2 MiB      0.0 MiB           1       print('dct_ob',asizeof.asizeof(dct_ob))
   121     31.2 MiB      0.0 MiB           1       print('set_ob',asizeof.asizeof(set_ob))
   122     31.2 MiB      0.0 MiB           1       print('record',asizeof.asizeof(record))
   123     31.2 MiB      0.0 MiB           1       print(f'Объём занимаемой объектом list памяти: {sys.getsizeof(lst_ob)} байт(а)')
   124     31.2 MiB      0.0 MiB           1       print(f'Объём занимаемой объектом tupl памяти: {sys.getsizeof(tupl)} байт(а)')
   125     31.2 MiB      0.0 MiB           1       print(f'Объём занимаемой объектом dict памяти: {sys.getsizeof(dct_ob)} байт(а)')
   126     31.2 MiB      0.0 MiB           1       print(f'Объём занимаемой объектом set памяти: {sys.getsizeof(set_ob)} байт(а)')
   127     31.2 MiB      0.0 MiB           1       print(f'Объём занимаемой объектом recordclass памяти: {sys.getsizeof(record)} байт(а)')

Здесь слишком маленькие массивы, чтобы функция их нормально отобразила, поэтому я в Блоке 4 делаем большие значения.
По PEP 8 я выхожу за границы, но не знаю, как показать эту информацию не выходя за границы.
"""


@profile
def lst():
    lst_ob = [1, 2, 3]
    tupl = (1, 2, 3,)
    dct_ob = {'x': 1, 'y': 2, 'z': 3}
    set_ob = {1, 2, 3}
    var_1 = recordclass('var_1', ('x', 'y', 'z'))
    record = var_1(x=1, y=2, z=3)
    print('lst_ob', asizeof.asizeof(lst_ob))
    print('tupl', asizeof.asizeof(tupl))
    print('dct_ob', asizeof.asizeof(dct_ob))
    print('set_ob', asizeof.asizeof(set_ob))
    print('record', asizeof.asizeof(record))
    print(f'Объём занимаемой объектом list памяти: {sys.getsizeof(lst_ob)} байт(а)')
    print(f'Объём занимаемой объектом tupl памяти: {sys.getsizeof(tupl)} байт(а)')
    print(f'Объём занимаемой объектом dict памяти: {sys.getsizeof(dct_ob)} байт(а)')
    print(f'Объём занимаемой объектом set памяти: {sys.getsizeof(set_ob)} байт(а)')
    print(f'Объём занимаемой объектом recordclass памяти: {sys.getsizeof(record)} байт(а)')


lst()

print('Блок 4____________________________________________________')

"""
Блок 4 - переназначаем ссылки, удаляем ссылки на объект, смотрим сколько MiB занимает структура данных
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   136     31.3 MiB     31.3 MiB           1   @profile
   137                                         def funct(max_value):
   138     33.5 MiB      2.2 MiB      100001       gen_lst = [i ** 2 for i in range(1, max_value) if i % 2 == 0]
   139     33.5 MiB      0.0 MiB           1       gen_tupl = (i ** 2 for i in range(1, max_value) if i % 2 == 0)
   140     36.8 MiB      3.3 MiB      100001       gen_set = {i ** 2 for i in range(1, max_value) if i % 2 == 0}
   141     42.5 MiB      5.8 MiB      100001       gen_dict = {i: i ** 2 for i in range(1, max_value) if i % 2 == 0}
   142     41.0 MiB     -1.6 MiB           1       gen_lst= 0
   143     37.7 MiB     -3.3 MiB           1       del gen_set
   144     37.7 MiB      0.0 MiB           1       return gen_lst, gen_tupl, gen_dict

Не понятно почему gen_tupl не занимает место в памяти. Или он занимает настолько малое место, что значение не показывает
В остально мы видим, что самые тяжелые по убыванию это:
1. Словарь
2. Множество
3. Список

Далее мы переназначаем ссылку gen_lst на значение 0
Удаляем из памяти ссылку и объект gen_set
"""


@profile
def funct(max_value):
    gen_lst = [i ** 2 for i in range(1, max_value) if i % 2 == 0]
    gen_tupl = (i ** 2 for i in range(1, max_value) if i % 2 == 0)
    gen_set = {i ** 2 for i in range(1, max_value) if i % 2 == 0}
    gen_dict = {i: i ** 2 for i in range(1, max_value) if i % 2 == 0}
    gen_lst = 0
    del gen_set
    return gen_lst, gen_tupl, gen_dict


funct(99999)
