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

str_input = input("Введите слово: ")


def com(str_in, res=set()):
    if len(str_in) == 0:
        return
    k = 0
    for j in range(len(str_in)):
        res.add(hash(str_in[0:j + 1]))
        k = j + 1
    com(str_in[1:k], res)
    return res


result = com(str_input)
print('количество различных подстрок с использованием хеш-функции: {}'.format(len(result)))
