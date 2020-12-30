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

s = input("vvedite stroku s malenkimi latinskimi bukvami")
n = len(s)
r = set()
for i in range(len(s)):
    if i == 0:
        n = len(s) - 1
    else:
        n = len(s)
    for j in range(n, i, -1):
        print(s[i:j])
        r.add(hashlib.sha256(s[i:j].encode()).hexdigest())

print(r)
print(s, len(r))

