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
"""


def main():
    source = 'papa'
    substrings = set()
    for i in range(len(source)+1):
        for j in range(i+1, len(source)+1):
            if source[i:j] and not (i == 0 and j == len(source)):
                substrings.add(source[i:j])
    print(substrings)
    print(f'Уникальных подстрок: {len(substrings)}')


if __name__ == '__main__':
    main()
