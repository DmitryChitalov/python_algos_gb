"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""
def max3_1( in_dict, in_count ): # O(N*k) где k - число компаний на выходе
    v_arr = list()
    if len(in_dict) < in_count: in_count = len(in_dict)
    for i in range(in_count):
        v_max = 0
        v_key = ''
        for k in in_dict.keys():
            v_inc = in_dict[k]
            if v_max < v_inc:
                if i > 0 and k != v_arr[i - 1] and v_inc <= in_dict[v_arr[i - 1]]\
                    or i == 0:
                    v_key = k
                    v_max = v_inc
        v_arr.append(v_key)
    print(v_arr)

def max3_2( in_comp, in_inc, in_count ): # O(N^2)
    if len(in_comp) < 2:
        return
    if len(in_comp) != len(in_inc):
        return
    if len(in_comp) < in_count: in_count = len(in_comp)
    for i in range(1,len(in_comp)):
        for j in range(0, i):
            if in_inc[j] > in_inc[i]:
                v_inc = in_inc[j]
                v_key = in_comp[j]
                in_inc[j] = in_inc[i]
                in_inc[i] = v_inc
                in_comp[j] = in_comp[i]
                in_comp[i] = v_key
    for i in range(in_count):
        print( in_comp[len(in_comp)-i-1] + ',')

if __name__ == '__main__':
    v_company_inc = { 'Spacial':12000,
                      'Wasp Engineering':4500,
                      'Interlink':1200,
                      'TrueConnect':22300,
                      'UniMobile':7900,
                      'CallACar':15100,
                      'Leftovers Inc':19700 }

    max3_1(v_company_inc, 3)

    v_company_lst = list(v_company_inc.keys())
    v_company_l_inc = list(v_company_inc.values())

    max3_2(v_company_lst, v_company_l_inc, 3)
# В случае небольших массивов алгоритм, использующий сортировку,
# сравним по времени выполнения с алгоритмом, находящим максимумы.
# В случае больших массивов использование даже быстрой сортировки
# будет заметно медленнее

