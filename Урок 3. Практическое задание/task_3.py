"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""

import hashlib

s = 'rara'
my_lst = []

for x in range(0, len(s), 1):
    # вытаскиваем подстроки, исходя из того, что len(s) - 4:
    lst_1 = s[x:x+1]
    lst_2 = s[x:x+2]
    lst_3 = s[x:x+3]
    for el in (lst_1, lst_2, lst_3):
        my_lst.append(el)

# убираем одинаковые, оставляем уникальные:
my_set = set(my_lst)
print(my_set)


def hash_gen(str):
    # получаем хеши из подстрок:
    hash_lst = []
    for s in str:
        hash_obj = hashlib.sha1((s).encode('utf-8'))
        result = hash_obj.hexdigest()
        hash_lst.append(result)
    return hash_lst

print(len(hash_gen(my_set)))
