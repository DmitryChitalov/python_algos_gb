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

def get_unique_set(i_str):
    l_len = len(i_str)
    l_uns = set()

    for ln in range(1, l_len+1):
        if ln == l_len:
            break
        for jm in range(0, l_len):
            l_fin = jm+ln
            if l_fin > l_len:
                break
            l_sub_str = i_str[jm:jm+ln]
            #print(l_sub_str, hash(l_sub_str))
            l_found = False
            for rec in l_uns:
                if hash(rec) == hash(l_sub_str):
                    l_found = True
                    break
            if not l_found:
                l_uns.add(l_sub_str)
    return l_uns


print(get_unique_set('papa'))
