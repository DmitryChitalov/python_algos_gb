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

a = set()
var_str = "papa"
len_val = len(var_str)
len_val_2 = len_val // 2

for i in range(1, len_val):
    for j in range(len_val):
        if j + i > len_val:
            break
        str_tmp = var_str[j:j + i]
        hash_val = hash(str_tmp)
        if hash_val not in a:
            a.add(hash_val)
            print(str_tmp)

print(f"Количество различных подстрок = {len(a)}")
