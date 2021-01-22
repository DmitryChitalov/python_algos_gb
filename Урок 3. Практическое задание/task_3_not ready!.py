"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""
# 3 ЗАДАНИЕ В ПРОЦЕССЕ ВЫПОЛНЕНИЯ

# d = 'papa'
# print(d[1:1+1])
# print(d[0:0+2])
# print(d[0:0+3])
# print(d[0:0+4])
# print(d[0:0+5])  # почему здесь нет error? индексы ведь кончились

# НЕ МОЙ КОД, Я ЕГО РАЗБИРАЮ ПО ЧАСТЯМ.
# def all_substr(s):
#     l = len(s)
#     return set([s[b:b + a] for a in range(1, l) for b in range(l + 1 - a)])
#
# print(all_substr('papa'))
#
# test_str = 'papa'
# for sub in all_substr(test_str):
#     print(sub)
# #

# for i in string:
#     a.append(i)
#
#
#

# ПРОСТО ПОРАБОТАЛ С ИНДЕКСАМИ
# a = 'papa'
# for i in range(len(a)):
#     if i < len(a)-1:
#         print(i, len(a)-1)
#         if a[i] != a[i+1]:
#             print('not equal',a[i], a[i+1])
#             b.append(a[i])
#         else:
#             print('equal',a[i], a[i+1])
#             c.append(a[i])
#
#
# print(a)
# print(b)