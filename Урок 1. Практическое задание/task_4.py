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


# Функция #1 Линейная. Jптимальная, так как использует только 1 цикл for in

def user_login(users, users_input):
    login = False
    password = False
    auth = False
    for k, v in users.items():
        user = v
        if user['login'] == users_input['login']:
            login = True
        else:
            login = False
        if user['password'] == users_input['password']:
            password = True
        else:
            password = False
        if user['authorisation']:
            auth = True
        else:
            auth = False
        if login and password and auth:
            break

    if login & password & auth:
        print('Вам разрешен вход')
    if not auth:
        print('Вы не прошли авторизацию. Пройдите ее')
    if not password:
        print('Вы ввели не правильный пароль')
    if not login:
        print('Вы ввели не правильный логин')


# Функция #2. O(n^2). Функция не оптимальна, так как использует два цикла for in, а это - квадратичная функция.
def user_login_2(users, users_input):
    login = False
    password = False
    auth = False
    pass_in = ()

    for k, v in users.items():
        for i in v:
            if i == 'login':
                if v[i] == users_input['login']:
                    login = True
                else:
                    login = False
            if i == 'password':
                if v[i] == users_input['password']:
                    password = True
                else:
                    password = False
            if i == 'authorisation':
                if v[i] == True:
                    auth = True
                else:
                    auth = False
            if login and password and auth:
                break

    if login & password & auth:
        print('Вам разрешен вход')
    if not auth:
        print('Вы не прошли авторизацию. Пройдите ее')
    if not password:
        print('Вы ввели не правильный пароль')
    if not login:
        print('Вы ввели не правильный логин')




# Словарь с сохраненными пользователями
users = {'user_1':
    {
        'login': 'login_1',
        'password': 'password_1',
        'authorisation': True
    },

    'user_2':
        {
            'login': 'login_2',
            'password': 'password_2',
            'authorisation': False
        }
}

# Ввод пользователя
users_input = {'login': 'login_1',
               'password': 'password_1'}

# Запуск функций
user_login(users, users_input)
