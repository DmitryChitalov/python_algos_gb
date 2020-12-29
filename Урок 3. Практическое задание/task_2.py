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
from uuid import uuid4


def check_user(user_name, password):
    user_data = users.get(user_name)
    if user_data is None:
        print('Такого пользователя нет')
        return False
    check_pass = hashlib.sha256(user_data[1].encode() + password.encode()).hexdigest()
    if user_data[0] == check_pass:
        return True
    return False


def add_user(name, password):
    user_data = users.get(name)
    if user_data is None:
        salt = uuid4().hex
        pass_hash = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
        print(f'хеш: {pass_hash}\tсоль: {salt}')
        users.update({name: [pass_hash, salt]})
        return True
    return False


users = {}
for i in range(10):
    add_user('user' + str(i), str(i)*4)
while True:
    ans = input('Выберите действие (+ - добавить пользователя, * - проверить пароль пользователя, 0 - выход):')
    if ans == '0':
        break
    if ans == '+' or ans == '*':
        u_name = input('Введите имя пользователя: ')
        u_pass = input('Введите пароль: ')
        if ans == '+':
            if add_user(u_name, u_pass):
                print('Пользователь добавлен!')
            else:
                print('Ошибка! Не удалось добавить пользователя!')
        else:
            if check_user(u_name, u_pass):
                print('Пароль верный!')
            else:
                print('Пароль неверный!')
