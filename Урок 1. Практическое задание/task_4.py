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

users_list = {
    'user_1': {'user_name': 'user_1', 'password': 'password_1', 'active': 'True'},
    'user_2': {'user_name': 'user_2', 'password': 'password_2', 'active': 'False'},
    'user_3': {'user_name': 'user_3', 'password': 'password_3', 'active': 'True'},
    'user_4': {'user_name': 'user_4', 'password': 'password_4', 'active': 'True'}}


"""
Easy way O(1)
Более простое и наглядное решение.
Нет циклов.
"""

def user_check_1(users):
    typed_name = input('Type login name: ')
    if not users.get(typed_name):
        return "You haven't account yet. Please register first."
    print(f'Welcome, {typed_name}. ', end='')

    user_password = input('Type password: ')
    if users.get(typed_name).get('password') != user_password:
        return "Wrong password."

    if users.get(typed_name).get('active') == 'False':
        return "Your account not verified!"
    else:
        return f"Welcome, {typed_name}!"


"""
# Nightmare way O(n**2)
2 цикла for, много ветвлений, не наглядная структура.
"""

def user_check_2(users):
    typed_name = input('Type login name: ')
    for keys in users:
        if typed_name not in users.keys():
            return "You haven't account yet. Please register first."
        else:
            typed_password = input('Type password: ')
            for values in users.values():
                if typed_password == users.get(typed_name).get('password'):
                    if users.get(typed_name).get('active') == 'True':
                        return f'Welcome, {typed_name}'
                    return f'{typed_name}, Your account not verified!'
                else:
                    return 'Wrong password'


"""
# Hard way O(n)
because "for" detected, ветвления, не наглядная структура.
"""

def user_check_3(users):
    typed_name = input('Type login name: ')
    typed_password = input('Type password: ')
    for key, value in users.items():
        if key == typed_name:
            if value['password'] == typed_password:
                if value['active'] == 'True':
                    return f'Welcome, {typed_name}'
                elif value['active'] == 'False':
                    return f'{typed_name}, Your account not verified!'
            return "Wrong password."
        else:
            return "You haven't account yet. Please register first."


print(user_check_1(users_list))
print(user_check_2(users_list))
print(user_check_3(users_list))