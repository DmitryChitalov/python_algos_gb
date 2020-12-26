"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
арpap
ара
р
а
"""
import hashlib

S = input("Введите строку : ")

print("Строка \'%s\' имеет длину %d сиволов." % (S, len(S)))
S = hashlib.sha256(S.strip().encode('utf-8'))
S = S.hexdigest()

subs_set = set()
for i in range(len(S)):
    for j in range(len(S) - 1 if i == 0 else len(S), i, -1):
        subs_set.add((S[i:j]))

print("Количество различных подстрок в этой строке:", len(subs_set))
print(subs_set)
