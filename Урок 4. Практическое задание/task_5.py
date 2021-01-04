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
from timeit import timeit


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    # O(n^2)
    while count <= i:                               #O(n)
        t = 1
        is_simple = True
        while t <= n:                               #O(n)
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


def my_find_simple(i):
    lst = [2]
    k = 3
    # for k in range(3, i+1, 2):
    while len(lst) < i:
        if (k > 10) and (k % 10 == 5):
            k += 2
            continue
        for el in lst:
            if el*el-1 > k:
                lst.append(k)
                break
            if k % el == 0:
                break
        else:
            lst.append(k)
        k += 2
    return lst[-1]


print('Нахождение простого числа с порядковым номером 10')
print(simple(10))
print(my_find_simple(10))
print(timeit('simple(10)', 'from __main__ import simple', number=1))
print(timeit('my_find_simple(10)', 'from __main__ import my_find_simple', number=1))
print('Нахождение простого числа с порядковым номером 100')
print(simple(100))
print(my_find_simple(100))
print(timeit('simple(100)', 'from __main__ import simple', number=1))
print(timeit('my_find_simple(100)', 'from __main__ import my_find_simple', number=1))
print('Нахождение простого числа с порядковым номером 1000')
print(simple(1000))
print(my_find_simple(1000))
print(timeit('simple(1000)', 'from __main__ import simple', number=1))
print(timeit('my_find_simple(1000)', 'from __main__ import my_find_simple', number=1))

"""
При нахождении простых числе в конечной последовательности алгоритм решето Эратосфена заметно быстрее, чем алгоритм
приведенный в задаче.
Однако целью задачи является не нахождение всех простых чисел в последовательности из n чисел, а нахождение простого
числа с порядковым номером n.
В этом случае прямое использование алгоритма Эратосфена получилось настолько затратнее чем алгоритм simple, что
его даже не стал оставлять в задаче.
Доработанный алгоритм my_find_simple по скорости поиска на порядкии превосходит simple, чем больше порядковый номер 
искомого просто числа, тем больше разница в скорости.
Происходит это из-за того, что simple проходит по всем числам от 0 до искомого, в то время как my_find_simple 
изначально выбрасывает из обработки четные числа, и числа делащиеся на 5, что уменьшает количество обрабатываемых 
элементов примерно в 3 раза.      
"""
