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
from pympler import asizeof
import os, hashlib, urllib3


@profile()
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return 0
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)
        return revers_num


@profile()
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


@profile()
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


num = 123456789

print(asizeof.asizeof(revers(num)))
print(asizeof.asizeof(revers_2(num)))
print(asizeof.asizeof(revers_3(num)))

"""
memory_profiler показывает одинаковый результат для всех трех реализации функции реверса числа.
Для дополнительной проверки решил использовать также функцию asizof из библиотеки pympler, она
показала несколько иной результат, но возможно это связано с рекурсией.
Первые два варианта так же используют одинаковый объем памяти, 
а вот резульатат по третьему варианту в 2,5 раза выше. Поэтому делаю вывод что третий вариант хоть 
и быстрее по скорости работы, но более затратный по объему занимаемой памяти.
Версия интерпретатора Python - 3.8, разрядность ОС - 64 бит.
"""

#######################################################################################

"""
И все-таки меня смущает что memory_profile показывает одинаковый результат, 
поэтому попробую еще на паре скриптов
"""


@profile()
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@profile()
def func_2(nums):
    new_arr = [num for num in nums if num % 2 == 0]
    return new_arr


nums = [num for num in range(1000)]

print(asizeof.asizeof(func_1(nums)))
print(asizeof.asizeof(func_2(nums)))

###############################################################################33


cache_table = {}


@profile()
def cache_check(url):
    content = ''
    hasher = hashlib.new('md5')
    http = urllib3.PoolManager()
    req = http.request('GET', url)
    with open('cache', 'wb+') as f:
        f.write(req.data)
        content = f.read()
        hasher.update((str(content) + url).encode('utf-8'))
        if hasher.hexdigest() not in cache_table:
            cache_table[url] = hasher.hexdigest()
            # ну и здесь тогда можно добавить, например сохранения кэшированного файла в папку кэша
        os.remove('cache')


print(asizeof.asizeof(cache_check('http://rostovmeteo.ru/index.php')))

"""
В общем результат по memory_profile какой-то одинаковый, подозреваю что данные скрипты просто не нагружают
память, есть прирост объема используемой памяти только в последнем скрипте, т.к. видимо происходит схранение 
в память данных http  запроса.
Функция asizeof в общем показывает разные размеры объектов. Самые большие идут в функциях, которые делают массив
из четных элементов, но это из-за того что там большой исходный массив
"""
