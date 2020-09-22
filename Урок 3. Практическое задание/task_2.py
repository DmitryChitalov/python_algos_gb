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


def get_pass_user():
    """
    функция запрашивает пароль пользователя
    :return: str
    """
    return input('Enter your password: ')


def hash_password(password, salt='I am salt'):
    """
    функция получает пароль и хеширует его с солью
    :param salt: str
    :param password: str
    :return: hash
    """
    res = hashlib.sha3_256(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
    print(res)
    return res


def check_password(first_passw, second_passw):
    if first_passw == second_passw:
        print('Ok')
        return True
    else:
        print('Пароли не совпадают: ')
        return False


def main(first_pw):
    pw_2 = get_pass_user()
    second_pw = hash_password(pw_2)
    if check_password(first_pw, second_pw) is False:
        main(first_pw)
    return


pw_1 = hash_password(get_pass_user())
main(pw_1)
