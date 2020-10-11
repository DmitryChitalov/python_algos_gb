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


def determine_substrings(in_str: str):
    str_len = len(in_str)
    hash_list = []
    subst_list = []
    hash_salt = 'Saltyyyyy'.encode('utf-8')
    for i in range(0, str_len):
        for j in range(i, str_len):
            if i == j:
                cur_str = in_str[i]
                cur_hash = hashlib.sha256(cur_str.encode('utf-8') + hash_salt)
                hash_list.append(cur_hash.hexdigest())
                str_prev = ""
            else:
                if not str_prev:
                    cur_str = in_str[i] + str_prev + in_str[j]
                    cur_hash = hashlib.sha256(cur_str.encode('utf-8') + hash_salt)
                    hash_list.append(cur_hash.hexdigest())
                else:
                    cur_str = str_prev + in_str[j]
                    cur_hash = hashlib.sha256(cur_str.encode('utf-8') + hash_salt)
                    hash_list.append(cur_hash.hexdigest())
                str_prev = cur_str
            subst_list.append(cur_str)
    subst_list.remove(in_str)
    return [len(set(hash_list)) - 1, set(subst_list)]


user_str = input("Введите строку: ")

subst_len, subst_list = determine_substrings(user_str)

subst_list_as_str = "\n".join(subst_list)

print(f'Введена строка {user_str}\nКоличество подстрок: {subst_len}\nПодстроки: \n{subst_list_as_str}')
