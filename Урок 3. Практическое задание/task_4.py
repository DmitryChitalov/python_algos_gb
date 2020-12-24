"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

class cache(object):
    def __init__(self, fun):
        self.fun = fun
        self.cache = {}

    def __call__(self, *args, **kwargs):
        key  = str(args) + str(kwargs)
        try:
            return self.cache[key]
        except KeyError:
            self.cache[key] = rval = self.fun(*args, **kwargs)
            return rval
        except TypeError: # incase key isn't a valid key - don't cache
            return self.fun(*args, **kwargs)
@cache
def get_url_src(url):
    return urllib.urlopen(url).read()
