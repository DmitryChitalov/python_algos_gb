"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import uuid 
import hashlib
class Cash_pages:
    cash = []

    def __init__(self, url):
        self.url = url

    def check_url_page(self):
        if self.url in self.cash:
            return f'Такая страница уже находится в кэше'
        else:
            return self.append_page()

    def append_page(self):
        Cash_pages.cash.append(self.url)
        return self.hex_s()
    
    def hex_s(self):
        salt = uuid.uuid4().hex
        hex_url = hashlib.sha256(salt.encode() + self.url.encode()).hexdigest()
        return hex_url, self.url

url1 = Cash_pages('123.00.223.90')
url2 = Cash_pages('124.00.223.90')
url3 = Cash_pages('123.00.223.90')

print(url1.check_url_page())
print(url2.check_url_page())
print(url3.check_url_page())




        