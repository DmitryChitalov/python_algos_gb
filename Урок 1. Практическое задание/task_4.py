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


# Итовая сложность O (N)
def auth_1(all_users, user, passwd):
    for key, value in all_users.items():
        if key == user:
            if value['password'] == passwd and value['status']:
                return 'Authorization successfull!'
            elif value['password'] == passwd and not value['status']:
                return 'Please activate account!'
            else:
                return 'Wrong password!'
    return 'account does not exists or wrong password! Check creditinals or sing up'


# Итовая сложность O (1).
# этот вариант более эффективный.
def auth_2(all_users, user, passwd):
    if all_users.get(user):
        if all_users[user]['password'] == passwd and all_users[user]['status']:
            return 'Authorization successfull!'
        elif all_users[user]['password'] == passwd and not all_users[user]['status']:
            return 'Please activate account!'
        else:
            return 'Wrong password!'
    else:
        return 'account does not exists or wrong password! Check creditinals or sing up'


users = {'user1': {'password': '123', 'status': True},
         'user2': {'password': '123', 'status': True},
         'user3': {'password': '123', 'status': False}
         }

username = input('Введите логин: ')
password = input('Введите пароль: ')
print("var1")
print(auth_1(users, username, password))
print("var2")
print(auth_2(users, username, password))
