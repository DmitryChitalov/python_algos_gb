"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""


from uuid import uuid4
import hashlib

salt = uuid4().hex
cache_obj = {}

def get_page(url):
    if cache_obj.get(url):
        print(f'Данный адрес: {url} присутствует в кэше')
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache_obj[url] = res
        print(cache_obj)

get_page('https://soap4.me/')
get_page('http://warcraftlogs.com')
get_page('https://wago.io')

# print(hash('https://soap4.me/'))  # -> -6499363324312427766, а потом 4749810662702906957 и т.д.

# а такие результаты у других разработчиков
# hash('http://warcraftlogs.com') Result: 3376700473951288741, а потом 5301384251666604420 и т.д.

# hash('https://wago.io') Result: -7927643437841927488, а потом -1237842076897232829  и т.д.

# сделаем выводы!