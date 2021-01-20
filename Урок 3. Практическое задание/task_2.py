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

from hashlib import sha256
from uuid import uuid4
import sqlite3  # импорт библиотеки sqlite
from sqlite3 import Error  # импорт класса

salt = uuid4().hex


#  print(salt)


def create_connection(path):  # подключение к базе данных
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Соединение успешно")
    except Error as E:
        print(f" Произошла ошибка '{E}'!")

    return connection


connect = create_connection("E:\\gb\example.sqlite")  # создает файл базы данных по указанному пути


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Добавление в БД успешно")
    except Error as e:
        print(f"Ошибка '{e}' !")


def read_query(connection, query):  # чтение из БД
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return print(result)
    except Error as e:
        print(f" Ошибка '{e}'! ")


# оздание простой таблицы с двумя столбцами id и pass
create_hash_pass_table = """                    
CREATE TABLE IF NOT EXISTS hashed_pass (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pass BLOB 
);
"""
execute_query(connect, create_hash_pass_table)


def hash_pass(password):
    psswrd = sha256(salt.encode() + password.encode()).hexdigest() + '/' + salt
    execute_query(connect, f"insert into hashed_pass(pass) values ('{psswrd}')")
    # read_query(connect, "SELECT * FROM hashed_pass")
    return psswrd


def check_hashed_pass():
    check_pass = input('Введите пароль для проверки: ')
    check_pass_h = sha256(salt.encode() + check_pass.encode()).hexdigest() + '/' + salt
    psswrd = read_query(connect, "SELECT pass FROM hashed_pass WHERE id = 1")
    if check_pass_h == psswrd:
        print('Введен правильный пароль ')
    else:
        print('Пароли не совпадают')


passwd = input('Введите пароль: ')
hash_pass(passwd)
# execute_query(connect, hash_pass(passwd))
check_hashed_pass()
# execute_query(connect, "DROP TABLE IF EXISTS hashed_pass")
#abc = read_query(connect, "SELECT pass FROM hashed_pass WHERE id = 1 ")
#print(type(abc))
