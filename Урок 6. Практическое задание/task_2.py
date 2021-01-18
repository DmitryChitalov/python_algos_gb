"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
from memory_profiler import memory_usage
from time import time


def profiler(func):
    def wrapper(*args, **kwargs):
        start_t = time()
        start_m = memory_usage()[0]
        n = func(*args, **kwargs)
        end_t = time()
        end_m = memory_usage()[0]
        return print(f'{func.__name__}:\nTime taken - {end_t - start_t}; Memory usage - {end_m - start_m}; '
                     f'Result - {n}')
    return wrapper


@profiler
def nums_squared_lc(numbers):
    return sum([num**2 for num in numbers])


@profiler
def nums_squared_gc(numbers):
    return sum((num**2 for num in numbers))


for i in [1000, 10000, 1000000]:
    print(f'{str(i) + " elements":-^100}')
    num_lc = nums_squared_lc(range(i))
    num_gc = nums_squared_gc(range(i))


"""
-------------------------------------------1000 elements--------------------------------------------
nums_squared_lc:
Time taken - 0.10935330390930176; Memory usage - 0.0703125; Result - 332833500
nums_squared_gc:
Time taken - 0.10937166213989258; Memory usage - 0.00390625; Result - 332833500
-------------------------------------------10000 elements-------------------------------------------
nums_squared_lc:
Time taken - 0.10942864418029785; Memory usage - 0.375; Result - 333283335000
nums_squared_gc:
Time taken - 0.10936331748962402; Memory usage - 0.0; Result - 333283335000
------------------------------------------1000000 elements------------------------------------------
nums_squared_lc:
Time taken - 0.42179298400878906; Memory usage - 1.3203125; Result - 333332833333500000
nums_squared_gc:
Time taken - 0.43747544288635254; Memory usage - 0.0; Result - 333332833333500000

Как видно из приведенных выше замеров - использование генераторов действительно значительно сокращает использование 
памяти, при этом с увеличением длины массива необходимого для работы - объем памяти не увеличивается, а время 
выполнения операции сопоставимо с обычным проходом по списку. 
"""
