"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

from timeit import timeit
import cProfile


def revers(enter_num, revers_num=0):
    # Функция ничего не возвращала. На уроке об этом ни слова не было. Только у меня так?
    # Код поправил, теперь результат возвращается.
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


num = int(input('Введите целое число: '))
print(revers(num))
print(revers_2(num))
print(revers_3(num))

print('Рекурсия:', timeit('revers(num)', 'from __main__ import revers, num'))
print('Цикл:    ', timeit('revers_2(num)', 'from __main__ import revers_2, num'))
print('Срез:    ', timeit('revers_3(num)', 'from __main__ import revers_3, num'))

cProfile.run(f'revers({num})')
cProfile.run(f'revers_2({num})')
cProfile.run(f'revers_3({num})')

"""
Введите целое число: 12345678909
90987654321.0
90987654321.0
90987654321
Рекурсия: 3.243458885997825
Цикл:     2.219692529000895
Срез:     0.3762004470008833
         15 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     12/1    0.000    0.000    0.000    0.000 task_3.py:17(revers)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:29(revers_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:37(revers_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

Самая неэффективная реализация - через рекурсию. Рекурсивные вызовы сами по себе ресурсоемкие. 
Плюс добавляются математические вычисления.
Реализация через цикл заметно эффективнее рекрсивной. Разница из-за отсутствия накладных расходов на вызов функций.
Самый эффективный способ - это через срезы. В отличие от предыдущих методов здесь отсутсвуют математические действия.
"""
