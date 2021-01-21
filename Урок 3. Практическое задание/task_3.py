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
result_set = set()
s = 'verylongstring'
for sym in range(len(s)):
    last_str = s[sym:]
    for length in range(1, len(last_str) + 1):
        sub_str = s[sym:sym + length]
        if s != sub_str:
            hash_sub_str = hash(sub_str)
            result_set.add(hash_sub_str)

print(len(result_set))
