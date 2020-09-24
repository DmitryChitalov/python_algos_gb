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

from hashlib import pbkdf2_hmac


def passwd_check():
    while True:
        first_answer_l = input('Введите логин: ').encode('utf-8')
        first_answer_p = input('Введите пароль: ').encode('utf-8')
        one = pbkdf2_hmac(
            hash_name='sha256',
            password=first_answer_p,
            salt=first_answer_l,  # сразу решил юзать логин в качестве соли
            iterations=100000
        )
        print(f'В базе данных хранится: {one}')
        second_answer_l = input('Повторно введите логин: ').encode('utf-8')
        second_answer_p = input('Повторно введите пароль: ').encode('utf-8')
        two = pbkdf2_hmac(
            hash_name='sha256',
            password=second_answer_p,
            salt=second_answer_l,
            iterations=100000
        )
        print(f'В базе данных хранится: {two}')
        if one == two:
            print('Всё верно')
            break
        else:
            print('Данные не совпадают')


passwd_check()
