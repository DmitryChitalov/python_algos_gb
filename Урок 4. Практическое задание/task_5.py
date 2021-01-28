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


def simple_2(idx):
    """С использованием «Решета Эратосфена»"""
    n = 10000
    numbers = []
    for k in range(n + 1):
        numbers.append(k)

    numbers[1] = 0

    i = 2
    while i <= n:
        if numbers[i] != 0:
            j = i + i
            while j <= n:
                numbers[j] = 0
                j = j + i
        i += 1

    numbers = set(numbers)
    numbers.remove(0)
    numbers = sorted(list(numbers))
    return numbers[idx - 1]


idx = 10
print(simple(idx))
print(simple_2(idx))

idx = 100
print(simple(idx))
print(simple_2(idx))

idx = 1000
print(simple(idx))
print(simple_2(idx))

print(timeit('simple(1000)', globals=globals(), number=10))
print(timeit('simple_2(1000)', globals=globals(), number=10))

"""
Второй вариант функции (с решетом Эратосфена) работает гораздо быстрее

7.1652762999999995
0.06885610000000053

Однако, если первый вариант можно применять для любых чисел, то  второй 
ограничен по количеству элементов. Чтобы он учитывал любое количество 
натуральных чисел, функцию нужно переписать (у меня не хватило времени, 
не получилось).
"""

idx = 5000
print(simple(idx))
print(simple_2(idx))

"""
При поиске 5000го элемента первая функция работает долго, но работает. 

48611

Вторая же выдаёт ошибку

Traceback (most recent call last):
  File "D:/programming/python_algos_gb/Урок 4. 
  Практическое задание/task_5.py", line 93, in <module>
    print(simple_2(idx))
  File "D:/programming/python_algos_gb/Урок 4. 
  Практическое задание/task_5.py", line 59, in simple_2
    return numbers[idx-1]
IndexError: list index out of range


Так как она может выбрать простые числа только из 10000 натуральных чисел.

К сожалению, оба решения неидеальны, хороший вариант решения я написать не 
успела
"""
