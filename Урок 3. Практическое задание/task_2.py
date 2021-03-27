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
import sys
from textwrap import dedent
from random import choice, randint
from hashlib import pbkdf2_hmac


# Класс для удобства работы с базой данных
class SQLite():
    def __init__(self, file='passwd.db'):
        self.file = file

    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        self.conn.row_factory = sqlite3.Row
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.conn.close()


# Генерирует имя пользователя из букв,
# следит за чередованием гласных и согласных
def gen_login(maxlen=10):
    SONANTS = 'aeiou'
    CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
    i1 = randint(0, 1)
    i2 = randint(i1 + 3, maxlen)
    result = []
    for i in range(i1, i2+1):
        arr = SONANTS if i % 2 == 0 else CONSONANTS
        result.append(choice(arr))
    return "".join(result)


# Генерирует пароль из произвольных символов
def gen_passwd(n=5):
    return "".join(chr(randint(33, 126)) for _ in range(n))


# Генерирует таблицу (логин, пароль)
def gen_db(size=10):
    return [
        (gen_login(), gen_passwd())
        for i in range(size)
    ]


def hashit(login, passwd):
    scrambled = "".join(
        [x for i, c in enumerate(login) for x in (c, login[-i-1])]*3)
    saltb = scrambled.encode()
    passb = passwd.encode()
    return pbkdf2_hmac(
        hash_name='sha256',
        password=passb,
        salt=saltb,
        iterations=100000
    ).hex()


def reset_db():
    db = gen_db()
    with open("passwd.txt", "w") as fo:
        for login, passwd in db:
            fo.write(f"{login}\t{passwd}\n")
    data = [
        (login, hashit(login, passwd))
        for login, passwd in db
    ]

    with SQLite() as cur:
        try:
            cur.execute(dedent("""\
                DELETE FROM users"""))
        except sqlite3.OperationalError:
            cur.execute(dedent("""\
                CREATE TABLE users
                (login text, hash text)"""))

        cur.executemany(dedent("""\
            INSERT INTO users
            VALUES (?, ?)"""), data)


def check_passwd(login, passwd):
    with SQLite() as cur:
        cur.execute('SELECT * FROM users WHERE login=?', (login,))
        res = cur.fetchone()
        if res is not None:
            if hashit(login, passwd) == res[1]:
                print("Успешный вход в систему")
                return None
        print("Неправильный логин или пароль")


if len(sys.argv) > 2:
    check_passwd(sys.argv[1], sys.argv[2])
elif len(sys.argv) > 1 and sys.argv[1] == "--reset":
    reset_db()
else:
    print("usage: task_2.py <uname> <passwd> OR task_2.py --reset")
