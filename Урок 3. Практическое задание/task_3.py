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
from hashlib import sha1

S = input('Введите строку из строчных латинских букв: ')
N = len(S)
hash_set = set()

for i in range(N):
    for j in range(N, i, -1):
        substr = S[i:j]
        if substr == S:
            continue
        print(substr)
        hash_set.add(sha1(substr.encode()).hexdigest())
print(hash_set)
print(f'В строке "{S}" {len(hash_set)} различных подстрок')

