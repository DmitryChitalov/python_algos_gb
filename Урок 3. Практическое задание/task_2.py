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
import hashlib as h

users = {
    'user' + str(i):
        h.sha256(('user' + str(i) + 'password' + str(i)).encode()).hexdigest()
    for i in range(10)
}


class User:

    def is_user_exists(self, username):
        return username in users.keys()


    def create_user(self):
        username = input('Введите имя нового пользователя: ')
        if self.is_user_exists(username):
            print('Такой пользователь уже существует!')
            return
        else:
            password = input('Введите пароль для нового пользователя: ')
            users[username] = \
                h.sha256((username + password).encode()).hexdigest()
            return

    def login(self):
        login = input('Введите логин пользователя: ')
        if not self.is_user_exists(login):
            print('Пользователь не зарегистрирован в системе!')
            return
        else:
            password = input('Введите пароль пользователя: ')
            password = h.sha256((login + password).encode()).hexdigest()
            print(f'В базе данных хранится строка {password}')
            password = input('Введите пароль пользователя '
                             'еще раз для проверки: ')
            password = h.sha256((login + password).encode()).hexdigest()
            if users[login] == password:
                print('Вы успешно вошли в систему!')
                return
            else:
                print('Неверный пароль, доступ запрещен!')
                return





for i in users.keys():
    print(i)
user = User()
user.create_user()
user.create_user()
for i in users.keys():
    print(i)
user.login()