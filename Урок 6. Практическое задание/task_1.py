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

from memory_profiler import profile
from numpy import mean

@profile
def aver_1():
    my_list_sum = 0
    my_list = [el for el in range(100000)]
    for el in my_list:
        my_list_sum += el
    aver = my_list_sum / len(my_list)
    return aver


@profile
def aver_2():
    my_list = [el for el in range(100000)]
    aver = mean(my_list)
    return aver


"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     4     39.4 MiB     39.4 MiB           1   @profile
     5                                         def aver_1():
     6     39.4 MiB      0.0 MiB           1       my_list_sum = 0
     7     41.7 MiB  -1878.5 MiB      100003       my_list = [el for el in range(100000)]
     8     41.7 MiB      0.0 MiB      100001       for el in my_list:
     9     41.7 MiB      0.0 MiB      100000           my_list_sum += el
    10     41.7 MiB      0.0 MiB           1       aver = my_list_sum / len(my_list)
    11     41.7 MiB      0.0 MiB           1       return aver
***************************************************************************************
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    14     39.7 MiB     39.7 MiB           1   @profile
    15                                         def aver_2():
    16     41.7 MiB      2.0 MiB      100003       my_list = [el for el in range(100000)]
    17     41.4 MiB     -0.3 MiB           1       aver = mean(my_list)
    18     41.4 MiB      0.0 MiB           1       return aver


Обе программы выполняют одну и ту же задачу -- поиск среднего значения чисел в списке.
Я хотел увидеть разницу в использовании функции модуля numpy и ручным подсчетом.
На первую программу выделяется 39.4 MiB памяти. При создании списка указано -1878.5 MiB,
хотя объем памяти не уменьшается, а увеличивается.
На вторую программу выделяется 39,7 MiB памяти, на создание списка 2 MiB, использование 
функции mean уменьшило потребление на 0.3 MiB. 
При работе с маленькими списками на 100 элементов разницы в потреблении памяти практически нет.
"""

@profile
def func_2():
    s = """Gur Mra bs Clguba, ol Gvz Crgref

Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyrk.
Pbzcyrk vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcnefr vf orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orngf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""
    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i + c)] = chr((i + 13) % 26 + c)
    print("".join([d.get(c, c) for c in s]))


"""
Filename: C:/Users/79215/PycharmProjects/untitled/test.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    48     39.8 MiB     39.8 MiB           1   @profile
    49                                         def func_2():
    50     39.8 MiB      0.0 MiB           1       s = """"""
    51     39.8 MiB      0.0 MiB           1       d = {}
    52     39.8 MiB      0.0 MiB           3       for c in (65, 97):
    53     39.8 MiB      0.0 MiB          54           for i in range(26):
    54     39.8 MiB      0.0 MiB          52               d[chr(i + c)] = chr((i + 13) % 26 + c)
    55     39.8 MiB      0.0 MiB          15       print("".join([d.get(c, c) for c in s]))
    
Для запуска программы выделено 39.8 MiB памяти. На выполнение всех действий дополнительно память не выделялась
"""
