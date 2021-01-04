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

db_user = {
    'User1': ['user1', 'pswuser1', 0],
    'User2': ['user2', 'pswuser2', 1],
    'User3': ['user3', 'pswuser3', 1],
    'User4': ['user4', 'pswuser4', 1],
    'User5': ['user5', 'pswuser5', 1],
    'User6': ['user6', 'pswuser6', 1],
    'User7': ['user7', 'pswuser7', 1],
    'User8': ['user8', 'pswuser8', 0],
    'User9': ['user9', 'pswuser9', 1],
    'User10': ['user10', 'pswuser10', 0]
}


def auth_1(db_user, user, lgn, psw):  # O(1)
    if db_user[user][2] and db_user[user][0] == lgn and db_user[user][1] == psw:  # O(1)
        return 'Please proceed to the web site'  # O(1)
    elif db_user[user][2] and (db_user[user][0] != lgn or db_user[user][1] != psw):
        return 'Access denied'  # O(1)
    else:
        answ = input('Please continue your activation: [N] - NO, [Y] - YES ')  # O(1)
        if answ.lower() == 'yes':  # O(1)
            db_user[user][2] = 1  # O(1)
            return 'Please proceed to the web site'  # O(1)
        else:
            return 'Access denied'  # O(1)


print(auth_1(db_user, 'User6', 'user6', 'pswuser6'))
print(auth_1(db_user, 'User6', 'user6', 'pswuser7'))
print(auth_1(db_user, 'User10', 'user10', 'pswuser10'))


def auth_1(db_user,lgn, psw):
    for el in db_user.values():  # O(N)
        if el[0] == lgn:
            if el[1] == psw and el[2]:
                return 'Please proceed to the web site'  # O(1)
            elif el[1] != psw:
                return 'Access denied'  # O(1)
            else:
                return 'Please continue your activation'


print('#' * 35, '\n', '#' * 35)
print(auth_1(db_user, 'user6', 'pswuser6'))
print(auth_1(db_user, 'user6', 'pswuser7'))
print(auth_1(db_user, 'user1', 'pswuser1'))

# Оптимально использовать первый алгоритм, так как сложность вычисления ниже
