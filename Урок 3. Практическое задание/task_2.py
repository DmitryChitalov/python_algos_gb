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

def hash_creator(line):
    return hashlib.sha256(bytes(line) + bytes((str(pow(len(line), 2))*len(line)).encode(encoding='UTF=8'))).hexdigest()

pwd = str(input("Enter your password: ")).encode(encoding='UTF=8')
hash_pwd = hash_creator(pwd)
print(hash_pwd)

check_pwd = str(input("Enter your password: ")).encode(encoding='UTF=8')
hash_tpwd = hash_creator(check_pwd)
print(hash_tpwd)

if hash_pwd == hash_tpwd:
    print("Correct")
else:
    print("Access denied!")





