"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса
Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import json
import pickle
import random
import sys

from memory_profiler import profile

"""
В качестве первого примера я решила использовать сериализацию файлов (модули 
pickle, json) и обычную запись в файл.

Система: win 10 x64
Python: 3.8

"""


def random_string():
    return "".join([chr(64 + random.randint(0, 25)) for _ in range(20)])


@profile
def create_file_j():
    x = [(random.random(),
          random_string(),
          random.randint(0, 2 ** 64))
         for _ in range(300000)]

    with open('data.json', 'w') as f:
        json.dump(x, f)


@profile
def load_file_j():
    with open('data.json', 'r') as f:
        y = json.load(f)
    return y


@profile
def create_file_p():
    x = [(random.random(),
          random_string(),
          random.randint(0, 2 ** 64))
         for _ in range(300000)]

    with open('data.pickle', 'wb') as f:
        pickle.dump(x, f)


@profile
def load_file_p():
    with open('data.pickle', 'rb') as f:
        y = pickle.load(f)
    return y


@profile
def create_file():
    x = [(random.random(),
          random_string(),
          random.randint(0, 2 ** 64))
         for _ in range(300000)]

    with open('data.txt', 'w') as f:
        for xx in x:
            print(xx, file=f)


@profile
def load_file():
    y = []
    with open('data.txt', 'r') as f:
        for line in f:
            f, s, t = line.split(', ')
            f = float(f.strip('('))
            s = s.strip('\'')
            t = int(t.strip(')\n'))
            line = f, s, t
            y.append(line)
    return y


if __name__ == "__main__":
    create_file()
    load_file()

    create_file_j()
    load_file_j()

    create_file_p()
    load_file_p()

"""
Запись в файл:

Line #    Mem usage    Increment   Line Contents
================================================
   161     13.7 MiB      0.0 MiB   @profile
   162                             def create_file():
   163     50.2 MiB     36.5 MiB       x = [(random.random(),
   164     50.2 MiB      0.0 MiB             random_string(),
   165     50.2 MiB      0.0 MiB             random.randint(0, 2 ** 64))
   166     13.7 MiB    -36.5 MiB            for _ in range(300000)]
   167
   168     50.2 MiB     36.5 MiB       with open('data.txt', 'w') as f:
   169     50.2 MiB      0.0 MiB           for xx in x:
   170     50.2 MiB      0.0 MiB               print(xx, file=f)


Line #    Mem usage    Increment   Line Contents
================================================
   173     14.4 MiB      0.0 MiB   @profile
   174                             def load_file():
   175     14.4 MiB      0.0 MiB       y = []
   176     14.4 MiB      0.0 MiB       with open('data.txt', 'r') as f:
   177     49.7 MiB     35.4 MiB           for line in f:
   178     49.7 MiB      0.0 MiB               f, s, t = line.split(', ')
   179     49.7 MiB      0.0 MiB               f = float(f.strip('('))
   180     49.7 MiB      0.0 MiB               s = s.strip('\'')
   181     49.7 MiB      0.0 MiB               t = int(t.strip(')\n'))
   182     49.7 MiB      0.0 MiB               line = f, s, t
   183     49.7 MiB      0.0 MiB               y.append(line)
   184     49.7 MiB      0.0 MiB       return y



Использование модуля json

Line #    Mem usage    Increment   Line Contents
================================================
   125     15.3 MiB      0.0 MiB   @profile
   126                             def create_file_j():
   127     50.1 MiB     34.8 MiB       x = [(random.random(),
   128     50.1 MiB      0.0 MiB             random_string(),
   129     50.1 MiB      0.0 MiB             random.randint(0, 2 ** 64))
   130     15.3 MiB    -34.8 MiB            for _ in range(300000)]
   131
   132     50.1 MiB     34.8 MiB       with open('data.json', 'w') as f:
   133     50.1 MiB      0.0 MiB           json.dump(x, f)


Line #    Mem usage    Increment   Line Contents
================================================
   136     15.4 MiB      0.0 MiB   @profile
   137                             def load_file_j():
   138     15.4 MiB      0.0 MiB       with open('data.json', 'r') as f:
   139     54.7 MiB     39.3 MiB           y = json.load(f)
   140     54.7 MiB      0.0 MiB       return y

Использование модуля pickle:

Line #    Mem usage    Increment   Line Contents
================================================
   143     15.8 MiB      0.0 MiB   @profile
   144                             def create_file_p():
   145     49.8 MiB     34.0 MiB       x = [(random.random(),
   146     49.8 MiB      0.0 MiB             random_string(),
   147     49.8 MiB      0.0 MiB             random.randint(0, 2 ** 64))
   148     15.8 MiB    -34.0 MiB            for _ in range(300000)]
   149
   150     49.8 MiB     34.0 MiB       with open('data.pickle', 'wb') as f:
   151     49.9 MiB      0.2 MiB           pickle.dump(x, f)



Line #    Mem usage    Increment   Line Contents
================================================
   154     15.7 MiB      0.0 MiB   @profile
   155                             def load_file_p():
   156     15.7 MiB      0.0 MiB       with open('data.pickle', 'rb') as f:
   157     49.9 MiB     34.1 MiB           y = pickle.load(f)
   158     49.9 MiB      0.0 MiB       return y


Хотя я ожидала увидеть другие результаты, я не заметила особой разницы между
использованием json, pickle и записью в файл. Да, json тратит чуть больше
памяти, чем используется при записи в файл, однако он более универсальный,
сама функция проще пишется и лучше выглядит, поэтому, на мой взгляд,
он предпочительнее.

________________________________________________________________________


В качестве второго примера я решила использовать подсчёт суммы натурального
ряда с помощью цикла и с помощью рекурсии.

"""


@profile
def sum_natural(n):
    sum_n = 0
    for n in range(n + 1):
        sum_n += n
    return sum_n


def sum_natural_rec(n):
    if n == 1:
        return n
    else:
        return sum_natural_rec(n - 1) + n


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    print(sum_natural(5555))
    sum_n_rec = profile(sum_natural_rec)
    print(sum_n_rec(5555))

"""
Подсчёт через цикл: затраты памяти незаметны

Line #    Mem usage    Increment   Line Contents
================================================
   229     13.8 MiB      0.0 MiB   @profile
   230                             def sum_natural(n):
   231     13.8 MiB      0.0 MiB       sum_n = 0
   232     13.8 MiB      0.0 MiB       for n in range(n + 1):
   233     13.8 MiB      0.0 MiB           sum_n += n
   234     13.8 MiB      0.0 MiB       return sum_n


Подсчёт через рекурсию: затраты памяти на 4.5 MiB Больше, чем в предыдущем
методе, так как требуется память для хранения стека вызовов

Line #    Mem usage    Increment   Line Contents
============================================================
   237     18.3 MiB      0.0 MiB   def sum_natural_rec(n):
   238     18.3 MiB      0.0 MiB       if n == 1:
   239     18.3 MiB      0.0 MiB           return n
   240                                 else:
   241     18.3 MiB      0.0 MiB           return sum_natural_rec(n - 1) + n

Также в этом примере я решила 3е задание из домашней работы - использование
декораторов для рекурсивных вызовов. Чтобы функция-декоратор не вызывалась
каждый раз при рекурсивном вызове, необходимо поместить декоратор в
переменную с названием, отличным от названия функции.
Другой вариант - поместить рекурсивную функцию в дополнительную функцию -
обертку:
"""


@profile
def rec_wrapper(num):
    def sum_natural_r(n):
        if n == 1:
            return n
        else:
            return sum_natural_r(n - 1) + n

    return sum_natural_r(num)


if __name__ == "__main__":
    print(rec_wrapper(555))

"""
В качестве третьего варианта используем скрипт из курса основ:
"""
# 4. Представлен список чисел. Определить элементы списка, не имеющие
# повторений. Сформировать итоговый массив чисел, соответствующих
# требованию. Элементы вывести в порядке их следования в исходном
# списке. Для выполнения задания обязательно использовать генератор
# списка. (Можно использовать list.count()).
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

first_list = [random.randint(1, 10000000) for i in range(100000)]


@profile
def change_list(lst):
    result_list = [i for i in lst if lst.count(i) == 1]
    return result_list


@profile
def change_list_2(lst):
    dict_1 = {}

    for i in lst:
        if i not in dict_1:
            dict_1[i] = 1
        else:
            dict_1[i] += 1
    result_list = [i for i in dict_1 if dict_1[i] == 1]
    return result_list


if __name__ == "__main__":
    change_list(first_list)
    change_list_2(first_list)

"""
Использование списка и list.count:

Line #    Mem usage    Increment   Line Contents
================================================
   292     16.6 MiB      0.0 MiB   @profile
   293                             def change_list(lst):
   294     17.2 MiB      0.6 MiB       result_list = [i for i in lst if 
                                                            lst.count(i) == 1]
   295     17.2 MiB     -0.0 MiB       return result_list   

Использование словаря:
   
Line #    Mem usage    Increment   Line Contents
================================================
   298     16.4 MiB      0.0 MiB   @profile
   299                             def change_list_2(lst):
   300                             
   301     16.4 MiB      0.0 MiB       dict_1 = {}
   302                             
   303     19.3 MiB      3.0 MiB       for i in lst:
   304     19.3 MiB      0.0 MiB           if i not in dict_1:
   305     19.3 MiB      0.0 MiB               dict_1[i] = 1
   306                                     else:
   307     19.3 MiB      0.0 MiB               dict_1[i] +=1
   308     19.9 MiB      0.6 MiB       result_list = [i for i in dict_1 if 
                                                                dict_1[i] == 1]
   309     19.9 MiB      0.0 MiB       return result_list


В данном случае первый метод, с использованием списка, тратит меньше памяти (
для списка из 100000 элементов разница составляет 3 MiB. Однако второй метод 
работает ГОРАЗДО быстрее, замеры я не делала, но если первый отрабатывал 
несколько минут, то второй справился за несколько секунд. Так что, несмотря 
на экономию памяти, второй метод всё же предпочтительнее.
"""
