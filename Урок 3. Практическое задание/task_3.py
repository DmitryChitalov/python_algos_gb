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


def cut_string(my_str):
    hlist = []
    rlist = []
    l = len(my_str) + 1
    for i in range(l):
        for j in range(l):
            under_str = my_str[i:j]
            if under_str != '' and under_str != my_str:
                hlist.append(hashlib.sha256(under_str.encode()).hexdigest())
                rlist.append(under_str)
    # uniqs = len(list(set(reslt.keys())))
    return rlist, hlist


def count_set(my_str):
    my_str = cut_string(my_str)[0]
    uniqs = len(list(set(my_str)))
    return uniqs


def count_hash(my_str):
    my_str = cut_string(my_str)[1]
    uniqs = len(list(set(my_str)))
    return uniqs


if __name__ == '__main__':
    print(count_set('pарa'))
    print(count_set('papa'))

    print(count_hash('pарa'))
    print(count_hash('papa'))

# И все же - зачем здесь хеш?  множества же сделали бы тоже самое
