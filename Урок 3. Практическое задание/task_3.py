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


def f_uniq_count(v_str):
    v_len = len(v_str)
    v_set = set()
    for i in range(v_len):
        for j in range(i + 1, v_len + 1):
            if len(v_str[i:j]) < v_len:
                v_set.add(hash(v_str[i:j]))
    return len(v_set)


while True:
    print(
        f"количество различных подстрок : {f_uniq_count(input('введите строку состоящую только из строчных латинских букв >>> '))}")
