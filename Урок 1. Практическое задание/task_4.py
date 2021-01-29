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


class User:
    users = {}

    def __init__(self, login, password, is_activated):
        self.login = login
        self.password = password
        self.is_activated = is_activated
        users[login] = password, is_activated


def check(login_value, password_value):  # итоговая сложность: константная

    if login_value not in users:  # сложность — константная (1)
        print('Такого логина не существует. Пройдите регистрацию')  # сложность — константная (1)

    else:
        if users[login_value][0] != password_value:  # сложность — константная (1)
            print('Неверный пароль')  # сложность — константная (1)
        else:
            if users[login_value][1] == 1:  # сложность — константная (1)
                print('Авторизация прошла')  # сложность — константная (1)
            else:
                print('Ваш аккаунт не активирован. Пройдите активацию')  # сложность — константная (1)

    return None   # сложность: константная (1)


def check_v2(login_value, password_value):
    if login_value not in users:  # сложность — константная (1)
        print('Такого логина не существует. Пройдите регистрацию')  # сложность — константная (1)

    else:
        if users[login_value][0] == password_value and users[login_value][1] == 1:  # сложность — константная (1)
            print('Авторизация прошла')  # сложность — константная (1)
        elif users[login_value][0] == password_value and users[login_value][1] == 0:  # сложность — константная (1)
            print('Ваш аккаунт не активирован. Пройдите активацию')  # сложность — константная (1)
        else:
            print('Неверный пароль')  # сложность — константная (1)
    return None  # сложность — константная (1)