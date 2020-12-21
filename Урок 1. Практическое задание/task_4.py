"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

import hashlib

# p = hashlib.md5(bytes(input('Create password:\n'), 'cp1251')) -- как вариант
p = hashlib.md5(b'superpuperpassword')
p = p.hexdigest()

user_dict = {
    'user_1': {'password': p, 'activation': True},
    'user_2': {'password': p, 'activation': False},
    'user_3': {'password': p, 'activation': True},
    'user_4': {'password': p, 'activation': False}
}


def authorisation1(us_dict, name, pas):                  # O(n) -- общая сложность
    for key, value in us_dict.items():                                               # O(n)
        if key == name:
            if value['password'] == pas and value['activation'] is True:             # O(1)?
                return 'Welcome!'
            elif value['password'] == pas and value['activation'] is False:
                return 'Complete the activation process'
            elif value['password'] != pas:
                return 'Password is not correct'
    return 'A user with this name was not found'


# psw = hashlib.md5(bytes(input('Enter password:\n'), 'cp1251')) -- как вариант
psw = hashlib.md5(b'superpuperpassword')
psw1 = hashlib.md5(b'superrrpuperpassword')
print(authorisation1(user_dict, name='user_1', pas=psw.hexdigest()))
print(authorisation1(user_dict, name='user_9', pas=psw.hexdigest()))
print(authorisation1(user_dict, name='user_1', pas=psw1.hexdigest()))
"""Сложность O(n)"""
print('-' * 79)


def authorisation2(us_dict, name, pas):   # O(1) -- общая сложность, т.к. далее в функции везде константы
    if us_dict.get(name):
        if us_dict[name]['password'] == pas and us_dict[name]['activation'] is True:
            return 'Welcome!'
        elif us_dict[name]['password'] == pas and us_dict[name]['activation'] is not True:
            return 'Complete the activation process'
        elif us_dict[name]['password'] != pas:
            return 'Password is not correct'
    else:
        return "Who are you? You'd better go!"


print(authorisation2(user_dict, name='user_1', pas=psw.hexdigest()))
print(authorisation2(user_dict, name='user_9', pas=psw.hexdigest()))
print(authorisation2(user_dict, name='user_1', pas=psw1.hexdigest()))
print('-' * 79)


