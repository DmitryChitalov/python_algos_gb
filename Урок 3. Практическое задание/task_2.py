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

# print(hashlib.algorithms_available)
# print(hashlib.algorithms_guaranteed)


def get_hash(phrase, salt):
    # print( phrase, salt)
    hash_obj= hashlib.sha256(salt.encode() + phrase.encode()).hexdigest();
    return hash_obj

if __name__ == "__main__":
    login = input('Введите логин: ')
    passwd = input('Введите пароль: ')
    stored_digest = get_hash(passwd, login)
    print(f"{stored_digest} сохранено")
    confirm = input('Подтвердите повторным вводом пароля: ')
    if stored_digest == get_hash(confirm, login):
        print('Пароли совпадают, учетная запись создана')
    else:
        print('Введенные пароли  не совпадают!')
