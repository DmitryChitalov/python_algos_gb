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

import random
from memory_profiler import profile
from collections import namedtuple, defaultdict


@profile()
def search_min_1(num: int) -> int:
    lst = [random.randint(0, num) for i in range(1000)]

    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst[0]


@profile()
def database(user_db: dict, username: str, password: str) -> dict:
    user = (username, password)
    if user in user_db.keys() and user_db[user] == True:
        print(f'Hello {username}')
    elif user in user_db.keys() and user_db[user] == False:
        active = input('Пользовватель не активен, активировать (y/n): ')
        if active == 'y':
            print(f'Hello {username}')
            user_db[user] = True
    else:
        reg = input('Хотите зарегистрироваться? (y/n): ')
        if reg == 'y':
            user_db[user] = False
            print('Учетная запись создана, для активации еще раз войдите в программу')
        else:
            print('До свидания!')
    return user_db  # O(N)




cols = ['first', 'second', 'third', 'fourth']

factory = namedtuple('factory', cols)
factory_dict = defaultdict(int)

factory_dict['factory_1'] = factory(235, 34534, 55, 235)
factory_dict['factory_2'] = factory(345, 34, 543, 34)
factory_dict['factory_3'] = factory(5242, 252, 6512, 11)
factory_dict['factory_4'] = factory(212, 142, 121, 532)
factory_dict['factory_5'] = factory(245, 786, 6567, 22)


@profile()
def average_profit(factory_dict):
    average = 0
    left_average = []
    right_average = []
    for i in factory_dict.values():
        average += sum(i) / len(factory_dict)
    for i, j in factory_dict.items():
        if sum(j) < average:
            left_average.append(i)
        else:
            right_average.append(i)
    return f'Средняя годовая прибыль всех предприятий: {average}. \n' \
           f'Предприятия, с прибылью ниже среднего значения:  {", ".join(left_average)}.\n' \
           f'Предприятия, с прибылью выше среднего значения:  {", ".join(right_average)}'


user_db = {
    ('Bill', '236'): False,
    ('Nik', '123'): True,
}
name = 'Bill'
paswrd = '236'
num = random.randint(0, 100)

search_min_1(num)
database(user_db, name, paswrd)
average_profit(factory_dict)


"""
Line #    Mem usage    Increment   Line Contents
================================================
    22     14.6 MiB     14.6 MiB   @profile()
    23                             def search_min_1(num: int) -> int:
    24     14.6 MiB      0.0 MiB       lst = [random.randint(0, num) for i in range(1000)]
    25                             
    26     14.7 MiB      0.0 MiB       for i in range(len(lst)):
    27     14.7 MiB      0.0 MiB           for j in range(len(lst)):
    28     14.7 MiB      0.0 MiB               if lst[i] < lst[j]:
    29     14.7 MiB      0.0 MiB                   lst[i], lst[j] = lst[j], lst[i]
    30     14.7 MiB      0.0 MiB       return lst[0]


Пользовватель не активен, активировать (y/n): n
Filename: C:/Users/Олег/Desktop/project/geekbrains/python_algos_gb/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    33     14.7 MiB     14.7 MiB   @profile()
    34                             def database(user_db: dict, username: str, password: str) -> dict:
    35     14.7 MiB      0.0 MiB       user = (username, password)
    36     14.7 MiB      0.0 MiB       if user in user_db.keys() and user_db[user] == True:
    37                                     print(f'Hello {username}')
    38     14.7 MiB      0.0 MiB       elif user in user_db.keys() and user_db[user] == False:
    39     14.6 MiB      0.0 MiB           active = input('Пользовватель не активен, активировать (y/n): ')
    40     14.6 MiB      0.0 MiB           if active == 'y':
    41                                         print(f'Hello {username}')
    42                                         user_db[user] = True
    43                                 else:
    44                                     reg = input('Хотите зарегистрироваться? (y/n): ')
    45                                     if reg == 'y':
    46                                         user_db[user] = False
    47                                         print('Учетная запись создана, для активации еще раз войдите в программу')
    48                                     else:
    49                                         print('До свидания!')
    50     14.6 MiB      0.0 MiB       return user_db  # O(N)


Filename: C:/Users/Олег/Desktop/project/geekbrains/python_algos_gb/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    67     14.6 MiB     14.6 MiB   @profile()
    68                             def average_profit(factory_dict):
    69     14.6 MiB      0.0 MiB       average = 0
    70     14.6 MiB      0.0 MiB       left_average = []
    71     14.6 MiB      0.0 MiB       right_average = []
    72     14.6 MiB      0.0 MiB       for i in factory_dict.values():
    73     14.6 MiB      0.0 MiB           average += sum(i) / len(factory_dict)
    74     14.6 MiB      0.0 MiB       for i, j in factory_dict.items():
    75     14.6 MiB      0.0 MiB           if sum(j) < average:
    76     14.6 MiB      0.0 MiB               left_average.append(i)
    77                                     else:
    78     14.6 MiB      0.0 MiB               right_average.append(i)
    79     14.6 MiB      0.0 MiB       return f'Средняя годовая прибыль всех предприятий: {average}. \n' \
    80                                        f'Предприятия, с прибылью ниже среднего значения:  {", ".join(left_average)}.\n' \
    81                                        f'Предприятия, с прибылью выше среднего значения:  {", ".join(right_average)}'
    
    
    Запускалось на Python 3.8 и Windows 10 x64. Нули в инкременте говорят о том, что либо нет узких мест в программе, 
    либо программа оперирует данными небольших размеров.
    """

