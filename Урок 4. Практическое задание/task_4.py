"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 7, 5, 5, 9, 8]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

def func_3():
    elem = max(set(array), key=array.count)
    max_3 = array.count(elem)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_3} раз(а)'


print(array)
print(func_1())
print(func_2())
print(func_3())


Num = 100000


print("func_1 - ", timeit('func_1()', setup='from __main__ import func_1', number=Num))
print("func_2 - ", timeit('func_2()', setup='from __main__ import func_2', number=Num))
print("func_3 - ", timeit('func_3()', setup='from __main__ import func_3', number=Num))


#
# Функция 1 (перебор) - самый оптимальный с точки зрения времени выполнения.
#
# Функция 2 (перебор со списком кол-ва вхождений каждого эллемента) является самой медленной,
# т к доп.список также требует времени на исполнение
#
# Функция 3 (поиск по ключу) - быстрая, однако зависит от количества эллементов в массиве.
# При малом количестве эллементов она медленнее функции 1,
# однако чем больше массив - тем больше выигрыш во времени исполнения по сравнению с функцией 1.

