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


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))


"""
Суть решето понял, не придумал как сделать диапазон для поиска, 
в голове была мысль седалть диапозон по искомое число потом вызывать его из конца.
"""

def resheto_eratosvena():
    i = int(input('Введите число: '))

    a = []
    for k in range(i + 1):
        a.append(k)

    a[1] = 0

    n = 2
    while n <= i:
        if a[n] != 0:
            x = n + n
            while x <= i:
                a[x] = 0
                x = x + n
        n += 1

    a = set(a)
    a.remove(0)
    print(a)


resheto_eratosvena()
