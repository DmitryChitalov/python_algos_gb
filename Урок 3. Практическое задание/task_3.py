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


def count_substrings(s):
    bag = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            bag.add(hash(s[i:j]))
    return len(bag)-1


for s in ("bbbb", "baba", "bcde"):
    print(f"{s} -> {count_substrings(s)}")

# ---output---
# bbbb -> 3
# baba -> 6
# bcde -> 9
