"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import os, hashlib, urllib3
cache_table = {}
def cache_check(url):

    content = ''
    hasher = hashlib.new('md5')
    http = urllib3.PoolManager()
    req = http.request('GET', url)
    with open('cache', 'wb+') as f:
        f.write(req.data)
        content = f.read()
        hasher.update((str(content) + url).encode('utf-8'))
        if hasher.hexdigest() not in cache_table:
            cache_table[url] = hasher.hexdigest()
            # ну и здесь тогда можно добавить, например сохранения кэшированного файла в папку кэша
        os.remove('cache')

cache_check('http://rostovmeteo.ru/index.php')
cache_check('https://161.ru/index.php')
cache_check('http://rostovmeteo.ru/index.php')
print(cache_table)
