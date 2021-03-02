"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""


""" 
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
import hashlib
from uuid import uuid4

hash_salt = uuid4().hex
v_url_cache = {}


def check_cache(tmp_url):
    v_hash = hashlib.sha256(hash_salt.encode() + tmp_url.encode()).hexdigest()
    #    if v_url_cache.get(tmp_url) is None:
    if v_url_cache.get(v_hash) is None:
        v_url_cache[v_hash] = tmp_url
        return "новая страница добавлена в кэш: " + v_url
    else:
        v_url_cache[v_hash] = tmp_url
        return "страница уже в кэше: " + v_url

for i in range(1, 5):
    v_url = "https://ya.ru/"
    print(f"зашел на страницу {i}-й раз. {check_cache(v_url)}")

for i in range(1, 2):
    v_url = "https://e1.ru/"
    print(f"зашел на страницу {i}-й раз. {check_cache(v_url)}")

v_url = "https://e1.ru/"
print(f"зашел на страницу снова. {check_cache(v_url)}")


#print(v_url_cache)