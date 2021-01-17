"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

from memory_profiler import profile

@profile()
def func1():
    my_list = [7, 5, 3, 3, 2]
    new_el = input("введите новый елемент рейтинга:")
    new_el = int(new_el)
    n = 0
    for i in range(len(my_list)):
        if new_el == my_list[i]:
            my_list.insert(i + 1, new_el)
            break


        elif new_el < my_list[i] and new_el > my_list[i + 1]:
            my_list.insert(i + 1, new_el)
            break
        elif new_el < my_list[-1]:
            my_list.insert(len(my_list), new_el)
            break

        elif new_el > my_list[0]:
            my_list.insert(0, new_el)
            break

    print(my_list)
    """ в этом коде изначально используется 15.6 миб и инкремент везде 0.0
    и в итоговом тоже используется 15.6"""
@profile()
def func2():
    my_list = [7, 5, 3, 3, 2]
    new_el = input("введите новый елемент рейтинга:")
    new_el = int(new_el)
    a=list(range(10000000))
    n = 0
    for i in range(len(my_list)):
        if new_el == my_list[i]:
            my_list.insert(i + 1, new_el)
            break


        elif new_el < my_list[i] and new_el > my_list[i + 1]:
            my_list.insert(i + 1, new_el)
            break
        elif new_el < my_list[-1]:
            my_list.insert(len(my_list), new_el)
            break

        elif new_el > my_list[0]:
            my_list.insert(0, new_el)
            break

    print(my_list)
    """
     а в этом коде из-за листа а 15.6 памяти добавляется 191.9 и итого тратится 207.5миб
     python 3.8
     oc 64
    """
#func1()
func2()




"""22222222"""

from pympler import asizeof
from memory_profiler import profile


class Road:
    def __init__(self, width, length):
        self.__width = width
        self.__length = length

    def result(self):
        self.weigh = 12
        self.thickness = 5
        x = self.weigh * self.thickness * self.__width * self.__length
        print(x)


def func():
    rslt = Road(width=10, length=7)
    rslt.result()
    print("func", asizeof.asizeof((rslt)))


class Broad:
    __slots__ = ['width', 'length']

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def result(self):
        self.weigh = 12
        self.thickness = 5
        x = self.weigh * self.thickness * self.width * self.length
        print(x)


def func2():
    rslt1 = Broad(width=10, length=7)
    print(rslt1.__slots__)

    print("func2", asizeof.asizeof((rslt1)))


func()
func2()
"""
в первом классе используется 304
а во втаром из-за слотов стало 56
"""
