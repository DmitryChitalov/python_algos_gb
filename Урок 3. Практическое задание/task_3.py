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

def distinct_substring(string):

    result = set()
    result_hash = set()

    # перечислим все подстроки
    for i in range(len(string) + 1):
        for j in range(i + 1, len(string) + 1):
            result.add(string[i:j])
            # добавляем все hash в отдельный Set, сет отсавляет только уникальные значения
            result_hash.add(hashlib.sha256(string[i:j].encode()).hexdigest())

    print(f'уникальные подстроки текстом: {result}')
    print(f'уникальные хеши: {result_hash}')
    return len(result);


input_str = "papa";
print(f'количество уникальных подстрок: {distinct_substring(input_str)}')
