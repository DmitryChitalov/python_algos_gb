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
num = int(input('Введите порядковый номер простого числа(до 10 000): ')) #ограничение в 10000 не случайно,
# доля простых чисел в ряду  на первые 10 тыс простых составляет около 10%, этот показатель определяет
# длину исходного списка чисел для просеивания. Представленное решение это адаптированный вариант под условия
# этой задачи,найденного мной в открытых источниках эффективного решета


def primes(n=num * 10, verbose=0):
    """ Returns  a list of primes < n """
    def pr(*args):
        if verbose > 0:
            print(*args)
    sieve = [True] * n
    pr("все чётные числа игнорируются и будут пропущены при возврате...\n")
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            pr('содержимое решета:\t{}'.format([x for x in range(3, n, 2) if sieve[x]]))
            pr(f'i:{i} вычёркиваем все числа кратные "{i}", начиная с "{i}^2": {list(range(i*i, n, 2*i))}')
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
            pr(f'sieve[{i}*{i}::2*{i}] = [False]*(({n-i}*{i-1})//(2*{i})+1)')
            pr('содержимое решета:\t{}'.format([x for x in range(3, n, 2) if sieve[x]]))
            pr('*' * 60)
        result = [2] + [i for i in range(3, n, 2) if sieve[i]]
    return result[num-1]


def simple(num):
    count = 1
    n = 2
    while count <= num:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == num:
                break
            count += 1
        n += 1
    return n


print(simple(num))
print(primes())

print(timeit.timeit("primes()", setup="from __main__ import primes, num", number=100))
print(timeit.timeit("simple(num)", setup="from __main__ import simple, num", number=100))

'''При поиске числа с порядковым номером 10 в списке из простых чисел "наивный" поиск работает лучше,чем рещето
 Но чем больше становится искомое число, тем больше разрыв в производительности в пользу решета.
 '''