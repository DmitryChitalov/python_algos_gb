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

user_base = {'oleg': 123}
flag = False
while flag == False:
    login = input('Введите логин: ')
    if login in user_base:
        print('Такой логин уже существует! Введите новый.')
        flag = False
    else:
        flag = True
password = input('Введите пароль: ')
pass_hash = hashlib.sha256(password.encode('utf-8') + login.encode('utf-8')).hexdigest()
print(f'Хеш пароля - {pass_hash}')
check_pass = input('Введите пароль еще раз для проверки: ')
check_pass_hash = hashlib.sha256(check_pass.encode('utf-8') + login.encode('utf-8')).hexdigest()
if pass_hash == check_pass_hash:
    print('Пароли совпадат. Пользователь добавлен в базу')
    user_base[login] = pass_hash
else:
    print('Пароли не совпадают. Пользователь не добавлен в базу!')
