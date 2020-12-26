"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib

salt = 'my_salt'
cache_table = {}

def cache_web_pages(url : str, cache : dict, salt : str):
    if cache.get(url):
        return f"Адрес {url} уже есть в кэше"
    else:
        cache[url]= hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        return f"Адрес {url} добавлен в кэш"


print(cache_web_pages("https://test1.ru", cache_table, salt))
print(cache_web_pages("https://test2.ru", cache_table, salt))
print(cache_web_pages("https://test3.ru", cache_table, salt))
print(cache_table)
print(cache_web_pages("https://test1.ru", cache_table, salt))
print(cache_table)
