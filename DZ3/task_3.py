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

S = input("Введите строку из маленьких латинских букв: ")
container = set()

N = len(S)
for i in range(N):
    if i == 0:
        N = len(S) - 1
    else:
        N = len(S)
    for j in range(N, i, -1):
        print(S[i:j])
        container.add(hashlib.sha1(S[i:j].encode('utf-8')).hexdigest())
print(container)

print(f"Количество различных подстрок равно {len(container)}")
