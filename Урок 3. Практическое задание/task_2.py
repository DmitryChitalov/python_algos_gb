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
from uuid import uuid4
import hashlib

next_inter = True
users_list = []
user_fname = ['Имя']
user_passw = ['Пароль']
salt = uuid4().hex


def createUsersList(user_fname: list, user_passw: list) -> list:
    user_row = {user_fname[0]: user_fname[1]
        , user_passw[0]: user_passw[1]}

    users_list.append(user_row)
    return users_list


def encode_passwd(passwd):
    hash_passwd = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
    return hash_passwd


while next_inter:
    while True:
        user_value = input("Ведите 'Имя' пользователя: ")
        if user_value != "":
            user_fname.append(user_value)
            break
        else:
            print("Ошибка ввода: поле 'Имя' пустое.")
    while True:
        user_value = input("Ведите 'Пароль' пользователя: ")
        if user_value != "":
            hash_pass = encode_passwd(user_value)
            user_passw.append(hash_pass)
            user_value = input("Ведите 'Пароль' еще раз: ")
            if user_value != "":
                hash_pass = ""
                hash_pass = encode_passwd(user_value)
                if hash_pass == user_passw[1]:
                    print(f"Пароли совпадают {hash_pass} :: {user_passw[1]}")
                    break
                else:
                    print(f"Пароли не совпадают {hash_pass} :: {user_passw[1]}")
                    break
            else:
                print("Ошибка ввода: поле 'Пароль' пустое.")
        else:
            print("Ошибка ввода: поле 'Пароль' пустое.")

    users_list = createUsersList(user_fname, user_passw)

    while True:
        next_add = input("Хотите добавить дополнительного пользователя? (Да / Нет): ")
        if next_add.lower() in ('да', 'нет', 'yes', 'no', 'y', 'n'):
            next_inter = next_add.lower() in ('да', 'yes', 'y')
            break
        else:
            print("Ошибка ввода: введите ответ еще раз")

print("- " * 50)
print(users_list)
