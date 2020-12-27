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


class UrlCash:
    """Реализация объекта url-кэш."""
    __cash = []
    __salt = uuid4().hex

    def __init__(self, url):
        """Получение url и вызов функции хеширования."""
        self.url = url
        self.url_hashing()

    def __repr__(self):
        """Определяет вид объекта."""
        return self.url

    def url_hashing(self):
        """Хеширует url и проверяет его наличие в кэше."""
        url_hash = hashlib.sha256(UrlCash.__salt.encode() + self.url.encode()).hexdigest()
        if url_hash not in UrlCash.__cash:
            UrlCash.__cash.append(url_hash)

    @staticmethod
    def count_url():
        """Вернуть значение количества url содержащихся в хэше."""
        return len(UrlCash.__cash)


if __name__ == '__main__':
    # Добавляем несколько url
    a = UrlCash('https://github.com/')
    b = UrlCash('https://habr.com/')

    print('Проверяем количество адресов в кэше: ')
    print(UrlCash.count_url())

    # Пробуем добавить один из адресов повторно
    c = UrlCash('https://github.com/')
    print('\nПроверяем количество адресов в кэше еще раз: ')
    print(UrlCash.count_url())

    print('\nВид объекта: ')
    print(a)

