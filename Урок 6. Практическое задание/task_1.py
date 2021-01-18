import sys
from memory_profiler import profile

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

# ВЕРСИЯ ПИТОН 3.8 64-бит win10 Взял задачи из 3-го -4го урока
@profile
def task_1(number):
    for elem in range(1, number + 1):
        yield elem

@profile
def task_1_1():
    list = []
    for elem in range(10000):
        list.append(elem)
    return list

@profile
def task_1_2(number):
    list = []
    for elem in number:
        list.append(elem * 2)
        return list

@profile
def task_1_3(number):
    list = [el * 2 for el in number]
    return list

@profile
def num_sum(letters='12345'):
    s_list = []
    for elem in letters:
        try:
            s_list.append(int(elem))
        except ValueError:
            break
    return sum(s_list)



@profile
def row(el_cnt, el=1):
    el_list_for_sum = []
    if el_cnt == 0:
        print('Сумма элементов равна: ' + str(sum(el_list_for_sum)))
    else:
        el_list_for_sum.append(el)
        el /= 2 * -1
        return row(el_cnt - 1, el)



a = task_1(500000)
b = task_1_1()
c = task_1_2(b)
print(sys.getrefcount(c))
d = task_1_3(b)
c = num_sum
print(sys.getrefcount(c))
del c


print(sys.getrefcount(a))
print(sys.getrefcount(b))
print(sys.getrefcount(d))
print(sys.getrefcount(row))


"""
Начем с простого, а именно функции "sys.getrefcount", в данном примере я заменил перменную "с", соответственно,
количество ссылок, где эта переменная используется увеличилось
Профайлер не сработал с yield, поскольку массив в памяти мы не храним.
Далее, исходя из списков функций. Переменная list занимает больше места, если в нее добавить элемент, чем использование 
генераторгого выражения
"""