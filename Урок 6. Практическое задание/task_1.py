"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов!.
Сделать их разные реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from memory_profiler import profile


@profile
def minimum_search(any_list):
    k = any_list[0]
    for i in range(1, len(any_list)):
        for j in range(1, len(any_list[:])):
            if any_list[i] > any_list[:][j] and any_list[:][j] <= k:
                k = any_list[:][j]
    return k


first_list = [3, 2, 5, 6, 10, 15]
printer = minimum_search(first_list)
print(printer)
print(minimum_search(first_list))

"""Результаты: 
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     3     15.8 MiB     15.8 MiB           1   @profile
     4                                         def minimum_search(any_list):
     5     15.8 MiB      0.0 MiB           1       k = any_list[0]
     6     15.8 MiB      0.0 MiB           6       for i in range(1, len(any_list)):
     7     15.8 MiB      0.0 MiB          30           for j in range(1, len(any_list[:])):
     8     15.8 MiB      0.0 MiB          25               if any_list[i] > any_list[:][j] and any_list[:][j] <= k:
     9     15.8 MiB      0.0 MiB           4                   k = any_list[:][j]
    10     15.8 MiB      0.0 MiB           1       return k

Профилировщик отработал превосходно, нигде прироста затрачиваемой памяти не обнаружено. 
На это влияет то, что программа отработала один раз, также то, что работает она всего с 2 строчками, которые
ввел пользователь. 
Само собой, если бы мы использовали, например, рекурсию и воспользовались ей, например 900 раз,
результаты могли быть другими. 
"""


@profile
def minimum_function(any_list):
    minimum = any_list[0]
    for i in range(1, len(any_list)):
        if any_list[i] < minimum:
            minimum = any_list[i]
    return minimum


print(minimum_function(first_list))
"""Результаты:

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    18     15.8 MiB     15.8 MiB           1   @profile
    19                                         def minimum_function(any_list):
    20     15.8 MiB      0.0 MiB           1       minimum = any_list[0]
    21     15.8 MiB      0.0 MiB           6       for i in range(1, len(any_list)):
    22     15.8 MiB      0.0 MiB           5           if any_list[i] < minimum:
    23     15.8 MiB      0.0 MiB           1               minimum = any_list[i]
    24     15.8 MiB      0.0 MiB           1       return minimum

Здесь всё примерно так же, как и в первой функции: небольшой объем данных, функция
ищет минимум, программа работает один раз с одним списком. 
Поэтому увеличения объема памяти, затраченных на нее, ни в одной строчке нет. 
"""


@profile
def company_searcher(any_dict):
    company_name = []
    maximum = []
    bigest_companies = []
    for i in any_dict.values():
        company_name.append(i)
    for j in [1, 2, 3]:
        maximum.append(max(company_name))
        company_name.remove(max(company_name))
    for i in maximum:
        for k, v in any_dict.items():
            if v == i:
                bigest_companies.append(k)
    return bigest_companies


company_vault = {
    'Ikea': 20000,
    'VK': 100000,
    'Games Workshop': 5000,
    'National Geographic': 3000,
    'Завод консервных банок': 1000
}

"""Результаты: 
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    29     15.8 MiB     15.8 MiB           1   @profile
    30                                         def company_searcher(any_dict):
    31     15.8 MiB      0.0 MiB           1       company_name = []
    32     15.8 MiB      0.0 MiB           1       maximum = []
    33     15.8 MiB      0.0 MiB           1       bigest_companies = []
    34     15.8 MiB      0.0 MiB           6       for i in any_dict.values():
    35     15.8 MiB      0.0 MiB           5           company_name.append(i)
    36     15.8 MiB      0.0 MiB           4       for j in [1, 2, 3]:
    37     15.8 MiB      0.0 MiB           3           maximum.append(max(company_name))
    38     15.8 MiB      0.0 MiB           3           company_name.remove(max(company_name))
    39     15.8 MiB      0.0 MiB           4       for i in maximum:
    40     15.8 MiB      0.0 MiB          18           for k, v in any_dict.items():
    41     15.8 MiB      0.0 MiB          15               if v == i:
    42     15.8 MiB      0.0 MiB           3                   bigest_companies.append(k)
    43     15.8 MiB      0.0 MiB           1       return bigest_companies


Как видно, объем памяти, на разных участках не увеличился, хоть программа и выглядит объемной.
Опять же, работает она всего с одним словарем, в котором 5 значений.
Кроме того, функция ищет 3 максимальных значения заработка компаний.
Иными словами: больших вычислений не производится, объем данных небольшой, отсюда и результаты.   

"""

printer = company_searcher(company_vault)
print(printer)


@profile
def autentificator(login, password):
    total_phrase = None
    activation = None
    users_base = {
        'Todd Howard': 'Bethesda rules',
        'Tim Sweeney': 'We are against apple',
        'Phil Spencer': 'x-box is a future'
    }
    users_activate = {
        'Todd Howard': 'activated',
        'Tim Sweeney': 'deactivated',
        'Phil Spencer': 'deactivated'
    }

    base_len = 0
    for k, v in users_base.items():
        base_len = base_len + 1
        if login == k and password == v:
            for k, v in users_activate.items():
                if login == k:
                    activation = v
            if activation == 'activated':
                total_phrase = "Добро пожаловать, ", login, "!"
            else:
                total_phrase = "Добро пожаловать, ", login, "! Перед входом в систему пройдите активацию."
    if base_len >= 3 and total_phrase == None:
        total_phrase = "Неправильный логин или пароль"

    return total_phrase


login = input("Введите ваш логин: ")
password = input("Введите ваш пароль: ")

autentification = autentificator(login, password)
print(autentification)

"""Результаты: 
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   120     15.8 MiB     15.8 MiB           1   @profile
   121                                         def autentificator(login, password):
   122     15.8 MiB      0.0 MiB           1       total_phrase = None
   123     15.8 MiB      0.0 MiB           1       activation = None
   124     15.8 MiB      0.0 MiB           1       users_base = {
   125     15.8 MiB      0.0 MiB           1           'Todd Howard': 'Bethesda rules',
   126     15.8 MiB      0.0 MiB           1           'Tim Sweeney': 'We are against apple',
   127     15.8 MiB      0.0 MiB           1           'Phil Spencer': 'x-box is a future'
   128                                             }
   129     15.8 MiB      0.0 MiB           1       users_activate = {
   130     15.8 MiB      0.0 MiB           1           'Todd Howard': 'activated',
   131     15.8 MiB      0.0 MiB           1           'Tim Sweeney': 'deactivated',
   132     15.8 MiB      0.0 MiB           1           'Phil Spencer': 'deactivated'
   133                                             }
   134                                         
   135     15.8 MiB      0.0 MiB           1       base_len = 0
   136     15.8 MiB      0.0 MiB           4       for k, v in users_base.items():
   137     15.8 MiB      0.0 MiB           3           base_len = base_len + 1
   138     15.8 MiB      0.0 MiB           3           if login == k and password == v:
   139     15.8 MiB      0.0 MiB           4               for k, v in users_activate.items():
   140     15.8 MiB      0.0 MiB           3                   if login == k:
   141     15.8 MiB      0.0 MiB           1                       activation = v
   142     15.8 MiB      0.0 MiB           1               if activation == 'activated':
   143     15.8 MiB      0.0 MiB           1                   total_phrase = "Добро пожаловать, ", login, "!"
   144                                                     else:
   145                                                         total_phrase = "Добро пожаловать, ", login, "! Перед входом в систему пройдите активацию."
   146     15.8 MiB      0.0 MiB           1       if base_len >= 3 and total_phrase == None:
   147                                                 total_phrase = "Неправильный логин или пароль"
   148                                         
   149     15.8 MiB      0.0 MiB           1       return total_phrase

Тут ровно то же самое: программа работает с двумя строчками, сравнивая значения с двумя словарями.
Делается это один раз, поэтому затраты памяти на разных этапах не увеличиваются.
Скорее всего, с большим объемом данных были бы видны изменения, но с учетом текущих данных ситуация стабильная.
"""
