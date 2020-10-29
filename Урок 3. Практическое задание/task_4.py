"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib

cache = {}
url_salt = {}


def generate_key(url):
    """Генерирует соленый хеш для url"""
    salt = url_salt.get(url)
    if salt is None:
        salt = url[::-1]
        url_salt[url] = salt
    salt_url = hashlib.sha256(url.encode() + salt.encode()).hexdigest()
    return salt_url


def get_cache(key):
    """Возвращает данные из кэша, если они есть в кэш для данного url. Если нет - возвращает None"""
    if key in cache.keys():
        return cache.get(key)
    return None


def get_data(url):
    """Эмулирует получение данных по введенному url, если он не содержится в кэш к этому моменту"""
    return {'data': 'some data'}


def set_cache(key, data):
    """Записывает в кэш url и полученные данные"""
    cache[key] = data


def app():
    """Точка входа в приложение"""
    while True:
        url = input('Введите url: ')  # запрашиваем url
        key = generate_key(url)  # хешируем соленый url
        stored_data = get_cache(key)  # запрашиваем данные по полученому хеш в кэше
        if stored_data is None:  # если данных в кэш нет:
            received_data = get_data(url)  # "идем за данными по url"
            set_cache(key, received_data)  # записываем полученные данные к кэш
            print('Данные по этому url отсутствуют в кэш и будут добавлены. Введите url еще раз')
        else:
            print(stored_data)  # получаем данные из кэш, если есть, если нет - то полученные при первичном запросе
            print(url_salt, cache)


if __name__ == '__main__':
    app()
