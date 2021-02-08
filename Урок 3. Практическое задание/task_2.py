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

import sqlite3
from hashlib import sha256

conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS PASS (user,password)''')


def insert_into_pass(conn, usr, hash_pass):
    c = conn.cursor()
    c.execute('''INSERT INTO PASS values(?, ?)''', (usr, hash_pass))
    conn.commit()


def select_from_pass_by_usr(conn, usr):
    c = conn.cursor()
    c.execute('SELECT password FROM PASS WHERE user=?', (usr,))
    row = c.fetchone()
    print(row)
    if row is None:
        return None
    else:
        return row[0]


def hashing_password(pas, usr):
    return sha256(pas.encode() + usr.encode()).hexdigest()


while True:
    input_user = input("Введите имя пользователя: ")
    res = select_from_pass_by_usr(conn, input_user)
    input_password = input('Введите пароль: ')
    p_hash = hashing_password(input_password, input_user)
    if res is None:
        # new user create
        insert_into_pass(conn, input_user, p_hash)
        res = p_hash
    print('В базе данных хранится строка: {}'.format(res))
    same_pas=input('Введите пароль еще раз для проверки: ')
    new_hash = hashing_password(same_pas, input_user)
    if res == new_hash:
        print('Вы ввели правильный пароль')
    else:
        print('Пароль введен не правильно')

