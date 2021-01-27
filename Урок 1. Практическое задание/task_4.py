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

def activate_user(user_name):
    """процедура активации пользователя

    Сложность O(n)
    """

    act = str(input("Пользователь не активирован. Активировать? (Y - для активации): "))

    if act == "Y":
        for i in USERS:
            if USERS[i]['name'] == user_name:
                USERS[i]['active'] = True
        return True
    return False


def check_user1(user_name, user_pass):
    """проверяем корректность пароля и активен пользователь или нет.
    Если не активен, то предлагаем активироваться

    Сложность O(n)
    """

    res = list(filter(lambda x: x.get('name') == user_name, USERS.values()))

    if not res:
        return "Пользователь не найден"

    if res[0]['password'] != user_pass:
        return "Введен не правильный пароль"

    if not res[0]['active']:
        if not activate_user(user_name):
            return "Пользователь не активен"

    return "Успешная авторизация"


#Задаем список пользователей
USERS = {'usr1': {'name': "root", 'password': "123456", 'active': True},
         'usr2': {'name': "admin", 'password': "admin", 'active': True},
         'usr3': {'name': "oper", 'password': "qwerty", 'active': True},
         'usr4': {'name': "test", 'password': "zxc", 'active': False},
         'usr5': {'name': "user", 'password': "123", 'active': False}
        }

print(USERS)

USR=str(input("Введите имя пользователя: "))
PASSWD=str(input("Введите пароль: "))

print(check_user1(USR, PASSWD))

print(USERS)
