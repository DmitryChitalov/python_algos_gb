"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""

import uuid, hashlib

salt = uuid.uuid4().hex
database = {}

def webpage(adress):
    if adress in database.keys():
        print(f"Web page {adress} already cached.")
    else:
        val = hashlib.sha256(salt.encode() + adress.encode()).hexdigest()
        database[adress] = val
        print(database[adress])


webpage('www.google.com')
webpage('www.google.com')