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
import hashlib as hl


def substr_generate(string):
    start = 0
    stop = 0

    def get_hash(string):
        return hl.md5(string.encode()).hexdigest()

    while True:
        string_hash = get_hash(string[start:stop + 1])
        if start == len(string) - 1:
            print('Case 3')
            if string_hash not in hash_archive:
                hash_archive.append(string_hash)
                print(string[start: stop + 1])
            print(f'Всего {len(hash_archive)} подстрок')
            break
        elif stop == len(string):
            print('Case 2')
            start += 1
            stop = start
        else:
            print('Case 1')
            if string_hash not in hash_archive:
                hash_archive.append(string_hash)
                print(string[start: stop + 1])
                stop += 1
            else:
                stop += 1
                continue


#########################################


hash_archive = []
substr_generate('parapam')
print(hl.md5('a'.encode()).hexdigest())
