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
from binascii import hexlify
from hashlib import pbkdf2_hmac
import sqlite3
from sqlite3 import Error


def sql_connection():

    try:
        con = sqlite3.connect(":memory:")
        return con
    except Error:
        print(Error)


def create_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE users(login text, password_hash text)")
    con.commit()


def create_user(login, password):
    p = hexlify(
        pbkdf2_hmac(
            hash_name="sha256",
            password=password.encode(),
            salt=login.encode(),
            iterations=100000,
        )
    )
    con.execute(
        f"INSERT INTO users(login, password_hash) VALUES (?,?)", (login, p)
    )
    return p


def check_password(login, password):
    cur = con.execute(
        "select password_hash from users where login = ?", (login,)
    )
    db_pass_hash = cur.fetchone()
    new_pass_hash = hexlify(
        pbkdf2_hmac(
            hash_name="sha256",
            password=password.encode(),
            salt=login.encode(),
            iterations=100000,
        )
    )
    if db_pass_hash[0] == new_pass_hash:
        print("Вы ввели правильный пароль.")
    else:
        print("Ошибка. Неправильный пароль.")


con = sql_connection()
create_table(con)
create_user("user1", input("Введите пароль :"))
cur = con.execute('select password_hash from users where login = "user1"')
db_pass = cur.fetchone()
print(f"В базе данных хранится строка:{db_pass[0]}")
check_password("user1", input("Введите пароль еще раз для проверки:"))
con.close()
