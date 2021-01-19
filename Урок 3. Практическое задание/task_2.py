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
import os


class UserManager:
    """
    Класс для создания пользователей и аутентификации
    """
    @staticmethod
    def create_usr(usr_id, passwd):
        """
        Метод для создания нового юзера
        """
        salt = usr_id
        if os.path.isfile('save_pass'):
            with open('save_pass', 'r') as f_in:
                lin = f_in.readlines()
            for elem in lin:
                if elem.find(usr_id) >= 0:
                    raise Exception('Пользователь с таким ником уже существует')
        else:
            open('save_pass', 'w')
        hash_obj = hashlib.new('sha512')
        hash_obj.update((passwd + salt).encode('utf-8'))
        with open('save_pass', 'a') as f_out:
            f_out.write(f'{usr_id} {hash_obj.hexdigest()}\n')
        print('Пользователь успешно создан!')


    @staticmethod
    def auth_usr(user_id, passwd):
        """
        Метрод аутентификации юзера
        """
        salt = user_id
        if os.path.isfile('save_pass'):
            cnt = -1
            with open('save_pass', 'r') as f_in:
                lin = f_in.readlines()
            for i, elem in enumerate(lin):
                if elem.find(user_id) >= 0:
                    cnt = i
                    break
            if cnt == -1:
                print('Аутентификация не пройдена!')
                return
        else:
            raise Exception('Файл с данными пользователей не найден')
        passwd_ident = lin[i].split(' ')[1][:-1]
        hash_obj = hashlib.new('sha512')
        hash_obj.update((passwd + salt).encode('utf-8'))
        if str(hash_obj.hexdigest()) == passwd_ident:
            print(f'Добро пожаловать {user_id} !')
        else:
            print('Аутентификация не пройдена!')


if __name__ == '__main__':
    usr = UserManager()
    usr.create_usr('kk', '123qwe')
    usr.auth_usr('kk', '123qwe')
    usr.auth_usr('LLgg', '123qwen')



