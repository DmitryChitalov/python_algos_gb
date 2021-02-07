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


def reverse(n):
    if len(n) == 0:
        return n
    else:
        return n[len(n) - 1] + reverse(n[:len(n) - 1])


def sub_counter(s):
    result_set = set()

    for i in range(len(s)):
        result_set.add(hashlib.sha1(s[:i].encode()).hexdigest())

    for i in range(len(s) - 1):
        result_set.add(hashlib.sha1(s[i + 1:].encode()).hexdigest())

    # переворачиваем строку 'qwerty' -> 'ytrewq' и повторяем действия выше
    reverse_str = reverse(s)

    for i in range(len(reverse_str)):
        result_set.add(hashlib.sha1(reverse_str[:i].encode()).hexdigest())

    for i in range(len(reverse_str) - 1):
        result_set.add(hashlib.sha1(reverse_str[i + 1:].encode()).hexdigest())

    return f'введенная строка: {s}, количество уникальных подстрок: ' \
           f'{len(result_set) - 1}'  # -1 т.к. не считаем пустую подстроку ''


print(sub_counter('papa'))
