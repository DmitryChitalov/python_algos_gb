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
import hashlib , uuid, json

def check_password():
    password = input("Введите пароль: ")
    salt = uuid.uuid4().hex
    database_hash = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    with open("db_hash.txt","wb") as f:
        db_dict = {}
        db_dict["db_hash"] = database_hash
        f.write(json.dumps(db_dict).encode())

    print("В базе данных хранится строка:", database_hash)
    confirm_password = input("Введите пароль еще раз для проверки: ")
    confirm_hash = hashlib.sha256(salt.encode() + confirm_password.encode()).hexdigest()
    with open("db_hash.txt","rb") as f:
        obj = json.load(f)
    if obj["db_hash"] == confirm_hash:
        print("Вы ввели правильный пароль")
    else:
        print("Вы ввели неправильный пароль")

check_password()
