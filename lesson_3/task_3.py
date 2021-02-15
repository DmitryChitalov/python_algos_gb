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

S = str(input("Введите строку S: "))
# S = 'papa'
N = len(S)
slice_set = set()

for i in range(N):
    for j in range(N - 1 if i == 0 else N, i, -1):
        sh = hashlib.sha256(S[i:j].encode('utf-8')).hexdigest()
        sh = S[i:j]
        slice_set.add(sh)

print("Количество различных подстрок в этой строке:", len(slice_set))

print(slice_set)
