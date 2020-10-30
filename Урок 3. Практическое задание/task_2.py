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


def get_hash(passwd, salt):
    return hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()


def password_verification(passwd, salt):
    hash_passwd = get_hash(passwd, salt)
    print(f'В базе данных хранится строка: {hash_passwd}')
    repeated_passwd = input('Введите пароль еще раз для проверки: ')
    if hash_passwd == get_hash(repeated_passwd, salt):
        return print('Вы ввели правильный пароль')
    else:
        return print('Ошибка! Вы ввели неправильный пароль')


if __name__ == "__main__":
    user_salt = "89991237788"  # номер телефона
    password_verification(input("Введите пароль: "), user_salt)