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

input_string = input("Введите строку из маленьких латинских букв: ")
unique_substrings = set()
hash_collision_check = dict()
for char_index in range(len(input_string)):
    right_part = input_string[char_index:]
    for length in range(1, len(right_part) + 1):
        string_part = input_string[char_index:char_index + length]
        if input_string != string_part:
            substring_hash = hash(string_part)
            # хоть и коллизии маловероятны здесь их в любом случае нужно обработать
            if substring_hash in hash_collision_check:
                if hash_collision_check[substring_hash] != string_part:
                    # как раз тот самый случай, когда для разных значений хеш одинаковый
                    # на самом деле средство разрешения коллизий уже встроено в словарь, и можно было бы им ограничиться
                    # но в задаче требуется именно применить свою хеш функцию, поэтому делаем так.
                    raise Exception('Hash collision error.')  # сделано так только по причине ограничения времени на
                    # задачу, на самом деле правильнее было бы вызвать функцию повторно (может даже с другой хеш-функцией)
                    # либо с самого начала подобрать такую функцию, чтобы коллизии были ещё менее вероятными чем в
                    # случае функции hash()
            else:
                hash_collision_check[substring_hash] = string_part
            unique_substrings.add(substring_hash)

print(f"Количество подстрок в строке {input_string} равно {len(unique_substrings)}")
