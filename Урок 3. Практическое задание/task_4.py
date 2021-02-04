"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from hashlib import sha256
from uuid import uuid4

a = set()
salt = uuid4().hex
while True:
    var_str = input("Введите URL (пустая строка - выход):")
    if var_str == "":
        break
    hash_val = sha256(salt.encode() + var_str.encode()).hexdigest()
    if hash_val in a:
        print(f"Страница была закеширована ранее")
    else:
        a.add(hash_val)
        print(f"Страница добавлена в кэш")
