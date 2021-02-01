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
from binascii import hexlify
from hashlib import pbkdf2_hmac

new_word = 'papa'


def num_substrings(word):
    hash_set = set()

    for start in range(len(word)):
        for finish in range(len(word)):
            substring = word[start:finish + 1]
            if substring and substring != word:
                hash_substring = hexlify(pbkdf2_hmac(
                    hash_name='sha256',
                    password=substring.encode('utf-8'),
                    salt=substring.encode('utf-8'),
                    iterations=10)).decode('utf-8')
                hash_set.add(hash_substring)
    return len(hash_set)


print(num_substrings(new_word))
