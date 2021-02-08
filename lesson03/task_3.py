"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
a
"""

# hash?

my_string = str(input("Введите строку: "))
hash_set = {hash(my_string)}
unique_count = 0
for idx1 in range(len(my_string)):
    for idx2 in range(idx1 + 1, len(my_string) + 1):
        sub_string = my_string[idx1:idx2]
        hash_string = hash(my_string[idx1:idx2])
        if hash_string not in hash_set:
            # print(sub_string)
            hash_set.add(hash_string)
            unique_count += 1

print(f"Всего уникальных подстрок: {unique_count}")
