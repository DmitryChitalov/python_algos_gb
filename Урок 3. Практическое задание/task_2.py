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

Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
import sqlite3
from uuid import uuid4
import hashlib


def create_db(db_path):
    try:
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            cur.executescript("""
                DROP TABLE IF EXISTS users;
                CREATE TABLE users(
                    user NOT NULL PRIMARY KEY,
                    password TEXT,
                    uuid NOT NULL
                );
                """)
            conn.commit()
    except sqlite3.DatabaseError as e:
        print(f"Ошибка работы с базой данных: {e}")


def add_user(user, password):
    uuid = str(uuid4())
    """ Генерируем соль для каждого пользователя и складываем в базу.
    не уверен  разумности подхода, т.к. попади база к злоумышленникам будет известна вторая часть пароля.
    еще можно захардкодить соль одну на всех, тогда раздельно будет хранится хеш и соль                     
    """
    hash_password = hashlib.sha256(uuid.encode() + password.encode()).hexdigest()
    print(f'hash pass: {hash_password} \n uuid: {uuid}')
    try:
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO users VALUES(?, ?, ?)", (user, hash_password, uuid))
            conn.commit()
            return True
    except sqlite3.DatabaseError as e:
        if str(e) == 'UNIQUE constraint failed: users.user':
            print(f"Такой пользователь существует!")
        return False


def check_user(user, password):
    try:
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            cur.execute("SELECT user, password, uuid FROM users")
            conn.commit()
            db_user, db_password, uuid = cur.fetchone()
            hash_password = hashlib.sha256(uuid.encode() + password.encode()).hexdigest()
            print(f'hash pass: {hash_password} \n uuid: {uuid}')
            if user == db_user and hash_password == db_password:
                return True
            else:
                return False
    except sqlite3.DatabaseError as e:
        print(f"Ошибка работы с базой данных: {e}")


def main():
    choice = input('Добро пожаловать!\nЧтобы пройти регистрацию введите 1, для аутентификации введите 2\n')
    if choice == '1':
        login = input('Введите логин')
        password = input('Введите пароль')
        if add_user(login, password):
            print("Регистрация успешна!")
    elif choice == '2':
        login = input('Введите логин')
        password = input('Введите пароль')
        if check_user(login, password):
            print(f'Аутентификация успешна!')
        else:
            print(f'Нет такой учетной записи')
    if input('Выйти? (да)') == 'да':
        return 0
    main()


if __name__ == '__main__':
    db_path = 'test.sqlite'
    create_db(db_path)
    main()
