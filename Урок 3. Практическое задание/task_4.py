"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""


from hashlib import sha256

#Класс таблицы url и хешей
class UrlHash:
    url_hashes = {}
    salt = "Солёная соль"

    def __init__(self, my_salt: str):
        self.url_hashes = {}
        self.salt = my_salt

# Добавлние в кэш соответствующий url
    def add_url_hash(self, url: str):
        hash_url = sha256(self.salt.encode("UTF-8") + url.encode("UTF-8")).hexdigest()
        self.url_hashes[hash_url] = url
        return hash_url

# Возвращение из кэша url
    def get_url_hash(self, url_hash: str):
        return self.url_hashes.get(url_hash)


my1 = UrlHash("Добавим немножко соли")

while True:
    url1 = input("Введите url (enter без данных завершить): ")
    if url1 == "":
        break

    print(f"Хеш {url1} = {my1.add_url_hash(url1)}")

print(my1.url_hashes)

