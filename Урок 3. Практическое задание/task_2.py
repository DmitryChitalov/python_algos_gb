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

В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл

import os, time, hashlib

autorise_dist = {}

def err_pin():
    print("пин-код должен состоять из 4 цифр")
    return

def passw_input(v_salt):
    try:
        v_passw = str(int(input("пин код >>>")))
        if len(v_passw) == 4:
            hash_obj = hashlib.sha256(v_salt.encode() + v_passw.encode()).hexdigest()
        else:
            err_pin()
            hash_obj = None
    except ValueError:
        err_pin()
        hash_obj = None
    return hash_obj


login = os.getlogin()
pin = False

print(f"Добрый день, <{login}>. Установите пинкод:")
while pin is False:
    hash_passw = (passw_input(login.upper()))  # передаем логин в качестве соли
    if hash_passw != None:
        print(f"Пин-код установлен. Хэш пароля записан: {hash_passw}")
        autorise_dist[login.upper()] = hash_passw
        time.sleep(1)
        pin = True

i = 0
while i < 3:  # число попыток ввода
    print("Для проверки доступа введите логин, используемый при регистрации. Регистр не важен")
    #   print(autorise_dist)
    v_login = input("введите логин:").upper()
    key_hash = autorise_dist.get(v_login)
    if key_hash is not None:  # логин в словаре найден, по нему найден авторизованный ранее хеш
        v_hash = passw_input(v_login.upper())

        if v_hash != key_hash:  # пин-код неверный
            print(f"Пин-код неверен. Осталось попыток {2 - i}")
            i += 1
        else:
            print("Отлично. Пин-код верный.")
            print(f"хеш введенного   пин-кода: {key_hash}")
            print(f"хеш сохраненного пин-кода: {v_hash}")
            time.sleep(2)
            i = 3
    else:
        print(f"пользователь <{v_login}> не найден. Осталось {2 - i} попыток")
        i += 1
        if i >= 3:
            print("Вы исчерпали количество попыток...")
            exit()