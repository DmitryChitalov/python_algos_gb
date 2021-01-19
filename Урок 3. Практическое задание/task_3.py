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


def all_un_sub(str_in):
    res = [str_in[i: j] for i in range(len(str_in))
           for j in range(i + 1, len(str_in) + 1)]
    res_hash = set(map(lambda x: hash(x), res))
    return len(res_hash)


if __name__ == '__main__':
    print(all_un_sub('рара'))


