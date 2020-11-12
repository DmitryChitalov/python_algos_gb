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

from hashlib import sha256

a = 'papa'
c = set()

for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i:j + 1] == a: break
        c.add(sha256(a[i:j + 1].encode()).hexdigest())

for i in c: print(i)

# решил не удалять первоеое решение

# b = set()

# for i in range(len(a)):
#     obj_hash = sha256(a[i].encode())
#     temp = a[i]
#     b.add(obj_hash.hexdigest())
#     for j in a[i + 1:]:
#         temp += j
#         if temp == a:break
#         obj_hash = sha256(temp.encode())
#         b.add(obj_hash.hexdigest())
#
# for i in b:
#     print(i)


