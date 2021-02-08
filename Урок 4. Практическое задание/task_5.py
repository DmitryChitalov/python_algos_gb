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


def get_sim_erat(i_ind):
    # список заполняется значениями от 0 до n
    a = []
    n = i_ind
    n = n * 10
    for i in range(n + 1):
            a.append(i)

    # Вторым элементом является единица,
    # которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    # начинаем с 3-го элемента
    i = 2
    while i <= n:
        # Если значение ячейки до этого
        # не было обнулено,
        # в этой ячейке содержится
        # простое число.
        if a[i] != 0:
            # первое кратное ему
            # будет в два раза больше
            j = i + i
            while j <= n:
                # это число составное,
                # поэтому заменяем его нулем
                a[j] = 0
                # переходим к следующему числу,
                # которое кратно i
                # (оно на i больше)
                j = j + i
        i += 1

    res = []
    for rec in a:
        if rec != 0:
            res.append(rec)
    #print(res)
    #print(len(res))
    return res[i_ind-1]


#i = int(input('Введите порядковый номер искомого простого числа: '))
#print(simple(i))
print('simple(10)', simple(10))
print('get_sim_erat(10)', get_sim_erat(10))
print('simple(100)', simple(100))
print('get_sim_erat(100)', get_sim_erat(100))
print('simple(1000)', simple(1000))
print('get_sim_erat(1000)', get_sim_erat(1000))

print('simple(10)', timeit('simple(10)', setup='from __main__ import simple', number=100))
print('simple(100)', timeit('simple(100)', setup='from __main__ import simple', number=100))
print('simple(1000)', timeit('simple(1000)', setup='from __main__ import simple', number=100))

print('get_sim_erat(10)', timeit('get_sim_erat(10)', setup='from __main__ import get_sim_erat', number=100))
print('get_sim_erat(100)', timeit('get_sim_erat(100)', setup='from __main__ import get_sim_erat', number=100))
print('get_sim_erat(1000)', timeit('get_sim_erat(1000)', setup='from __main__ import get_sim_erat', number=100))
# На сравнительно небольших числах(в пределах нескольких десятков)
# алгоритм через перебор делителей является более быстрым, чем
# алгоритм "Решето эратосфена".
# Видимо здесь идет влияние работа с дополнительным списком:
# его создание, размещение в памяти, и т.п.
# На больших числах алгоритм "Решето эратосфена" показывает
# меньшее время работы.
# При увеличении числа элементов алгоритм "Решето эратосфена"
# показывает все больший отрыв по времени работы.
# Алгоритм через перебор имеет сложность O(n**2)(цикл в цикле),
# где на каждой операции идет операция остаток от деления,
# тогда как второй алгоритм имеет сложность O(n*log(n)),
# где на каждой операции идет обнуление элемента.
# Вывод: алгоритм "Решето эратосфена" намного эффективнее, чем
# алгоритм перебор делителей.
