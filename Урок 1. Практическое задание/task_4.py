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
def authentication_1(users, user_name, user_pass):
    for key, value in users.items():
        if key == user_name:
            if value['password'] == user_pass and value['activation']:
                return 'Welcome'
            elif value['password'] == user_pass and not value['activation']:
                return 'Declined'
            elif value['password'] != user_pass:
                return 'Password is incorrect'
    return 'No such user'


# Сложность: O(1)
def authentication_2(users, user_name, user_pass):
    if users.get(user_name):
        if users[user_name]['password'] == user_pass and users[user_name]['activation']:
            return 'Welcome'
        elif users[user_name]['password'] == user_pass and not users[user_name]['activation']:
            return 'Declined'
        elif users[user_name]['password'] != user_pass:
            return 'Password is incorrect'
    else:
        return 'No such user'


users = {'user_1': {'password': '123', 'activation': True},
         'user_2': {'password': '213', 'activation': True},
         'user_3': {'password': '321', 'activation': False}
}

print(authentication_1(users, 'user_1', '123'))
print(authentication_1(users, 'user_4', '123'))
print(authentication_2(users, 'user_2', '123'))
print(authentication_2(users, 'user_3', '321'))

# Второй вариант лучше, так как сложность - константная, в первой варианте сложность - линейная.
