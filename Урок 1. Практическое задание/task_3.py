"""
Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
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

# Линейная сложность — O(n)
# Функция схожа с линейной сложностью, так как идет перебор массива для поиска 3 максимальных значений. Количество шагов = количеству элементов в массиве.
# O(n) - в нотации О-большое
def var_1 (dict_obj):
    l_result_dict = {'Первая кампания': 0, 'Вторая кампания': 0, 'Третья кампания': 0}

    for idx in dict_obj:                                           #O(n)
          if l_result_dict.get('Первая кампания') == 0 :
              l_result_dict.update({'Первая кампания': idx})
              continue
          if  l_result_dict.get('Вторая кампания') == 0 :
              l_result_dict.update({'Вторая кампания': idx})
              continue
          if  l_result_dict.get('Третья кампания') == 0 :
              l_result_dict.update({'Третья кампания': idx})
              continue

          if dict_obj.get(idx) > dict_obj.get(l_result_dict.get('Первая кампания')):
              l_result_dict.update({'Третья кампания': l_result_dict.get('Вторая кампания')})
              l_result_dict.update({'Вторая кампания': l_result_dict.get('Первая кампания')})
              l_result_dict.update({'Первая кампания': idx})
              continue
          elif dict_obj.get(idx) > dict_obj.get(l_result_dict.get('Вторая кампания')):
              l_result_dict.update({'Третья кампания': l_result_dict.get('Вторая кампания')})
              l_result_dict.update({'Вторая кампания': idx})
              continue
          elif dict_obj.get(idx) > dict_obj.get(l_result_dict.get('Третья кампания')):
              l_result_dict.update({'Третья кампания': idx})
              continue

    return l_result_dict
# Квадратичная сложность — O(n2)
# Функция схожа с Квадратичной сложностью, так как идет цикл в цикле, из-за этого O(n2)
# O(n2) - в нотации О-большое
def var_2 (dict_obj):
    l_result_dict = {'Первая кампания': 0, 'Вторая кампания': 0, 'Третья кампания': 0}

    for idx in dict_obj:                                     #Один Цикл
      for idx1 in reversed(l_result_dict):                   #Второй цикл внутри первого
         if l_result_dict.get(idx1) == 0:
             l_result_dict.update({idx1: dict_obj.get(idx)})

         if l_result_dict.get(idx1) < dict_obj.get(idx):
             continue
         else:
             l_result_dict.update({idx1: dict_obj.get(idx)})

    return l_result_dict

d = {'NKP1': 1000000000, 'NKP2': 2000000, 'NKP3': 123456778, 'NKP4': 6789034546}

print(var_1(d))
print(var_2(d))

# Как итог, две функции возвращают одинаковое значение кампаний.
# Эффективным решением считаю 2, оно более гибкое, и не настроена на перебор как в первом случае.
