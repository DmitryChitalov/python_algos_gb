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

word = 'papa'
words = {}

for i in range(len(word)):
    for j in range(1, len(word)+1):
        if word[i:j] != '' and word[i:j] != word:
            words[hashlib.sha1(word[i:j].encode()).hexdigest()] = word[i:j]

print(words)
print(set(words.values()))
