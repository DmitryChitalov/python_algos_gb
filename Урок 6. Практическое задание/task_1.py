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
from collections import namedtuple
from timeit import default_timer
from memory_profiler import memory_usage
from random import randint

"""
Первый скрипт для анализа:
"Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."
"""


def memory_with_time_profiler(func_obj):
    def wrapper(*args, **kwargs):
        average_memory = []
        average_time = []
        for num in range(10):
            start_memory = memory_usage()
            start_time = default_timer()
            func_obj(args[0], args[1], args[2], args[3], args[4], args[5])
            end_time = default_timer()
            end_memory = memory_usage()
            average_time.append(end_time - start_time)
            average_memory.append(end_memory[0] - start_memory[0])

        print(f'Среднее время работы функции за 10 запусков: {sum(average_time) / 10} cек')
        print(f' Среднее количество использованной памяти за 10 запусков: {sum(average_memory) / 10} Mib')
        print('\n')
    return wrapper


@memory_with_time_profiler
def generation_user_info(name, surname, year_of_birth, city_of_residence, email, phone_number):
    user_info = {"name": name, "surname": surname, "year_of_birth": year_of_birth,
                 "city_of_residence": city_of_residence, "email": email, "phone_number": phone_number}
    return user_info


@memory_with_time_profiler
def generation_user_info_with_optimization(name, surname, year_of_birth, city_of_residence, email, phone_number):
    USER_INFO = namedtuple('Profile', 'name surname year_of_birth city_of_residence email phone_number')
    filled_user_info = USER_INFO(
        name=name,
        surname=surname,
        year_of_birth=year_of_birth,
        city_of_residence=city_of_residence,
        email=email,
        phone_number=phone_number
    )
    return filled_user_info


"""
Второй скрипт для анализа:
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""


def memory_with_time_profiler2(func_obj):
    def wrapper(*args, **kwargs):
        average_memory = []
        average_time = []
        for num in range(10):
            start_memory = memory_usage()
            start_time = default_timer()
            func_obj(args[0])
            end_time = default_timer()
            end_memory = memory_usage()
            average_time.append(end_time - start_time)
            average_memory.append(end_memory[0] - start_memory[0])

        print(f'Среднее время работы функции за 10 запусков: {sum(average_time) / 10} cек')
        print(f' Среднее количество использованной памяти за 10 запусков: {sum(average_memory) / 10} Mib')
        print('\n')
    return wrapper


@memory_with_time_profiler2
def get_result_with_generate(num_list):
    def get_result_elem(num_list):
        for num in range(1, len(num_list)):
            if num_list[num] > num_list[num - 1]:
                yield num_list[num]

    return list(get_result_elem(num_list))


@memory_with_time_profiler2
def get_result_with_cycle(num_list):
    result = []
    for num in range(1, len(num_list)):
        if num_list[num] > num_list[num - 1]:
            result.append(num_list[num])
    return result


@memory_with_time_profiler2
def get_result_with_list_comprehension(num_list):
    return [num_list[num] for num in range(1, len(num_list)) if num_list[num] > num_list[num - 1]]


if __name__ == "__main__":
    user_name = 'Наталья'
    user_surname = 'Комарова'
    user_birth = 1989
    user_city = 'Москва'
    user_email = 'shadowx110@yandex.ru'
    user_phone = 9161137975
    print('Анализ эффективности времени и памяти для функции generation_user_info')
    user_information = generation_user_info(user_name,
                                            user_surname,
                                            user_birth,
                                            user_city,
                                            user_email,
                                            user_phone
                                            )
    print('Анализ эффективности времени и памяти для функции generation_user_info_with_optimization')
    user_information_2 = generation_user_info_with_optimization(
        user_name,
        user_surname,
        user_birth,
        user_city,
        user_email,
        user_phone
    )
    test_list = [randint(-100, 100) for _ in range(1000000)]
    print('Анализ эффективности времени и памяти для функции get_result_with_list_comprehension')
    get_result_with_list_comprehension(test_list)
    print('Анализ эффективности времени и памяти для функции get_result_with_generate')
    get_result_with_generate(test_list)
    print('Анализ эффективности времени и памяти для функции get_result_with_cycle')
    get_result_with_cycle(test_list)

"""
Выводы:
1. Анализ затрат времени и памяти двух функций первого задания показал, что функция, использующая словарь, для 
хранения данных быстрее, чем функция, использующая именованый кортеж. Следовательно оптимизация в этом случае 
не принесла положительных результатов в рамках решения задачи.
2. Анализ затрат памяти и времени во втором задании показал, что:
    - функция, использующая list comprehension быстрее двух других, но более затратна по использованию памяти
    - функции, использующие цикл и генератор, для решения используют меньше памяти, но работают медленнее.
"""
