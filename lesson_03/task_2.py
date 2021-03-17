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
import sqlite3
from os import path
from contextlib import contextmanager


@contextmanager
def db_connect(name):
    con = sqlite3.connect(name)
    yield con
    con.commit()
    con.close()


class UserValidator:

    def __init__(self, name_db):
        self.db_name = f'{name_db}.db'
        if not path.exists(self.db_name):
            with db_connect(self.db_name) as con:
                cur = con.cursor()
                cur.execute('CREATE TABLE users_pass (login varchar PRIMARY KEY, password_hash varchar)')

    def add_user(self, login, password):
        pass_hash = hashlib.sha256(password.encode(encoding='utf-8') + login.encode(encoding='utf-8')).hexdigest()
        with db_connect(self.db_name) as con:
            cur = con.cursor()
            cur.execute('INSERT OR IGNORE INTO users_pass VALUES (?, ?)', (login, pass_hash))
        print(f'Добавлен пользователь {login}')
        print(f'В базу сохранен хеш пароля: {pass_hash}\n')

    def delete_user(self, login):
        with db_connect(self.db_name) as con:
            cur = con.cursor()
            cur.execute('DELETE FROM users_pass WHERE login=:log', {'log': login})

    def update_user(self, login, new_password):
        pass_hash = hashlib.sha256(new_password.encode(encoding='utf-8') + login.encode(encoding='utf-8')).hexdigest()
        with db_connect(self.db_name) as con:
            cur = con.cursor()
            cur.execute('UPDATE users_pass SET password_hash=:hash WHERE login=:log',
                        {'hash': pass_hash, 'log': login})

    def get_users_data(self):
        with db_connect(self.db_name) as con:
            cur = con.cursor()
            cur.execute('SELECT * FROM users_pass')
            result = cur.fetchall()
        return result

    def validation(self, login, password):
        with db_connect(self.db_name) as con:
            cur = con.cursor()
            cur.execute('SELECT password_hash FROM users_pass WHERE login=:log', {'log': login})
            pass_hash = cur.fetchone()

        if pass_hash is not None:
            user_pass_hash = hashlib.sha256(password.encode(encoding='utf-8') +
                                            login.encode(encoding='utf-8')).hexdigest()
            if pass_hash[0] == user_pass_hash:
                return True
            else:
                return False

    @staticmethod
    def enter_user_data():
        user_log = input('Введите логин: ')
        user_pas = input('Введите пароль: ')
        return user_log, user_pas


if __name__ == '__main__':

    users = UserValidator('users_db')

    test_dict = {
        'Masha': '123',
        'Dino747': '456',
        'Zanuda_over_9000': 'bHyuL3oih0J8N190fd',
        'User_user': '111111',
        'Simka': 'tralala1',
        'Kotik': '999666'
    }

    for log, pas in test_dict.items():
        users.add_user(log, pas)

    print('В базе хранятся следующие записи:')
    print(*users.get_users_data(), sep='\n')

    print('\nВведите данные пользователя для добавления в базу:')
    us_log, us_pass = users.enter_user_data()
    users.add_user(us_log, us_pass)
    confirm_pass = input('Для входа введите пароль повторно:')
    valid = users.validation(us_log, confirm_pass)
    if valid:
        print('Доступ разрешён!')
    elif not valid:
        print('Доступ запрещён!')
    else:
        print('Логина нет в системе!')

    print('\nТеперь в базе хранятся следующие записи:')
    print(*users.get_users_data(), sep='\n')

    users.delete_user('Masha')

    print('\nМы удалили пользователя Masha. Теперь в базе хранятся следующие записи:')
    print(*users.get_users_data(), sep='\n')
