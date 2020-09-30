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

from hashlib import sha256


def get_hash(pswd, _salt):
    return sha256(_salt.encode() + pswd.encode() + _salt.encode()).hexdigest()


def hash_check(_hash_in_database, entered_pswd, _salt):
    return _hash_in_database == get_hash(entered_pswd, _salt)


data_user_1 = {
    'login': 'user 1',
    'password': '73e984880789e029a6fed7db309aa261c05068f229af7d88a96daa535d5e6276'
}
salt_user_1 = data_user_1['login']

pswd_user = input('Введите пароль: ')

hash_in_database = get_hash(pswd_user, salt_user_1)
print(f'Хеш хранящийся в базе -> {hash_in_database}')

pswd_verification = input('Введите пароль для проверки: ')

if hash_check(hash_in_database, pswd_verification, salt_user_1):
    print('Вы ввели верный пароль')
else:
    print('Парольи не совпадают!')
