"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import random, hashlib
import sqlite3

# Создаем базу для хранения хешей URL (поле url - для теста. в реальной БД не используем)
conn = sqlite3.connect('db_url.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS url(
                urlid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                urlhash TEXT,
                url TEXT);
            """)
conn.commit()

# для теста заполняем значениями
lst_url = set(['URL_' + str((random.randint(1, 100))) for i in range(1, 100)])
#print(lst_url)

login = 'somelogin'

# солим и добавляем хеши в БД
for i in lst_url:
    hash_obj_str = hashlib.sha256(i.encode('utf-8') + login.encode('utf-8')).hexdigest()
    curr = (None, hash_obj_str, i)
    cur.execute("INSERT INTO url VALUES(?, ?, ?);", curr)
conn.commit()

while True:
    S = str(input("Введите URL: "))
    hash_obj_str_check = hashlib.sha256(S.encode('utf-8') + login.encode('utf-8')).hexdigest()

    select_cursor = "SELECT URLHASH FROM url WHERE url.URLHASH = :h_o"
    cur.execute(select_cursor, {'h_o': hash_obj_str_check})
    one_result = cur.fetchone()

    if one_result is not None and one_result[0] == hash_obj_str_check:
        print('URL is found')
    else:
        print('URL has been add to base')
        hash_obj_str = hashlib.sha256(S.encode('utf-8') + login.encode('utf-8')).hexdigest()
        curr = (None, hash_obj_str, S)
        cur.execute("INSERT INTO url VALUES(?, ?, ?);", curr)
        conn.commit()
