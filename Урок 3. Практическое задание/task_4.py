"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""


class CashUrl:
    import hashlib
    from uuid import uuid4
    __urls = {}
    salt = uuid4().hex

    def set_url(self, url):
        hash_url = self.hashlib.sha256(self.salt.encode() + url.encode()).hexdigest()
        if self.__urls.get(hash_url):
            print(f"{url} уже в кэше")
        else:
            self.__urls[hash_url] = url

    def print_cashed_urls(self):
        for key, valee in self.__urls.items():
            print(f"ключ {key} :: url {valee}")


cash_url = CashUrl()

cash_url.set_url("www.mail.ru")
cash_url.set_url("www.aport.ru")
cash_url.set_url("www.mail.ru")
cash_url.print_cashed_urls()
