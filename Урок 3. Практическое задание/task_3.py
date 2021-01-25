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
# код писал - анализируя разбор дз
import hashlib

s = input('Enter the string: ').lower()
r = set()

N = len(s)
for i in range(N):
    if i == 0:
        N = len(s) - 1
    N = len(s)

    for j in range(N, i, -1):
        print(s[i:j])
        r.add(hashlib.sha256(s[i:j].encode('utf-8')).hexdigest())

print(r)
print(f'in string "{s}", number of substrings = {len(r)}')