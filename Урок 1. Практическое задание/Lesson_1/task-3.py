Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.	Выведите результат.
"""	"""
'''Решение 1 сложность O(n log n)
Сложность решения - линейно логарифмическая, поскольку самая сложная операция sorted, дающая линейно логарифмическую сложность. 
Остальные операции - константная сложность. 
'''
def search_max_1(dict_companys):
    return sorted(dict_companys.items(), key=lambda x: x[1], reverse=True)[:3]

''' Решение 2 сложность O(n)
Сложность решения - линейная, поскольку самая сложная операция - цикл for in, сложность которого 
прямопропорциональна размеру входящих данных. 
Так же есть линейно логарифмическая (sorted), остальные операции - константной сложности.
'''
def search_max_2(dict_companys):
    i = 1
    print('Второй вариант: ', end='')
    for item in sorted(dict_companys, key=dict_companys.get, reverse=True):
        print(item, dict_companys[item], end=' ')
        i += 1
        if i > 3:
            break
    return print()

dict_companys = {'Region': 10000, 'Numbers': 2000, 'Resources': 3000, 'Dynamics': 500}

max_1 = search_max_1(dict_companys)
print(f'Первый вариант: {max_1}')

max_2 = search_max_2(dict_companys)