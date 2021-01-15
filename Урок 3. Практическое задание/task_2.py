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


def make_hash(salt, password):
    hash_obj_salt = hashlib.sha3_256(salt.encode())
    hex_result_salt = hash_obj_salt.hexdigest()
    hash_obj_psw = hashlib.sha3_256(password.encode())
    hex_result_psw = hash_obj_psw.hexdigest()
    hex_result = hex_result_salt + hex_result_psw
    return hex_result


user_name = input('Введите login: ')
user_password = input('Введите пароль: ')
result = make_hash(user_name, user_password)
print(f'В базе данных хранится строка: {result}')

with open('file_hash.txt', 'w', encoding='utf8') as f:
    f.write(result)

user_name = input('Введите еще раз login: ')
user_password = input('Введите еще раз пароль: ')
result = make_hash(user_name, user_password)

with open('file_hash.txt', 'r', encoding='utf8') as f:
    pswd = f.read()

if result == pswd:
    print('Доступ разрешен')
else:
    print('Что-то пошло не так')
