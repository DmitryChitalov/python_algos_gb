"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""

import cProfile


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


def sieve(n, m=1):
    # список заполняется значениями от 0 до n
    a = [p for p in range(n+1000*m)]

    # Вторым элементом является единица,
    # которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    # начинаем с 3-го элемента
    i = 2
    while i <= n+1000*m-1:
        # Если значение ячейки до этого
        # не было обнулено,
        # в этой ячейке содержится
        # простое число.
        if a[i] != 0:
            # первое кратное ему
            # будет в два раза больше
            j = i + i
            while j <= n+1000*m-1:
                # это число составное,
                # поэтому заменяем его нулем
                a[j] = 0
                # переходим к следующему числу,
                # которое кратно i
                # (оно на i больше)
                j = j + i
        i += 1

    if (len(set(a))) < n:
        return sieve(n, m+2)
    else:
        # Превращая список во множество,
        # избавляемся от всех нулей кроме одного.
        a = sorted(list(set(a)))
        # удаляем ноль
        a.remove(0)
        return a[n-1]


# i = int(input('Введите порядковый номер искомого простого числа: '))
cProfile.run('simple(1000)')
cProfile.run('sieve(1000)')
"""Главным недостатком решета, что изначально мы не знаем, где может находиться искомое простое число
поэтому необходимо строить каждый раз массив. В моей реализации используется итерация функции,
потому скорость может различаться, меняя значения в строке 71 m+2 на m+4, например для заведомо больших чисел.
Для больших величин, решето существенно превосходит в скорости симпл.
         4 function calls in 0.583 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.583    0.583 <string>:1(<module>)
        1    0.583    0.583    0.583    0.583 task_5.py:20(simple)
        1    0.000    0.000    0.583    0.583 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         17 function calls (14 primitive calls) in 0.018 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.018    0.018 <string>:1(<module>)
      4/1    0.017    0.004    0.018    0.018 task_5.py:40(sieve)
        4    0.001    0.000    0.001    0.000 task_5.py:42(<listcomp>)
        1    0.000    0.000    0.018    0.018 {built-in method builtins.exec}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}"""