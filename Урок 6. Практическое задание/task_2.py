"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
from memory_profiler import memory_usage
from numpy import array
from pympler import asizeof
from time import process_time


def runtime(func):
    def wrapper(*args):
        t1 = process_time()
        m1 = memory_usage()
        result = func(*args)
        t2 = process_time()
        m2 = memory_usage()
        print(f'Выполнение заняло {t2 - t1} сек и {m2[0] - m1[0]} MiB.')
        return result
    return wrapper


def runtime_2(func):
    def wrapper(*args):
        t1 = process_time()
        m1 = memory_usage()
        result = list(func(*args))
        t2 = process_time()
        m2 = memory_usage()
        print(f'Выполнение заняло {t2 - t1} сек и {m2[0] - m1[0]} MiB.')
        return result
    return wrapper


@runtime
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@runtime
def func_2(nums):
    return [i for id, i in enumerate(nums) if i % 2 == 0]


@runtime
def func_3(nums):
    return list(filter(lambda x: x % 2 == 0, nums))


@runtime_2
def func_4(nums):
    for i in nums:
        if i % 2 == 0:
            yield i


n = array([i for i in range(1000000)])
print(asizeof.asizeof(n))  # 4000048 байт
func_1(n)  # Выполнение заняло 0.75 сек и 9.20703125 MiB.
func_2(n)  # Выполнение заняло 0.65625 сек и 9.41015625 MiB.
func_3(n)  # Выполнение заняло 0.640625 сек и 9.359375 MiB.
func_4(n)  # Выполнение заняло 0.546875 сек и 9.34765625 MiB.

"""
Для замеров создал 2 декоратора, для функции с генератором отдельный, чтобы функция возвращала список как остальные.
В итоге доказательства не вышло, т.к. по результатам все 4 функции используют примерно одинаковое количество памяти.
Таким образом делаю вывод, что генератор рационально использовать, пока используем его в ходе вычислений,
если хотим сохранить результат сформированного генератором списка, то преимущество перед другими вариантами отсутствует.

Использование array из библиотеки numpy, дает отличное преимущество по памяти.
Для списка из 1 млн. элементов - 3,8 Мб, против 19,4 Мб при создании обычного списка.
"""
