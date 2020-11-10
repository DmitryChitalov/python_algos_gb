"""
Задание 2.
Предложить еще какие-гибудь варианты (механизмы, библиотеки) оптимизации и
доказать (наглядно, кодом) их эффективность
"""

"""
Нашел что вроде как замена циклов for на функции map, filter и reduce уменьшает количество используемой 
памяти, но профилировщики этого не показывают. Так же рекомендуют по возможности пользоваться 
интерпритатором PyPy, использовать локальные переменные вместо глобальных.
И вот тут есть несколько дельных советов https://academy.yandex.ru/posts/python-prostye-no-poleznye-sovety-po-optimizatsii-koda
"""

from memory_profiler import profile
from functools import reduce
from pympler import asizeof

numbers = [num for num in range(1000)]


# вычисление суммы квадратов нечетных чисел в списке
@profile()
def sum_squ_odd_num(numbers):
    odd_numbers = []
    squared_odd_numbers = []
    total = 0
    for number in numbers:
        if number % 2 == 1:
            odd_numbers.append(number)
    for number in odd_numbers:
        squared_odd_numbers.append(number * number)
    for number in squared_odd_numbers:
        total += number
    return total


@profile()
def sum_squ_odd_num2(numbers):
    odd_numbers = filter(lambda n: n % 2 == 1, numbers)
    squared_odd_numbers = map(lambda n: n * n, odd_numbers)
    total = reduce(lambda acc, n: acc + n, squared_odd_numbers)
    return total


print(asizeof.asizeof(sum_squ_odd_num(numbers)))
print(asizeof.asizeof(sum_squ_odd_num2(numbers)))
