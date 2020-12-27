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
import time


def count_unique_substrings(string: str) -> int:
    ln = len(string)
    st_set = set()
    for i in range(ln):
        for j in range(ln-i):
            st_set.add(hashlib.sha256(string[i:ln-j].encode()).hexdigest())
    return len(st_set)


# Вариант решения со словарем
def count_unique_substrings1(string: str) -> int:
    ln = len(string)
    a = {hashlib.sha256(string[i:ln-j].encode()).hexdigest(): '' for i in range(ln) for j in range(ln-i)}
    return len(a.items())


if __name__ == '__main__':
    s1 = time.perf_counter()
    print(count_unique_substrings('papa'))
    print(time.perf_counter() - s1)

    # Сравниваем скорость работы
    s1 = time.perf_counter()
    print(count_unique_substrings1('papa'))
    print(time.perf_counter() - s1)
