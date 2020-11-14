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
from hashlib import md5

word = "papa"
hash_set = set()
foo = set()
for i in range(len(word)):
    for j in range(len(word), i, -1):
        bar = word[i:j]
        if bar != word:
            foo.add(bar)
            hash_set.add(md5(bar.encode()).hexdigest())
print(hash_set)
print(foo)
print(f'В строке "{word}" {len(hash_set)} различных подстрок')
