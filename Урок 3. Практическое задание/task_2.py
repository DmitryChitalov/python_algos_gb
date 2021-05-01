"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш
Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""
import hashlib
import os

users = {}  # Простое демо хранилище

# Add a user
username = 'Brent'  # Имя пользователя
password = 'mypassword'  # Пароль пользователя

salt = os.urandom(32)  # Новая соль для данного пользователя
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
users[username] = {  # Хранение ключа и соли
    'salt': salt,
    'key': key
}

# Попытка проверки 1 (неправильный пароль)
username = 'Brent'
password = 'notmypassword'

salt = users[username]['salt']  # Получение соли
key = users[username]['key']  # Получение правильного ключа
new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

assert key != new_key  # Ключи не совпадают, следовательно, пароли не совпадают

# Попытка проверки 2 (правильный пароль)
username = 'Brent'
password = 'mypassword'

salt = users[username]['salt']
key = users[username]['key']
new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

assert key == new_key  # Ключи совпадают, следовательно, и пароли совпадают

# Добавление нового пользователя
username = 'Jarrod'
password = 'my$ecur3p@$$w0rd'

salt = os.urandom(32)  # Новая соль для данного пользователя
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
users[username] = {
    'salt': salt,
    'key': key
}

# Проверяем правильно ли введен пароль
username = 'Jarrod'
password = 'my$ecur3p@$$w0rd'

salt = users[username]['salt']
key = users[username]['key']
new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

assert key == new_key  # Ключи совпадают, поэтому совпадают пароли и у этого пользователя

"""
# -*- coding: utf-8 -*-
import re

login = input('123')
password =input('123')

test = True

def main():
    if test == True:
        print ('Привет {}'.format(login))
    else: print ('Кто-то пытался притвориться пользователем {}, но в пароле допустил ошибку:{}.'.format(login, name_error))


def askPassword(success, failure):
    global test
    global name_error
    vowels = ('e', 'y', 'u', 'i', 'o', 'a')
    kolvo_vowels = 0
    for i in vowels:
        kolvo_vowels += int(failure.count(i))

    if kolvo_vowels > 2:
        consonants = int(len(re.findall(r'\w', failure))) - int(len(re.findall(r'\d', failure))) - kolvo_vowels
        if consonants == kolvo_vowels:
            if consonants > 2:
                return success
                main()
            else:
                test = False
                name_error = str('Wrong consonants').upper()
                main()
                print ('{} Wrong consonants'.format(success))
                return failure
        else:
            test = False
            name_error = str(Everything is wrong).upper()
            main()
            print ('{} Everything is wrong'.format(success))
            return failure
    else:
        test = False
        print ('{} Wrong number of vowels'.format(success))
        name_error = str('Wrong number of vowels').upper()
        main()
        return failure

askPassword(login, password)
"""

"""
vowels = set('aeiouy')
consonants = set(chr(n) for n in range(ord('a'), ord('z') + 1) if chr(n) not in vowels)
messages = ['', 'Wrong number of vowels', 'Wrong consonants', 'Everything is wrong']

def check_passord(login, password):
    def filter_consonants(s):
        return [c for c in s if c in consonants]
    r1 = 0 if sum(1 for c in password if c in vowels) == 3 else 1
    r2 = 0 if filter_consonants(login) == filter_consonants(password) else 2
    return messages[r1 + r2]

def askPassword(success, failure):
    login =    input().lower()
    password = input().lower()
    message = check_password(login, password)
    if message:
        failure(login, message)
    else:
        success(login)

def main():
    def say_hello(login):
        print(f'Привет {login}')
    def report_error(login, message):
        print(f'Кто-то пытался притвориться пользователем {login}, но в пароле допустил ошибку: {message}.')
    askPassword(say_hello, report_error)
"""
