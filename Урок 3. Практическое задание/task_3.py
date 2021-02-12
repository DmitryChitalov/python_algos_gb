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


def substr_count(string):
    import hashlib
    count = len(string)
    set_substr = set()
    for start in range(0, count - 1):
        if start != 0:
            set_substr.add(hashlib.sha256(string[start:count].encode()).hexdigest())
        for end in range(count - 1, 1, -1):
            if start != end:
                set_substr.add(hashlib.sha256(string[start:end].encode()).hexdigest())
    return len(set_substr)


string = "papa"
print(f"В строке \"{string}\" различных подстрок {substr_count(string)}")
