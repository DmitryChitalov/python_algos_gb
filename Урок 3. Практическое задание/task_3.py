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


def get_hash(argstr):
    argstr = argstr.encode("utf-8")
    str_hash = hashlib.sha256(argstr)
    str_hash_hex = str_hash.hexdigest()
    return str_hash_hex


def build_set(my_str):
    res_set = set()
    start_pos = 0
    substr_count = 0
    while start_pos != len(my_str):
        for pos in range(start_pos, len(my_str) - 1):
            if start_pos != pos:
                line = my_str[start_pos:pos]
                res_set.add(get_hash(line))
                substr_count += 1
                print(line)
        start_pos += 1
    return res_set, substr_count


def main():
    pass
    try:
        my_str = "dodod"
        res_set, substr_count = build_set(my_str)

        print("Выводим сохраненыу хэши")
        for item in res_set:
            print(f"{item}")

        print(f"Из {substr_count} подстрок мы получили {len(res_set)} уникальных хэшей")

        print("\nПрограмма завершена!")
    except Exception as ex:
        print(f"Fatal error: {ex}")


if __name__ == "__main__":
    main()
