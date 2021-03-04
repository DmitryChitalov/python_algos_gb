"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (желательно хотя бы два)
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


# var 1 O(n)


# def authorization (users, user_name, user_password):
#     for key, value in users.items():
#         if key == user_name:
#             if value['password'] == user_password and value['activation']:
#                 return 'access granted'
#             elif value['password'] == user_password and not value['activation']:
#                 return 'account not activated'
#             elif value['password'] != user_password :
#                 return 'access denied'
#     return "user's not found"




# var 2 O(1)


def authorization (users, user_name, user_password):
    if users.get(user_name):
        if users[user_name]['password'] == user_password and users[user_name]['activation']:
            return 'access granted'
        elif users[user_name]['password'] == user_password and not users[user_name]['activation']:
            return 'account not activated'
        elif users[user_name]['password'] != user_password:
            return 'access denied'
    else:
        return "user's not found"

my_users = {
    'Main_user': {'p@ssword': '1234', 'activation': True},
    'Admin_user': {'passw0rd': '4567', 'activation': False},
    'Normal_user': {'PassWord': '4321', 'activation': True},
}
print (authorization(my_users, 'user4', '1111'))


# вариант 2 значительно более эффективен, поскольку отсутствие цикла существенно упрощает алгоритм,
# что может сыграть существенную роль при работе на "реальных" проектах со значительной нагрузкой

