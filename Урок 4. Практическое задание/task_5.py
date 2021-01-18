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


from timeit import timeit, default_timer


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


number = int(input('Введите порядковый номер искомого простого числа: '))
print(timeit("simple(number)", "from __main__ import simple, number", number=100))
print(simple(number))

number = int(input("Введите порядковый номер искомого простого числа: "))


def eratosphen(n):
    a = []
    for i in range(n + 1):
        a.append(i)

    a[1] = 0
    i = 2
    while i <= len(a)-1:
        if i == len(a)-1:
            if len(set(a)) >= n:
                return a
            else:
                for number in range(len(a), (len(a)-1)*2):
                    a.append(number)
            i = 2
        if a[i] != 0:
            j = i + i
            while j <= len(a)-1:
                a[j] = 0
                j = j + i
        i += 1
    return a


print(timeit("eratosphen(number)", "from __main__ import eratosphen, number", number=100))

simple_list = eratosphen(number)
simple_list = list(filter(lambda x: x != 0, simple_list))

print(simple_list[number-1])

"""
Написанная с помощью решета эратосфена функция показывает себя в разы лучше с большими числами.
На нахождение 1000-ого элемента у простого перебора ушло около 45 сек, в то время как эратосфен затратил 
1,25 сек. На нахождение 100-ого потребовалось 0,27 сек у простого перебора и 0,1 у решета.
Но смаленькими значениями перебор справляется лучше: 0,0022 сек против 0,0035 сек
Сложность перебора O(n**2), у решета O(n logn)
"""