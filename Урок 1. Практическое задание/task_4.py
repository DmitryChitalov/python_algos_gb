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

"""Алгоритм 1. Сложность O(N)"""

users = [{'name': 'Kate', 'sign': {'password': '12345', 'activated': True}},
         {'name': 'Max', 'sign': {'password': '54321', 'activated': False}},
         {'name': 'Leo', 'sign': {'password': 'qwerty', 'activated': True}}
         ]


def login_check(usr_name, users):
    for user in users:
        if usr_name == user['name']:
            return user


def sign_in_check(passwd, user):
    if passwd == user['sign']['password'] and user['sign']['activated'] is True:
        print('Вход выполнен')
    elif passwd != user['sign']['password']:
        print('Пароль неверный')
    elif not user['sign']['activated']:
        print('Пожалуйста, активируйте вашу учётную запись')


user_name, password = 'Kate', '12345'
user = login_check(user_name, users)

if not user:
    print('Пользователь с таким именем не существует')
else:
    sign_in_check(password, user)


"""Алгоритм из гита, сложность O(1)"""


def check_usr_1(users, usr_name, usr_pass):
    usr_check = users.get(usr_name)
    if usr_check is not None:
        if usr_check[0] == usr_pass and usr_check[1]:
            return 'Welcome !'
        elif usr_check[0] == usr_pass and not usr_check[1]:
            return 'You are not activated yet'
        elif usr_check[0] != usr_pass:
            return 'Wrong password'
    else:
        return 'Unknown user'


some_users = {'First': ['Pass', True], 'Second': ['addaZ', False], 'Third': ['zack54', True]}
print(check_usr_1(some_users, 'First', 'Pass'))
print(check_usr_1(some_users, 'Second', 'addaZ'))
print(check_usr_1(some_users, 'Third', 'addaZ'))
print(check_usr_1(some_users, 'Fourth', 'addaZ'))
