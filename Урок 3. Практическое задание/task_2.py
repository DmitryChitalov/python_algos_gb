"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""

import hashlib
import uuid



def get_hash(passwd_obj, hash_salt):
    pass_and_solt = hash_salt.encode("utf-8") + passwd_obj.encode("utf-8")
    pass_hash = hashlib.sha256(pass_and_solt)
    pass_hash_hex = pass_hash.hexdigest()
    return pass_hash_hex


def check_hash(old_hash, new_hash):
    return old_hash == new_hash


def do_ask_password(message):
    pass
    res = input(message)
    return res


def main():
    pass
    try:
        hash_salt = uuid.uuid4().hex
        password = do_ask_password("Введите пароль: ")
        hashed_pass = get_hash(password, hash_salt)

        retype_pass = do_ask_password("Введите пароль еще раз: ")
        hashed_newpass = get_hash(retype_pass, hash_salt)

        if check_hash(hashed_pass, hashed_newpass):
            print("Пароли совпали.")

        else:
            print("Пароли не совпали!")
        print(f"Первый пароль в виде хэша: {hashed_pass}")
        print(f"Второй пароль в виде хэша: {hashed_newpass}")

        print("\nПрограмма завершена!")
    except Exception as ex:
        print(f"Fatal error: {ex}")


if __name__ == "__main__":
    main()
