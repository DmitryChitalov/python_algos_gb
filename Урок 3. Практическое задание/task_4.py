"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib


salt = b'just salt'
hashed_urls = [b'www.yandex.ru', b'www.rbc.ru', b'www.google.com', b'www.mail.ru']
stored_hashes = []

def generate_hashes(url, salt):
    hash_record = hashlib.sha256(url + salt).hexdigest()
    return hash_record

# generating stored hashes
for i in range(len(hashed_urls)):
    stored_hashes.append(generate_hashes(hashed_urls[i],salt))

print (f'сохраненные хеши: {stored_hashes}')

input_url = input('введите URL:').encode()
input_url_hash = generate_hashes(input_url, salt)
print (f'hash введенного URL:{input_url_hash}')

if input_url_hash in stored_hashes:
    print ('страница присутствует в кэше')
else:
    print ('страница отсутствует в кэше')
    stored_hashes.append(input_url_hash)
    print('страница добавлена в кэш')
    print(f'обновленный список хешей:{stored_hashes}')