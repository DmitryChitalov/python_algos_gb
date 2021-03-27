"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib
from random import randint, seed


# Поскольку в этой задаче абстрактные объекты типа "хеш" или "словарь"
# наделяются конкретным смыслом (страница, url), логично ожидать,
# что класс будет моделировать процесс загрузки страницы.
# Это значит, что должны быть по крайней мере два метода.
# 1. Узнать, есть ли страница в кэше, если да, то получить
# из кэша содержимое.
# 2. Положить в кэш содержимое после успешной загрузки.
#
# Примечание: класс не защищен от коллизий. Грубо говоря,
# есть вероятность, что по запросу http://kremlin.ru
# будет показан http://whitehouse.gov или наоборот.
# Соль никак не защищает от этого, вернее, какие-то коллизии
# она убирает, но какие-то добавляет, и заранее это не определить,
# (иначе это уже не криптография).
class Cache:
    def __init__(self, salt):
        self.thecache = {}
        self.salt = salt.encode()

    def get_hash(self, url):
        return hashlib.sha256(url.encode()+self.salt).hexdigest()

    def __getitem__(self, url):
        hash_ = self.get_hash(url)
        return self.thecache.get(hash_)

    def __setitem__(self, url, text):
        hash_ = self.get_hash(url)
        self.thecache[hash_] = text


# Для симуляции процесса загрузки
def get_text(url):
    return f"<Это текст страницы {url}>"


cache = Cache(
    "Подсказка: задачу решите обязательно с применением 'соленого' хеширования")

urls = [
    "http://yandex.ru",
    "http://google.com",
    "http://geekbrains.ru"
]

# симулируем пользовательскую активность
seed(12)
order = [randint(0, 2) for _ in range(10)]
# [1, 1, 2, 2, 2, 1, 0, 1, 0, 1]

for i in order:
    url = urls[i]
    text = cache[url]
    if not text:
        # загружаем страницу
        text = get_text(url)
        print("Страница ", url, "не найдена в кэше, загружаем ее:\n", text)
        cache[url] = text
    else:
        print("Страница ", url, "есть в кэше, ее содержимое:\n", text)

# ---output---
# Страница  http://google.com не найдена в кэше, загружаем ее:
#  <Это текст страницы http://google.com>
# Страница  http://google.com есть в кэше, ее содержимое:
#  <Это текст страницы http://google.com>
# Страница  http://geekbrains.ru не найдена в кэше, загружаем ее:
#  <Это текст страницы http://geekbrains.ru>
# Страница  http://geekbrains.ru есть в кэше, ее содержимое:
#  <Это текст страницы http://geekbrains.ru>
# Страница  http://geekbrains.ru есть в кэше, ее содержимое:
#  <Это текст страницы http://geekbrains.ru>
# Страница  http://google.com есть в кэше, ее содержимое:
#  <Это текст страницы http://google.com>
# Страница  http://yandex.ru не найдена в кэше, загружаем ее:
#  <Это текст страницы http://yandex.ru>
# Страница  http://google.com есть в кэше, ее содержимое:
#  <Это текст страницы http://google.com>
# Страница  http://yandex.ru есть в кэше, ее содержимое:
#  <Это текст страницы http://yandex.ru>
# Страница  http://google.com есть в кэше, ее содержимое:
#  <Это текст страницы http://google.com>
