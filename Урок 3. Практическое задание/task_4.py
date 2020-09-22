"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib
from uuid import uuid4

def mem(func):
    def g(a, memory={}):
        r = memory.get(a)
        if r is None:
            r = func(a)
            memory[a] = r
        print(memory)
        return r
    return g
@mem
def get_url(b):
    a = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    return a

salt = uuid4().hex
for i in range(5):
    url = input('Enter - ')
    print(get_url(url))




