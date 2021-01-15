from uuid import uuid4
import hashlib

salt = uuid4().hex
cache = {}

def get_page(url):
    if cache.get(url):
        print(f'Url: {url} is IN cache')
    else:
        result = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache[url] = result
        print(cache)

get_page('https://www.yandex.ru')
get_page('https://www.yandex.ru')