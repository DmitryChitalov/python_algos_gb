"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from memory_profiler import profile
from datetime import datetime


def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func()
        print(datetime.now() - start)
        return result
    return wrapper()


num = int(input("Введите число"))


@profile
# @timer
def my_list(num):
    my_lst = [x for x in range(num)]
    return my_lst

#


@profile
# @timer
def my_dict(num):
    my_dct = {x: x for x in range(num)}
    return my_dct


print(my_list(num))
print(my_dict(num))  # Сделать замеры словаря и списка

"""
Line  # Mem usage    Increment  Occurences   Line Contents
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
32     15.6 MiB     15.6 MiB           1   @ profile
33                                         # @timer
34 def my_list(num):
    35     15.6 MiB      0.0 MiB          1003       my_lst = [x for x in range(num)]
    36     15.6 MiB      0.0 MiB           1 return my_lst

15.7 MiB     15.7 MiB           1   @ profile
    42                                         # @timer
    43 def my_dict(num):
        44     15.7 MiB      0.0 MiB          1003       my_dct = {x: x for x in range(num)}
        45     15.7 MiB      0.0 MiB           1 return my_dct

Для выполнения программы my_list выделено 15.6 Мебибайт. My_dict жу занимает 15, 7 . Разница появилась
только на значениях от 1000. До этого показания были аналогичны. Словарь как и ожидалось занимает больше места
за счет коллизий"""

# Вариант с рекурсией


@profile
def check_num(lst, even_n=0, odd_n=0):
    if len(lst) == 0:
        print(
            f'Количество четных символов равно: {even_n}', f'Количество нечетных равнo:{odd_n}')
        return
    elif (int(lst[0]) % 2) == 0:
        even_n += 1
    elif (int(lst[0]) % 2) == 1:
        odd_n += 1
    check_num(lst[1:], even_n, odd_n)


check_num(list(input("Введите число")))


# Вариант с циклом#
@profile
def check_num2(number, even_n=0, odd_n=0):
    digits = "02468"
    for i in number:
        if i in digits:
            even_n += 1
        else:
            odd_n += 1
    print(
        f'Количество четных символов равно:{even_n}', f'количество нечетных равно:{odd_n-1}')


check_num2(input("Введите число"))

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    73     15.6 MiB     15.6 MiB           5   @profile
    74                                         def check_num(lst, even_n=0, odd_n=0):
    75     15.6 MiB      0.0 MiB           5       if len(lst) == 0:
    76     15.6 MiB      0.0 MiB           2           print(
    77     15.6 MiB      0.0 MiB           1               f'Количество четных символов равно: {even_n}', f'Количество нечетных равнo:{odd_n}')
    78     15.6 MiB      0.0 MiB           1           return
    79     15.6 MiB      0.0 MiB           4       elif (int(lst[0]) % 2) == 0:
    80     15.6 MiB      0.0 MiB           3           even_n += 1
    81     15.6 MiB      0.0 MiB           1       elif (int(lst[0]) % 2) == 1:
    82     15.6 MiB      0.0 MiB           1           odd_n += 1
    83     15.7 MiB      0.0 MiB           4       check_num(lst[1:], even_n, odd_n)

Операция из за рекурсии выполняется столько, пока не происходит базовый случай. У меня вышло 5.
Check_num2  через цикл вызывается лишь один! раз, но занимает изначально больше памяти.15,7 Мэмибайт.
Возможно из-за еще одной переменной??
"""

array = [1, 3, 1, 3, 4, 5, 1]


@profile
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


@profile
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


 print(func_1())
print(func_2())

# func_1 15.6. Самое большое количество операций просиходит на цикле for.
# func_2 15.6- Число памяти аналогично. Вариант с генерационными выражениями дал большее
# количество операций, но сохранил прежний объем памяти
"""Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   146     15.6 MiB     15.6 MiB           1   @profile
   147                                         def func_2():
   148     15.6 MiB      0.0 MiB           1       new_array = []
   149     15.6 MiB      0.0 MiB           8       for el in array:
   150     15.6 MiB      0.0 MiB           7           count2 = array.count(el)
   151     15.6 MiB      0.0 MiB           7           new_array.append(count2)
   152
   153     15.6 MiB      0.0 MiB           1       max_2 = max(new_array)
   154     15.6 MiB      0.0 MiB           1       elem = array[new_array.index(max_2)]
   155     15.6 MiB      0.0 MiB           1       return f'Чаще всего встречается число {elem}, ' \
   156                                                    f'оно появилось в массиве {max_2} раз(а)'"""
