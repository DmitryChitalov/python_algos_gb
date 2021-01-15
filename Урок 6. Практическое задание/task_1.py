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
from timeit import timeit
from memory_profiler import profile, memory_usage
from random import randint
from math import log


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
            # print(n)
            if count == i:
                break
            count += 1
        n += 1
    return n


# сложность квадратичная - O(n**2)


@profile
def separator(i):
    """С использованием «Решета Эратосфена»"""
    m = i ** 2
    test_list = [a for a in range(m)]
    test_list[1] = 0
    n = 2
    while n <= m - 1:
        if test_list[n] != 0:
            new_n = n * 2
            while new_n <= m - 1:
                test_list[new_n] = 0
                new_n = new_n + n
        n += 1
    test_list = sorted(list(set(test_list)))
    return test_list[i]


# сложность квадратичная - O(n**2), по большей части из-за формирования начального ряда возведением в квадрат и
# последующей необходимости прореживать весь этот ряд


@profile
def separator_2(i):
    """2 c использованием «Решета Эратосфена»"""
    # m = i *15# работает примерно до i=500000
    m = int(i * (log(i ** 2)))  # на поиске 10'000'000-го простого числа у меня пямять на машине кончилась,
    # но милионное вполне себе ищет
    test_list = [a for a in range(m)]
    test_list[1] = 0
    n = 2
    while n <= m - 1:
        if test_list[n] != 0:
            new_n = n * 2
            while new_n <= m - 1:
                test_list[new_n] = 0
                new_n = new_n + n
        n += 1
    test_list = sorted(list(set(test_list)))
    return test_list[i]


# сложность логарифмическая O(log n) т.к, количество операций уменьшается на каждой итерации


@profile
def simple_rec(i, count=1, n=2):
    sys.setrecursionlimit(1700)
    if count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                return n
            count += 1
        n += 1
        return simple_rec(i, count, n)


# сложность квадратичная O(n**2)


@profile
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@profile
def func_2(nums):  # тоже самое через выражение
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


@profile
def func_3(nums):  # для количества добьем, но будет плохо
    new_arr = [i[0] for i in enumerate(nums) if i[1] % 2 == 0]
    return new_arr


@profile
def func_4(nums):  # кажется я придумал самый долгий способ для этой задачи...
    num_nums = enumerate(nums)
    new_arr = [i[0] for i in list(filter(lambda x: x[1] % 2 == 0, num_nums))]
    return new_arr


if __name__ == '__main__':
    # i = int(input('Введите порядковый номер искомого простого числа: '))
    # simple(i)
    # separator(i)
    # separator_2(i)

    """Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
        30     19.8 MiB     19.8 MiB           1   @profile
        31                                         def simple(i):
        32                                             "Без использования «Решета Эратосфена»"
        33     19.8 MiB      0.0 MiB           1       count = 1
        34     19.8 MiB      0.0 MiB           1       n = 2
        35     19.9 MiB      0.0 MiB        3120       while count <= i:
        36     19.9 MiB      0.0 MiB        3120           t = 1
        37     19.9 MiB      0.0 MiB        3120           is_simple = True
        38     19.9 MiB      0.0 MiB      652189           while t <= n:
        39     19.9 MiB      0.0 MiB      651744               if n % t == 0 and t != 1 and t != n:
        40     19.9 MiB      0.0 MiB        2675                   is_simple = False
        41     19.9 MiB      0.0 MiB        2675                   break
        42     19.9 MiB      0.0 MiB      649069               t += 1
        43     19.9 MiB      0.0 MiB        3120           if is_simple:
        44                                                     # print(n)
        45     19.9 MiB      0.0 MiB         445               if count == i:
        46     19.9 MiB      0.0 MiB           1                   break
        47     19.9 MiB      0.0 MiB         444               count += 1
        48     19.9 MiB      0.0 MiB        3119           n += 1
        49     19.9 MiB      0.0 MiB           1       return n
     В этом варианте потребления памяти практически нет потому что идет перебор по одному значению, 
     после чего ссылка на использованое значение удаляется
    
    
    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
        53     19.9 MiB     19.9 MiB           1   @profile
        54                                         def separator(i):
        55                                             "С использованием «Решета Эратосфена»"
        56     19.9 MiB      0.0 MiB           1       m = i**2
        57     28.6 MiB  -2780.3 MiB      198028       test_list = [a for a in range(m)]
        58     28.6 MiB      0.0 MiB           1       test_list[1] = 0
        59     28.6 MiB      0.0 MiB           1       n = 2
        60     28.6 MiB      0.0 MiB      198024       while n <= m-1:
        61     28.6 MiB      0.0 MiB      198023           if test_list[n] != 0:
        62     28.6 MiB      0.0 MiB       17823               new_n = n*2
        63     28.6 MiB      0.0 MiB      539447               while new_n <= m-1:
        64     28.6 MiB      0.0 MiB      521624                   test_list[new_n] = 0
        65     28.6 MiB      0.0 MiB      521624                   new_n = new_n+n
        66     28.6 MiB      0.0 MiB      198023           n += 1
        67     26.4 MiB     -2.2 MiB           1       test_list = sorted(list(set(test_list)))
        68     26.4 MiB      0.0 MiB           1       return test_list[i]
        
    В этом варианте рост памяти заметен при генерации массива. 
    Также заметно некоторое освобождение памяти когда множеством убираются лишние нули
    
    
    
    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
        73     20.1 MiB     20.1 MiB           1   @profile
        74                                         def separator_2(i):
        75                                             "2 c использованием «Решета Эратосфена»"
        76                                             # m = i *15# работает примерно до i=500000
        77     20.1 MiB      0.0 MiB           1       m = int(i*(log(i**2))) # на поиске 10'000'000-го простого числа у меня пямять на машине кончилась,
        78                                             # но милионное вполне себе ищет
        79     20.2 MiB      0.2 MiB        5430       test_list = [a for a in range(m)]
        80     20.2 MiB      0.0 MiB           1       test_list[1] = 0
        81     20.2 MiB      0.0 MiB           1       n = 2
        82     20.2 MiB      0.0 MiB        5426       while n <= m - 1:
        83     20.2 MiB      0.0 MiB        5425           if test_list[n] != 0:
        84     20.2 MiB      0.0 MiB         716               new_n = n * 2
        85     20.2 MiB      0.0 MiB       12793               while new_n <= m - 1:
        86     20.2 MiB      0.0 MiB       12077                   test_list[new_n] = 0
        87     20.2 MiB      0.0 MiB       12077                   new_n = new_n + n
        88     20.2 MiB      0.0 MiB        5425           n += 1
        89     20.3 MiB      0.0 MiB           1       test_list = sorted(list(set(test_list)))
        90     20.3 MiB      0.0 MiB           1       return test_list[i]
        
        Как и в предыдущем варианте  потребление памяти заметно при генерации списка. почему 100KiB отъело 
        при очистке нулей не очень понятно, возможно  сортировка требует расход памяти. 
        При этом так как исходный список меньше чем в прошлом варианте - памяти так же потребовалось меньше
        
        """
    my_nums = [randint(1, 1000) for i in range(100000)]
    func_1(my_nums)
    func_2(my_nums)
    func_3(my_nums)
    func_4(my_nums)
    """
        Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
       114     23.5 MiB     23.5 MiB           1   @profile
       115                                         def func_1(nums):
       116     23.5 MiB      0.0 MiB           1       new_arr = []
       117     25.2 MiB      0.0 MiB      100001       for i in range(len(nums)):
       118     25.2 MiB      1.5 MiB      100000           if nums[i] % 2 == 0:
       119     25.2 MiB      0.2 MiB       49938               new_arr.append(i)
       120     25.2 MiB      0.0 MiB           1       return new_arr
    при переборе массива выделяется память т.к. мы вызываем все элементы массива, а также память занимает новый массив.
    
          
    
    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
       123     23.3 MiB     23.3 MiB           1   @profile
       124                                         def func_2(nums):  # тоже самое через выражение
       125     25.2 MiB      1.9 MiB      100003       new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
       126     25.2 MiB      0.0 MiB           1       return new_arr
    что интересно, памяти понадобилось больше на этом варианте чем в предыдущем, хотя это же по сути тоже самое. 
    С другой стороны он и работает чуть быстрее
    
    
    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
       129     23.5 MiB     23.5 MiB           1   @profile
       130                                         def func_3(nums):  # для количества добьем, но будет плохо
       131     25.2 MiB      1.6 MiB      100003       new_arr = [i[0] for i in enumerate(nums) if i[1] % 2 == 0]
       132     25.2 MiB      0.0 MiB           1       return new_arr
    этот вариант по памяти выигрывает у первого и второго, но проигрывал им по производительности. 
    Производительность просела из-за дополнительно операции enumerate, 
    но она создала кортежи из которых осуществлялась дальнейшая выборка, 
    вероятно за счет кортежей и удалось сократить потребление памяти
    

    
    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
       135     24.2 MiB     24.2 MiB           1   @profile
       136                                         def func_4(nums):  # кажется я придумал самый долгий способ для этой задачи...
       137     24.2 MiB      0.0 MiB           1       num_nums = enumerate(nums)
       138     29.3 MiB      3.2 MiB      249941       new_arr = [i[0] for i in list(filter(lambda x: x[1] % 2 == 0, num_nums))]
       139     28.3 MiB     -1.0 MiB           1       return new_arr
       
       Этот способ помимо того что он самый долгий оказался и еще и самым прожорливым. 
       Кстати по вхождениям очень удобно смотреть сложность если известен исходный датасет - т.е. на вход я подавал 100к 
       элементов. В первых 3х вариантах около того же было и вхождений, а в 4м случае 250к вхождений. 
       Итого  можно предположить что он примерно в 2.5 раза больше операций делает. 
       Рост потребления памяти скорее всего связам именно с лишними операциями  т.е. сначала  мы отфильтровали 
       кортежи с нечетным [1] элементом пробегом по пелному списку, потом из этого списка кортежей, 
       еще раз пробежав по полному списку, но уже примерно половине от исходного (статистически) выбрали [0]-е элементы
    """
