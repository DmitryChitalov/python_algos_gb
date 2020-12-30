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
import timeit

n = 1000

def simple(i):  # Максимальная сложность O(n^2), т.к есть 2 вложенных цикла
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


def my_solution(n): # Максимальная сложность O(n^2), т.к есть 2 вложенных цикла, но при данном алгоритме получаем выйгрыш во времени
    s = set()
    s.add(2)
    i = 3
    while len(s) != n:
        is_simple = False
        length_c = len(s)
        for el in s:
            length_c -= 1
            if i % el != 0:
                if length_c == 0:
                    is_simple = True
            else:
                break
        if is_simple:
          s.add(i)
        i += 1
    return sorted(s)

print(f'{n}-й элемент(наивный алгоритм): ',simple(n))
print(f'{n}-й элемент(мой алгоритм): ',my_solution(n)[-1])

print("Время наивного алгоритма: ",timeit.timeit("simple(n)",setup= "from __main__ import simple, n",number=10))
print("Время моего алгоритма: ",timeit.timeit("my_solution(n)",setup= "from __main__ import my_solution, n",number=10))
"""
При n = 100:
    541
    541
    0.035140475 simple 
    0.011949711 my_solution
    
При n = 1000:
    7919
    7919
    5.596825657  simple 
    1.086853111  my_solution
Вывод: Написанный мной алгоритм оказался эффективнее по времени.
        Мы убедились этому благодаря замерам времени данных алгоритмов 
"""

