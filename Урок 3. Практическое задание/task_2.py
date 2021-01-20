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
def password_creater():
    password=hashlib.sha256(input('Введите пароль: ').encode()).hexdigest()
    print('В базе данных хранится строка:', password)
    password_check= hashlib.sha256(input('Введите пароль еще раз для проверки: ').encode()).hexdigest()
    if password == password_check:
        file = open("passwords.txt", "w")
        file.write(password)
        file.close()
        return 'Пароль верный, пароль записан'
    else:
        i = 3
        print(f'Неверно. У вас осталось 3 попытки')
        while password != password_check and i > 0:
            if password == password_check:
                file = open("passwords.txt", "w")
                file.write(password)
                file.close()
                return 'Пароль верный, пароль записан'
            else:
                password_check = hashlib.sha256(input('Введите пароль еще раз для проверки: ').encode()).hexdigest()
                print(f'У вас осталось {i} попыток')
                i-=1
        return 'Попытки закончились'


print(password_creater())