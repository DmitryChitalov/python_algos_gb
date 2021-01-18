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

'''Из задания 4 урока 1'''
from memory_profiler import profile
user_info = {'login':'olya', 'pass':'123', 'activated': True}


@profile
def test_1(my_login, my_pass, my_activated):
    if my_activated == True:
        if my_login != user_info.get('login') or my_pass != user_info.get('pass'):
            print('Невнрный логин или пароль!')
        else:
            print('Вы вошли в систему!')
    else:
        print('Активируйте профиль!')

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     29     18.6 MiB     18.6 MiB           1   @profile
#     30                                         def test_1(my_login, my_pass, my_activated):
#     31     18.6 MiB      0.0 MiB           1       if my_activated == True:
#     32     18.6 MiB      0.0 MiB           1           if my_login != user_info.get('login') or my_pass != user_info.get('pass'):
#     33                                                     print('Невнрный логин или пароль!')
#     34                                                 else:
#     35     18.6 MiB      0.0 MiB           1               print('Вы вошли в систему!')
#     36                                             else:
#     37                                                 print('Активируйте профиль!')

@profile
def test_2(my_info):
    if my_info == user_info and my_info.get('activated') is not False:
        print('Вы вошли в систему!')
    elif my_info.get('activated') is False:
        print('Активируйте профиль!')
    else:
        print('Невнрный логин или пароль!')


# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     45     18.6 MiB     18.6 MiB           1   @profile
#     46                                         def test_2(my_info):
#     47     18.6 MiB      0.0 MiB           1       if my_info == user_info and my_info.get('activated') is not False:
#     48     18.6 MiB      0.0 MiB           1           print('Вы вошли в систему!')
#     49                                             elif my_info.get('activated') is False:
#     50                                                 print('Активируйте профиль!')
#     51                                             else:
#     52                                                 print('Невнрный логин или пароль!')

# if __name__ == "__main__":
#     test_1('olya', '123', True)
#     test_2({'login': 'olya', 'pass': '123', 'activated': True})

# результаты совершенно одинаковые. Память расходуется только на создание функции, дальше в обоих случаях расхода
# памяти нет. Значит, с точки зрения памяти, обе функции одинакого хороши.


'''Из задания 3 урока 1 взяла два срипта и обернула их в функции.'''

companies_revenue = {'Royal Dutch Shell': 311600, 'State Grid': 387000, 'Walmart': 524000,  'Toyota': 280500,
                      'Sinopec Group': 369200, 'BR': 278400, 'China National Petroleum': 364100, 'Volkswagen': 275200,
                      'Saudi Aramco': 329800, 'Exxon Mobil': 265700}

@profile
def top_1(companies_revenue):
    names = tuple(companies_revenue.keys())
    money = list(companies_revenue.values())
    money_save = money.copy()
    max_money = list()
    for i in range(3):
        max_money.append(max(money))
        money.remove(max(money))
    for i in max_money:
        index_name = money_save.index(i)
    rezult = names[index_name]
    return rezult

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     86     18.6 MiB     18.6 MiB           1   @profile
#     87                                         def top_1(companies_revenue):
#     88     18.6 MiB      0.0 MiB           1       names = tuple(companies_revenue.keys())
#     89     18.6 MiB      0.0 MiB           1       money = list(companies_revenue.values())
#     90     18.6 MiB      0.0 MiB           1       money_save = money.copy()
#     91     18.6 MiB      0.0 MiB           1       max_money = list()
#     92     18.6 MiB      0.0 MiB           4       for i in range(3):
#     93     18.6 MiB      0.0 MiB           3           max_money.append(max(money))
#     94     18.6 MiB      0.0 MiB           3           money.remove(max(money))
#     95     18.6 MiB      0.0 MiB           4       for i in max_money:
#     96     18.6 MiB      0.0 MiB           3           index_name = money_save.index(i)
#     97     18.6 MiB      0.0 MiB           1       rezult = names[index_name]
#     98     18.6 MiB      0.0 MiB           1       return rezult


@profile
def top_2(companies_revenue):
    sort_names = (
        sorted(companies_revenue, key=companies_revenue.get, reverse=True))
    rezult = sort_names[0:3]
    return rezult

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#    101     18.6 MiB     18.6 MiB           1   @profile
#    102                                         def top_2(companies_revenue):
#    103                                             sort_names = (
#    104     18.6 MiB      0.0 MiB           1      sorted(companies_revenue, key=companies_revenue.get, reverse=True))
#    105     18.6 MiB      0.0 MiB           1       rezult = sort_names[0:3]
#    106     18.6 MiB      0.0 MiB           1       return rezult


# if __name__ == "__main__":
#     top_1(companies_revenue)
#     top_2(companies_revenue)

# И опять затраты памяти одинаковые, и паменять используется только на создание фунции, оба способа одинаково
# оптимальны. Поищу еще пример, чтобы было, что поанализировать...

'''Из задания 4 урока 4'''

# array = [1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 3, 4, 5, 1, 1, 3, 1, 3, 3, 1, 3, 4, 5, 1, 3, 4, 5, 1]

from random import randint
array = [randint(-10, 10) for i in range(10000)]

@profile
def func_1(array):
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#    148     18.9 MiB     18.9 MiB           1   @profile
#    149                                         def func_1(array):
#    150     18.9 MiB      0.0 MiB           1       m = 0
#    151     18.9 MiB      0.0 MiB           1       num = 0
#    152     18.9 MiB      0.0 MiB       10001       for i in array:
#    153     18.9 MiB      0.0 MiB       10000           count = array.count(i)
#    154     18.9 MiB      0.0 MiB       10000           if count > m:
#    155     18.9 MiB      0.0 MiB           4               m = count
#    156     18.9 MiB      0.0 MiB           4               num = i
#    157     18.9 MiB      0.0 MiB           1       return f'Чаще всего встречается число {num}, ' \
#    158                                                    f'оно появилось в массиве {m} раз(а)'

@profile
def func_2(array):
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)
    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#    161     18.9 MiB     18.9 MiB           1   @profile
#    162                                         def func_2(array):
#    163     18.9 MiB      0.0 MiB           1       new_array = []
#    164     19.2 MiB      0.0 MiB       10001       for el in array:
#    165     19.2 MiB      0.0 MiB       10000           count2 = array.count(el)
#    166     19.2 MiB      0.3 MiB       10000           new_array.append(count2)
#    167     19.2 MiB      0.0 MiB           1       max_2 = max(new_array)
#    168     19.2 MiB      0.0 MiB           1       elem = array[new_array.index(max_2)]
#    169     19.2 MiB      0.0 MiB           1       return f'Чаще всего встречается число {elem}, ' \
#    170                                                    f'оно появилось в массиве {max_2} раз(а)'

@profile
def func_3(array):
    counts = {array.count(el): el for el in array}
    m = max(counts.keys())
    num = counts.get(m)
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#    173     19.1 MiB     19.1 MiB           1   @profile
#    174                                         def func_3(array):
#    175     19.1 MiB      0.0 MiB       10003       counts = {array.count(el): el for el in array}
#    176     19.1 MiB      0.0 MiB           1       m = max(counts.keys())
#    177     19.1 MiB      0.0 MiB           1       num = counts.get(m)
#    178     19.1 MiB      0.0 MiB           1       return f'Чаще всего встречается число {num}, ' \
#    179                                                    f'оно появилось в массиве {m} раз(а)'

@profile
def func_4(array):
    numb = max(array, key=array.count)
    return f"Чаще всего встречается число {numb}, оно появилось в массиве {array.count(numb)} раз(а)"

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#    182     19.1 MiB     19.1 MiB           1   @profile
#    183                                         def func_4(array):
#    184     19.1 MiB      0.0 MiB           1       numb = max(array, key=array.count)
#    185     19.1 MiB      0.0 MiB           1       return f"Чаще всего встречается число {numb}, оно появилось в массиве {array.count(numb)} раз(а)"


if __name__ == "__main__":
    func_1(array)
    func_2(array)
    func_3(array)
    func_4(array)

# Итого:
# 1 - 18.9 MiB
# 2 - 19.2 MiB
# 3 - 19.1 MiB
# 4 - 19.1 MiB
# В случаях 1, 3 и 4 память тратиться только при создании функции, значит эти способы оптимальнее.
# При этом, у 1ой функции на это уходит меньше памяти, но я не понимаю, почему( Во варианте 2 на создание функции
# уходит столько же памяти, сколько и в 1ом варианте, но при этом идет прирост памяти на 0.3 потому что внутри функции
# мы создаем новый массив с количеством элементов, равным количеству элементов нашего исходного массива.
# Очевидно, это и должно отнимать память. Таким образом, 2ой вариант самый Не оптимальный, а 1ый - самый оптимальный.
