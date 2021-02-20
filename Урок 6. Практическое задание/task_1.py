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


"""
	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""
import time
import memory_profiler


def time_and_memory(func):
    
    def wrapper():
        t1 = time.process_time()
        m1 = memory_profiler.memory_usage() # левые отсечки времени и памяти
        res = func()
        t2 = time.process_time()
        m2 = memory_profiler.memory_usage()
        print(f"Время выполения, {t2-t1}, Затраты памяти, {m2[0]-m1[0]}")
        return res
    
    return wrapper

# решение церез цикл

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

#@profile
@time_and_memory
def even_digits():
    """ считает четные цифры"""   
    a = input("Введите целое число \n")
    dl = list(a)
    cnt = [] # счетчик

    while dl != [] :
        val = int(dl.pop(0))
        if is_even(val):
            cnt.append(val)

    return cnt
# рекурсия

def even_rec(a, vl = []):
    """ получаем число в виде массива"""
    if a != [] :
        if is_even(int(a[0])):
            vl.append(int(a.pop(0)))
            return  even_rec(a,vl)
        else:
            a.pop(0)
            return even_rec(a,vl)
    return vl

# Замер времмени и выделения памяти

#@profile
@time_and_memory
def count_even():
    """ Функция-обертка для рекурсии"""
    a = list(input("Ввведите целое число: \n"))
    return even_rec(a)


if __name__ == '__main__':
    @memory_profiler.profile
    def mainloop():
        print(even_digits())
        print(count_even())
        return
    mainloop()

"""
Запуск программ проходит в среде repl.it для каждого репозитория выделяется образ на Кубернетс, его параметры:
Процессор 
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              4
Model name:          Intel(R) Xeon(R) CPU @ 2.30GHz
Stepping:            0
CPU MHz:             2299.998
Тоесть 64 разрадный интел Xeon 4-х ядерный 3300 MHz
Система Убунту
VERSION="18.04.5 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.5 LTS"
VERSION_ID="18.04"

результаты профилировки
python3 'Урок 6. Практическое задание/task_1.py'
Введите целое число 
1234556
Время выполения, 0.0016899540000000213, Затраты памяти, 0.0
[2, 4, 6]
Ввведите целое число: 
1234566
Время выполения, 0.002306611000000014, Затраты памяти, 0.0
[2, 4, 6, 6]
Filename: Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    89     17.1 MiB     17.1 MiB           1       @memory_profiler.profile
    90                                             def mainloop():
    91     17.1 MiB      0.0 MiB           1           print(even_digits())
    92     17.1 MiB      0.0 MiB           1           print(count_even())
    93     17.1 MiB      0.0 MiB           1           return

Замеры с помощью декоратора и profile показывают отсутствие выделения памяти. Вероятно ввиду малого объема данных выделение дополнительного объема памяти не потребовалось.
В моем случае для profile выделено 17.1 MiB в примере 16 MiB.
Замеры времени выполнения показывают, что рекурсия более затратный способ

"""