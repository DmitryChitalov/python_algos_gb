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


def unique_sub_str_1(start_str):
    """Функция для определения уникальных подстрок в слове (с использованием множества)

    :param start_str: Исходное слово
    :return: Возвращается множество уникальных подстрок
    """
    sub_str = set()
    str_len = len(start_str)
    while str_len > 1:
        a, b = 0, str_len - 1
        while b <= len(start_str):
            sub_str.add(start_str[a:b])
            a, b = a + 1, b + 1
        str_len -= 1
    return sub_str


def unique_sub_str_2(start_str):
    """Функция для определения уникальных подстрок в слове (с использованием хеш-ключа)

    :param start_str: Исходное слово
    :return: Возвращается массив со всеми уникальными подстроками
    """
    sub_str = dict()
    str_len = len(start_str)
    while str_len > 1:
        a, b = 0, str_len - 1
        while b <= len(start_str):
            sub_str[hash(start_str[a:b])] = start_str[a:b]
            a, b = a + 1, b + 1
        str_len -= 1
    return [sub_str[i] for i in sub_str]


def print_unique(lst):
    print(f"Уникальные подстроки ({len(lst)}):\n{', '.join(lst)}")


##########################################
word = "рара"

sub_str_1 = unique_sub_str_1(word)
print_unique(sub_str_1)

sub_str_2 = unique_sub_str_2(word)
print_unique(sub_str_2)

word = "abrakadabra"

sub_str_1 = unique_sub_str_1(word)
print_unique(sub_str_1)

sub_str_2 = unique_sub_str_2(word)
print_unique(sub_str_2)
