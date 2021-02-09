"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
"""
Замер с помощью инструмента timeit 
func_1 0.1941711 seconds
func_2 0.30075219999999997 seconds
func_3 0.18761289999999997 seconds

Как видно самый быстрый вариант решения - третий. В котором мы воспользовались возможностями встроенных функций.
И самый долгий второй. В котором для много лишних повторений операции count, создание доп списка, поиск max 
и сопостовление двух списков. 
"""
from timeit import timeit


array = [1, 3, 1, 3, 4, 5, 1]


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
    # пробегает по array и возвращает максимальное значение для переданной функции
    # в данном случае для count()
    mostly = max(array, key=array.count)
    return f'Чаще всего встречается число {mostly}, ' \
           f'оно появилось в массиве {array.count(mostly)} раз(а)'


def timeit_check():
    print("Замер с помощью инструмента timeit ")
    print(f"func_1 {timeit('func_1()', globals=globals(), number=100000)} seconds")
    print(f"func_2 {timeit('func_2()', globals=globals(), number=100000)} seconds")
    print(f"func_3 {timeit('func_3()', globals=globals(), number=100000)} seconds")


print(f"Рассмотрим список: {array}. {func_3()} ")

timeit_check()
