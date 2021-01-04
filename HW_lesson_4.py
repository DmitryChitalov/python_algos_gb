"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
from random import randint
from timeit import timeit
import cProfile


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


arr = []
n = 100
for i in range(n):
    arr.append(randint(0, 100))

print('\n', 10*'#', ' 1 ', 10*'#')
# print(arr)
# print(func_1(arr))
# print(func_2(arr))

print(timeit("func_1(arr)", setup="from __main__ import func_1, arr", number=1000))
print(timeit("func_2(arr)", setup="from __main__ import func_2, arr", number=1000))

'''
Результаты выполнения программмы:

1. Запуск 
0.019031099999999995
0.015409699999999998

2. Запуск
0.017677900000000003
0.01437949999999999

3. Запуск
0.020827300000000007
0.016261299999999992

4. Запуск
0.022052100000000005
0.016437900000000005

5. Запуск
0.020463499999999996
0.016122399999999995

Вывод:  С помощью генераторного выражения было уменьшено количество строк кода и время выполнения программы. 
        При увеличении количества элементов массива время выполнения программы уменьшается. 
'''

# ---------------------------------------------------------------------------------------------------------------------

"""
Задание 2.

Приведен код, который формирует из введенного числа обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""


def memorize(func):
    def g(number, memory={}):
        r = memory.get(number)
        if r is None:
            r = func(number)
            memory[number] = r
        return r
    return g


@memorize
def recursive_reverse_m(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


print('\n', 10*'#', ' 2 ', 10*'#')
print(recursive_reverse(1234))
print(recursive_reverse_m(1234))

print(timeit("recursive_reverse(1234)", setup="from __main__ import recursive_reverse", number=1000))
print(timeit("recursive_reverse_m(1234)", setup="from __main__ import recursive_reverse_m", number=1000))

'''
Время выполнения без мемоизации     = 0.003863199999999997
Время выполнения c мемоизацией      = 0.0003515000000000046

Вывод: цифры говорят сами за себя, мемоизация в 10 раз увеличивает скорость выполнения программы.
'''

# ---------------------------------------------------------------------------------------------------------------------

"""
Задание 3.

Приведен код, формирующий из введенного числа обратное по порядку входящих в него цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""


def revers(enter_num, revers_num=0):
    num = 0
    if enter_num == 0:
        return int(revers_num + num / 10)
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
    return int(revers_num)


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def main():
    revers(123456789)
    revers_2(123456789)
    revers_3(123456789)


print('\n', 10*'#', ' 3 ', 10*'#')

print(revers(123456789))
print(revers_2(123456789))
print(revers_3(123456789))

cProfile.run('main()')

print(timeit("revers(123456789)", setup="from __main__ import revers", number=1000))
print(timeit("revers_2(123456789)", setup="from __main__ import revers_2", number=1000))
print(timeit("revers_3(123456789)", setup="from __main__ import revers_3", number=1000))


"""
##########  3  ##########
987654321
987654321
987654321
         16 function calls (7 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     10/1    0.000    0.000    0.000    0.000 HW_lesson_4.py:140(revers)
        1    0.000    0.000    0.000    0.000 HW_lesson_4.py:151(revers_2)
        1    0.000    0.000    0.000    0.000 HW_lesson_4.py:159(revers_3)
        1    0.000    0.000    0.000    0.000 HW_lesson_4.py:165(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


0.009500599999999984
0.004269200000000001
0.0009321999999999941

Process finished with exit code 0


Вывод: рекурсия работает медленнее всего, а алгоритм работы со строкой работает быстрее всего. 
"""

# ---------------------------------------------------------------------------------------------------------------------

"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

array = [1, 3, 1, 3, 4, 5, 1]


def func_1(array):
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2(array):
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3(arr):
    stat = sorted([(i, arr.count(i)) for i in set(arr)], key=lambda t: t[1])[-1]
    return f'Чаще всего встречается число {stat[0]}, ' \
           f'оно появилось в массиве {stat[1]} раз(а)'


print('\n', 10*'#', ' 4 ', 10*'#')

lst = [1, 2, 3, 3, 6, 7, 3, 8, 9, 2, 3, 3, 6, 7, 3, 8, 9]
print(func_1(lst))
print(func_2(lst))
print(func_3(lst))

print()
print(timeit("func_1(lst)", setup="from __main__ import func_1, lst", number=1000))
print(timeit("func_2(lst)", setup="from __main__ import func_2, lst", number=1000))
print(timeit("func_3(lst)", setup="from __main__ import func_3, lst", number=1000))


'''
Результаты работы программы:
 ##########  4  ##########
Чаще всего встречается число 3, оно появилось в массиве 6 раз(а)
Чаще всего встречается число 3, оно появилось в массиве 6 раз(а)
Чаще всего встречается число 3, оно появилось в массиве 6 раз(а)

0.010036199999999981
0.012890299999999993
0.008704000000000017

Process finished with exit code 0


Выводы: отсортированный массив сокращает время выполнения программы 
'''


                    """ C Рождеством Христовым! """