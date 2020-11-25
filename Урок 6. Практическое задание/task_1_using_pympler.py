'''
Пример использования библиотечки pympler
'''

from pympler import tracker



def sum_value_func(max_value):
    sum_value = 0
    for el in range(max_value):
        sum_value += el**el
        print(f'value is: {el}')
        print(f'Sum value is: {sum_value}')
    return sum_value

print('Program "Memory usage types, count objects, and their total memory size with using lib pympler"')
track = tracker.SummaryTracker() # Общая аналитика
sum_value_func(100)
track.print_diff() # Распечатка отличий

'''
Получаем число объектов, их типы и память, которые они занимают

                  types |   # objects |    total size
======================= | =========== | =============
                    str |        4051 |     186.80 KB
                   list |        4066 |     175.36 KB
                    int |         312 |       4.29 KB
                   dict |           3 |     228     B
                   code |           0 |      70     B
  function (store_info) |           1 |      68     B
                   cell |           2 |      40     B
                 method |           1 |      32     B
                  float |          -2 |     -32     B
                  tuple |         -32 |   -1140     B
'''
