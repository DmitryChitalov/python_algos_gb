from uuid import uuid4
import hashlib

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


def check_password(count=0):
    password_one = input('Введите пароль: ')                                    # первый введенный пароль
    hash_1 = hashlib.sha256(salt.encode() + password_one.encode()).hexdigest()  # создание хеша 1го пароля

    file = open('test.txt', 'r+')
    for line in file.readlines():
        if line.strip() == hash_1:
            count += 1
    if count == 0:
        file.writelines(hash_1 + '\n')          # запись хеша в файл
    count = 0
    file.close()

    print(f'---В базе данных хранится строка: {hash_1}')
    password_two = input('Введите пароль еще раз для проверки: ')               # второй введенный пароль
    hash_2 = hashlib.sha256(salt.encode() + password_two.encode()).hexdigest()  # создание хеша 2го пароля

    file = open('test.txt', 'r')
    for line in file.readlines():
        if line.strip() == hash_2:
            count += 1
    if count == 0:
        print('---Error! Ваши пароли НЕ совпадают')
    else:
        print('---OK! Ваши пароли совпадают')
    file.close()


# file = open('test.txt', 'w')
# file.close()

salt = uuid4().hex          # генерируемая соль
check_password()