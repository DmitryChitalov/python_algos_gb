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

# Решение #1.

USERS_1 = [
    {"login": "lev", "password": "gn4o3bgg", "verify": True},
    {"login": "prav", "password": "asd032fng3", "verify": False},
    {"login": "alexsei", "password": "yfdfkmysq", "verify": True},
    {"login": "gosha", "password": "asndkjdxf", "verify": False},
    {"login": "nikita", "password": "209hg43", "verify": False},
    {"login": "danil228", "password": "x2398f2", "verify": True},
    {"login": "sasha", "password": "v3094", "verify": False},
]


def do_auth_1(login, password):
    for one_user in USERS_1: # O(N)
        if one_user["login"] == login and one_user["password"] == password:  # O(1)
            if one_user["verify"]:  # O(1)
                print(f'[v] Пользователь {login} допущен к ресурсу.')
            else:
                print(f'[!] Пользователь {login} не прошел активацию.')
            return
    print(f'[x] Пользователь {login} не найден!')

# Итого: O(N)

do_auth_1(login='sergey', password='293gns9df') # Не существует.
do_auth_1(login='gosha', password='asndkjdxf') # Не активировал запись.
do_auth_1(login='alexsei', password='yfdfkmysq') # Допущен к ресурсу.
print()

##########################################################################################################

# Решение #2.

USERS_2 = {
    "lev": {"password": "gn4o3bgg", "verify": True},
    "prav": {"password": "asd032fng3", "verify": False},
    "alexsei": {"password": "yfdfkmysq", "verify": True},
    "gosha": {"password": "asndkjdxf", "verify": False},
    "nikita": {"password": "209hg43", "verify": False},
    "danil228": {"password": "x2398f2", "verify": True},
    "sasha": {"password": "v3094", "verify": False},
}


def do_auth_2(login, password):
    if USERS_2.get(login, {}).get('password') == password: # O(1)
        if USERS_2[login]["verify"]: # O(1)
            print(f'[v] Пользователь {login} допущен к ресурсу.')
        else:
            print(f'[!] Пользователь {login} не прошел активацию.')
    else:
        print(f'[x] Пользователь {login} не найден!')

# Итого: O(1)

do_auth_2(login='sergey', password='293gns9df') # Не существует.
do_auth_2(login='gosha', password='asndkjdxf') # Не активировал запись.
do_auth_2(login='alexsei', password='yfdfkmysq') # Допущен к ресурсу.

'''
Решение №2 эффективнее, т.к. мы не пробегаем по всему списку, проверяя каждый элемент, а напрямую
обращаемся к нему. А только затем проверяем его значение.
'''
