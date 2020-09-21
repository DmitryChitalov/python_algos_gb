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
import task_2


def get_substrings(word):
    hashes = set()
    word_lengh = len(word)
    for length in range(word_lengh - 1):
        idx = 0
        while idx + length < word_lengh:
            substring = word[idx:idx + length + 1]
            # Получаем хеш.
            local_hash = task_2.get_hash(password=substring, salt='salt')
            # Проверяем его наличие.
            if not local_hash in hashes:
                # Сохраняем хеш.
                hashes.add(local_hash)
                # Выводим уникальную подстроку.
                print(substring)
            idx += 1
    return len(hashes)

"""
Я не был уверен, является ли строка своей же подстрокой
"""
print(f'Количество различных подстрок: {get_substrings("papa")}')
