"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов!.
Сделать их разные реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

# Возьму разные вариации своей программы из Основ Python и на примере работы с библиотечкой itertools и методом count
# сделаю разные замеры памяти используя библиотечку memory_profiler метод profile
# Компьютер:
# 1. Процессор: Intel core i7-8550U 1.8GHz 2.0GHz (8ое поколение)
# 2. Память: 16 Гб
# 3. Разрядность системы: x64
# 4. Версия Python: 3.8

#----Program 1 Scripts with count cycle and memory usage ------------
from memory_profiler import profile
from sys import argv
from itertools import count, cycle, islice


@profile
def itertools_count_func(start_number):

    print('Program "scripts with count cycle"')
    print('itertools.count() c выходом по break:')
    for el in count(int(start_number)):
        if el > 10000:         # выход с break
            break
        else:
            print(el)

print('Program 1 Scripts with count cycle and memory usage')
itertools_count_func(999)

"""

1.Мы видим, что памяти используется немного, всего 16,1 Mib
2."Хороший" инкремент
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    30     16.1 MiB     16.1 MiB           1   @profile
    31                                         def itertools_count_func(start_number):
    32                                         
    33     16.1 MiB      0.0 MiB           1       print('Program "scripts with count cycle"')
    34     16.1 MiB      0.0 MiB           1       print('itertools.count() c выходом по break:')
    35     16.1 MiB      0.0 MiB        9003       for el in count(int(start_number)):
    36     16.1 MiB      0.0 MiB        9003           if el > 10000:         # выход с break
    37     16.1 MiB      0.0 MiB           1               break
    38                                                 else:
    39     16.1 MiB      0.0 MiB        9002               print(el)
    
3. Перепишем скрипт
"""
#----Program 1.2 Scripts with count cycle and memory usage ------------

@profile
def itertools_count_func2(start_number2):
    for el2 in islice(count(int(start_number2)), 10000):
        print(el2)

print('Program 1.2 Scripts with count cycle and memory usage')
print('\nОграничение itertools.count() без break, использование islice:')
itertools_count_func2(999)

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    73     16.1 MiB     16.1 MiB           1   @profile
    74                                         def itertools_count_func2(start_number):
    75     16.1 MiB      0.0 MiB       10001       for el in islice(count(int(start_number)), 10000):
    76     16.1 MiB      0.0 MiB       10000           print(el)
Как мы видим результаты "не слишком" поменялись.
Продолжим наши замеры и перепишем наш скрипт ещё раз.
"""
#----Program 1.3 Scripts with count cycle and memory usage ------------

@profile
def itertools_count_func3(start_number3):
    try:
        for el in count(int(start_number3)):
            if el == 10000:
                return print('Stop count, because find 10000:)')
            print(el)
    except ValueError:
        return print('Imput value is wrong...')
    finally:
        print('End work with itertools.count\n')

print('Program 1.3 Scripts with count cycle and memory usage')
print('\nОграничение itertools.count() без break, использование function:')
itertools_count_func3(999)

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     6     16.1 MiB     16.1 MiB           1   @profile
     7                                         def itertools_count_func3(start_number3):
     8     16.1 MiB      0.0 MiB           1       try:
     9     16.1 MiB      0.0 MiB        9002           for el in count(int(start_number3)):
    10     16.1 MiB      0.0 MiB        9002               if el == 10000:
    11     16.1 MiB      0.0 MiB           2                   return print('Stop count, because find 10000:)')
    12     16.1 MiB      0.0 MiB        9001               print(el)
    13                                             except ValueError:
    14                                                 return print('Imput value is wrong...')
    15                                             finally:
    16     16.1 MiB      0.0 MiB           1           print('End work with itertools.count\n')
Как мы видим результаты "не слишком" поменялись.

Вывод: Можно считать что все три варианта нашей программы имеют право на существование без особых затрат памяти. 
"""
