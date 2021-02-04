"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов
Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from memory_profiler import profile

@profile
def my_func():
   a = [1] * (10 ** 6)
   b = [2] * (2 * 10 ** 7)
   #del a
   #del b
   return None

@profile
def my_func_optimized():
   a = [1] * (10 ** 6)
   b = [2] * (2 * 10 ** 7)
   del a
   del b
   return None

#print('my_func()')
#my_func()
#print('my_func_optimized()')
#my_func_optimized()

"""
my_func()
Filename: D:/geekbrains hw/Algorythms/Урок 6. Практическое задание/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    26     15.7 MiB     15.7 MiB           1   @profile
    27                                         def my_func():
    28     19.5 MiB      3.8 MiB           1      a = [1] * (10 ** 6)
    29     95.8 MiB     76.3 MiB           1      b = [2] * (2 * 10 ** 7)
    30                                            #del a
    31                                            #del b
    32     95.8 MiB      0.0 MiB           1      return None


my_func_optimized()
Filename: D:/geekbrains hw/Algorythms/Урок 6. Практическое задание/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    34     15.7 MiB     15.7 MiB           1   @profile
    35                                         def my_func_optimized():
    36     19.5 MiB      3.8 MiB           1      a = [1] * (10 ** 6)
    37     95.8 MiB     76.3 MiB           1      b = [2] * (2 * 10 ** 7)
    38     92.0 MiB     -3.8 MiB           1      del a
    39     15.7 MiB    -76.3 MiB           1      del b
    40     15.7 MiB      0.0 MiB           1      return None
    
После реализации первой функции видно, что было использовано большое количество информации в переменных,
 которые по итогу не использовались в конечном результате, поэтому было принято решение воспрользоваться 
 функцией удаления переменных, что значительно уменьшило количество информации к концу реализации функции.
"""

@profile
def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n

@profile
def erato(n):
    i = 2
    last_elem = n * 10
    all_num = [z for z in range(last_elem)]
    all_num[1] = 0
    while i < last_elem:
        if all_num[i] != 0:
            check = i * 2
            while check < last_elem:
                all_num[check] = 0
                check = check + i
        i = i + 1
    return [x for x in all_num if x != 0][n - 1]


#print('Simple')
#simple(200)
#print('Eratosfen mode')
#erato(200)

"""
Simple
Filename: D:/geekbrains hw/Algorythms/Урок 6. Практическое задание/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    80     15.7 MiB     15.7 MiB           1   @profile
    81                                         def simple(i):
    82                                             
    83     15.7 MiB      0.0 MiB           1       count = 1
    84     15.7 MiB      0.0 MiB           1       n = 2
    85     15.7 MiB      0.0 MiB        1222       while count <= i:
    86     15.7 MiB      0.0 MiB        1222           t = 1
    87     15.7 MiB      0.0 MiB        1222           is_simple = True
    88     15.7 MiB      0.0 MiB      115669           while t <= n:
    89     15.7 MiB      0.0 MiB      115469               if n % t == 0 and t != 1 and t != n:
    90     15.7 MiB      0.0 MiB        1022                   is_simple = False
    91     15.7 MiB      0.0 MiB        1022                   break
    92     15.7 MiB      0.0 MiB      114447               t += 1
    93     15.7 MiB      0.0 MiB        1222           if is_simple:
    94     15.7 MiB      0.0 MiB         200               if count == i:
    95     15.7 MiB      0.0 MiB           1                   break
    96     15.7 MiB      0.0 MiB         199               count += 1
    97     15.7 MiB      0.0 MiB        1221           n += 1
    98     15.7 MiB      0.0 MiB           1       return n


Eratosfen mode
Filename: D:/geekbrains hw/Algorythms/Урок 6. Практическое задание/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   100     15.7 MiB     15.7 MiB           1   @profile
   101                                         def erato(n):
   102     15.7 MiB      0.0 MiB           1       i = 2
   103     15.7 MiB      0.0 MiB           1       last_elem = n * 10
   104     15.8 MiB      0.1 MiB        2003       all_num = [z for z in range(last_elem)]
   105     15.8 MiB      0.0 MiB           1       all_num[1] = 0
   106     15.8 MiB      0.0 MiB        1999       while i < last_elem:
   107     15.8 MiB      0.0 MiB        1998           if all_num[i] != 0:
   108     15.8 MiB      0.0 MiB         303               check = i * 2
   109     15.8 MiB      0.0 MiB        4452               while check < last_elem:
   110     15.8 MiB      0.0 MiB        4149                   all_num[check] = 0
   111     15.8 MiB      0.0 MiB        4149                   check = check + i
   112     15.8 MiB      0.0 MiB        1998           i = i + 1
   113     15.8 MiB      0.0 MiB        2003       return [x for x in all_num if x != 0][n - 1]
   
По статистике видно, что поиск n-го натурально числа лучше применить с помощью решета эратосфена 
с наличием полного списка чисел, которые будут проверены позже, чем в ходе постепенной итерации и проверки подобного списка, что
сокращает количество операций и заметно ускоряет код, учитывая линии 88, 89 и 92 в первой функции
"""

@profile
def power_of(power, last_number):
    output = []
    n = 1
    while n <= last_number:
        res = n**power
        output.append(res)
        n += 1
    print(output)

@profile
def power_of2(pow, ln):
    output = list()
    for i in range(1, ln):
        output.append(i**pow)
    print(output)


power_of(2, 150)
power_of2(2, 150)

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   173     15.6 MiB     15.6 MiB           1   @profile
   174                                         def power_of(power, last_number):
   175     15.6 MiB      0.0 MiB           1       output = []
   176     15.6 MiB      0.0 MiB           1       n = 1
   177     15.6 MiB      0.0 MiB         151       while n <= last_number:
   178     15.6 MiB      0.0 MiB         150           res = n**power
   179     15.6 MiB      0.0 MiB         150           output.append(res)
   180     15.6 MiB      0.0 MiB         150           n += 1
   181     15.6 MiB      0.0 MiB           1       print(output)


Filename: D:/geekbrains hw/Algorythms/Урок 6. Практическое задание/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   183     15.6 MiB     15.6 MiB           1   @profile
   184                                         def power_of2(pow, ln):
   185     15.6 MiB      0.0 MiB           1       output = list()
   186     15.6 MiB      0.0 MiB         150       for i in range(1, ln):
   187     15.6 MiB      0.0 MiB         149           output.append(i**pow)


Из статистики видно, что поиск квадратов чисел лучше искать при помощи второй функции. Несмотря на практически идентичное
использование памяти, количество операций сократилось в два раза, что позволяет на более длительной дистанции сэкономить ресурсы.

"""