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

"""
так как в решенных примерах не нашел кода с большими данными создал новые функции
пример 1 поиск индекса выбранного элемента
в первом случае использовал цикл
во втором случае использовал метод списк index
результат замеров показал значительное уменьшение затрат памяти
в третьем случае я использовал генератор для создания последовательности что показало еще лучшие результаты

    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
        24    403.9 MiB    403.9 MiB           1   @profile
        25                                         def search(el):
        26    404.3 MiB      0.4 MiB       10003       my_list = [el for el in range(10000)] !вот здесь
        27    404.3 MiB      0.0 MiB        3001       for i in range(len(my_list)):
        28    404.3 MiB      0.0 MiB        3001           if my_list[i] == el:
        29    404.3 MiB      0.0 MiB           1               return i
    
    
    3000
    Filename: /Users/olegbezrukov/gitKraken/python_algos_gb/Урок 6. Практическое задание/task_1.py
    
    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
        34    404.2 MiB    404.2 MiB           1   @profile
        35                                         def search2(el):
        36    404.3 MiB      0.1 MiB       10003       my_list = [el for el in range(10000)] !здесь
        37    404.3 MiB      0.0 MiB           1       return my_list.index(el)


    3000
"""


# создаем рандомный лист ищем в нем элемент
@profile
def search(el):
    my_list = [el for el in range(10000)]
    for i in range(len(my_list)):
        if my_list[i] == el:
            return i


# print(search(3000))

@profile
def search2(el):
    my_list = [el for el in range(10000)]
    return my_list.index(el)

# print(search2(3000))


@profile
def search3(el):
    my_list = (el for el in range(10000))
    for i in range(10000):
        if next(my_list) == el:
            return i

# print(search3(3000))

"""
Второй пример - поиск n-го числа Фибоначчи
В первом случае я реализую список и возвращаю в функции нужное значкение
Во втором случае я не сохраняю предыдущие значения, это существенно снижает затраты по памяти
Результаты замеров:
    84     13.6 MiB     13.6 MiB           1   @profile
    85                                         def fibo1(num):
    86     13.6 MiB      0.0 MiB           1       fib_list=[1,1]
    87     18.1 MiB      0.0 MiB       10000       for i in range(num-1):
    88     18.1 MiB      4.5 MiB        9999           new = fib_list[len(fib_list)-1] + fib_list[len(fib_list)-2]
    89     18.1 MiB      0.0 MiB        9999           fib_list.append(new)
    90     18.1 MiB      0.0 MiB           1       return fib_list[len(fib_list)-2]
    2 - вариант
     93     16.9 MiB     16.9 MiB           1   @profile
    94                                         def fibo2(num):
    95     16.9 MiB      0.0 MiB           1       fib1 = fib2 = 1
    96     16.9 MiB      0.0 MiB        9999       for i in range(2, num):
    97     16.9 MiB      0.0 MiB        9998           fib1, fib2 = fib2, fib1 + fib2
    98     16.9 MiB      0.0 MiB           1       return fib2
"""


@profile
def fibo1(num):
    fib_list=[1,1]
    for i in range(num-1):
        new = fib_list[len(fib_list)-1] + fib_list[len(fib_list)-2]
        fib_list.append(new)
    return fib_list[len(fib_list)-2]


@profile
def fibo2(num):
    fib1 = fib2 = 1
    for i in range(2, num):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2


print(fibo1(10000))
print(fibo2(10000))



