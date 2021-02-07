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

def sub_strs (S):
    subs = set()
    for i in range(len(S)):
        if i == 0:
            curr_len = len(S) - 1
        else:
            curr_len = len(S)
        for j in range(curr_len, i, -1):
            subs.add(sha256(S[i:j].encode()).hexdigest())
    return len(subs)

word = "test"
print(f"Количество подслов в слове {word} - {sub_strs(word)}")
