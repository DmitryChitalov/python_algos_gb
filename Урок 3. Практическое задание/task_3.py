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


def get_count_substrings(str_obj):
    substrings = set()
    new_str = str_obj.strip().lower()
    len_new_str = len(new_str)
    for num_letter_1 in range(len_new_str):
        if num_letter_1 == 0:
            len_new_str = len(new_str) - 1
        else:
            len_new_str = len(new_str)
        for num_letter_2 in range(len_new_str, num_letter_1, -1):
            substring = new_str[num_letter_1:num_letter_2]
            print(substring)
            substrings.add(hashlib.sha256(substring.encode('utf-8')).hexdigest())
    return substrings, len(substrings)


if __name__ == '__main__':
    substrings, count_substrings = get_count_substrings('papa')
    for substring in substrings:
        print(substring)
    print(count_substrings)







