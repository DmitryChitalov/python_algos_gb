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
def get_salt():
    """
    Функция создания соли.
    :return: str
    """
    import uuid
    return uuid.uuid4().hex

def hashing(passw: str, salt):
    """
    Функция хеширования введенного пароля.
    :param passw: str
    :return: hash
    """
    import hashlib
    return hashlib.sha256(salt.encode() + passw.encode()).hexdigest()

def auth(passw: str, hash_obj, salt):
    """
    Функция проверки пароля.
    :param passw: str
    :param hash_obj: str
    :param salt:str
    :return:None
    """
    if hashing(passw, salt) == hash_obj:
        print('Введён правильный пароль.')
    else:
        print('Пароль неверен!')
    return

if __name__ == '__main__':
    salt = get_salt()
    passw = hashing(input('Введите пароль: '), salt)
    print(f'В базе данных хранится строка: {passw}')
    auth(input('Введите пароль ещё раз для проверки: '), passw, salt)