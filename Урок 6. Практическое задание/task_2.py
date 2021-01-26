"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""

import memory_profiler as mp
import timeit


def my_third_decorator(func):
    def wrapper():
        time_start = timeit.default_timer()
        start_point = mp.memory_usage()
        x = func()
        end_point = mp.memory_usage()
        time_end = timeit.default_timer()
        print(f"Памяти занято {end_point[0] - start_point[0]} MiB, время работы {time_end - time_start} сек")
        return x
    return wrapper


@my_third_decorator
def create_list():
    my_list = []
    for i in range(10000):
        my_list.append(i)
    return my_list


data_list = create_list()


def my_gen():
    for i in range(10000):
        yield i


time_start = timeit.default_timer()
start_point = mp.memory_usage()
gen_list = [x for x in my_gen()]
end_point = mp.memory_usage()
time_end = timeit.default_timer()
print(f"Памяти занято после оптимизации "
      f"{end_point[0] - start_point[0]} MiB, время работы {time_end - time_start} сек")

"""
Создание списка из 10000 элементов заняло 0.5234375 MiB через цикл for и 0.30078125 MiB через генератор
"""

time_start = timeit.default_timer()
start_point = mp.memory_usage()

print('Hello' + ", World" + "!")

end_point = mp.memory_usage()
time_end = timeit.default_timer()
print(f"Памяти занято до оптимизации {end_point[0] - start_point[0]} MiB, время работы {time_end - time_start} сек")

time_start = timeit.default_timer()
start_point = mp.memory_usage()

a = 'Hello,'
b = 'World'
c = '!'
print(f"{a}{b}{c}")


end_point = mp.memory_usage()
time_end = timeit.default_timer()
print(f"Памяти занято после оптимизации  методом f-строки "
      f"{end_point[0] - start_point[0]} MiB, время работы {time_end - time_start} сек")

time_start = timeit.default_timer()
start_point = mp.memory_usage()

a = 'Hello,'
b = 'World'
c = '!'
print("{}{}{}".format(a, b, c))


end_point = mp.memory_usage()
time_end = timeit.default_timer()
print(f"Памяти занято после оптимизации методом .format "
      f"{end_point[0] - start_point[0]} MiB, время работы {time_end - time_start} сек")

"""
Использовать f-строки или .format для оптимизаци памяти при выводе строк
"""