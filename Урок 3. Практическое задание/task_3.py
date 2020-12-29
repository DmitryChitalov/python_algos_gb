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

s = 'papa'
substrings = set()

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        srez = hashlib.md5(s[i:j].encode()).hexdigest()
        # if srez !=s : # Никак не пойму, как сделать так, чтобы вcя строка нe бралась тоже.
        # Если убираю +1 от len(s)+1, то теряю значение...
        substrings.add(srez)

substrings.remove(hashlib.md5(s.encode()).hexdigest())  # Наверное, с точки зрения оптимизации так лучше, чем лишний if
print(substrings)
print(f'В строке {len(substrings)} уникальных подстрок.')
