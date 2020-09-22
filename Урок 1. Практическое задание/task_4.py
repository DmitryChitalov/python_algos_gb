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
# Вариант 1: Сложность : O(1) - более удачная реализация


def check_usr_1(users, usr_name, usr_pass):
    usr_check = users.get(usr_name)
    if usr_check is not None:
        if usr_check[0] == usr_pass and usr_check[1]:
            return 'Welcome !'
        elif usr_check[0] == usr_pass and not usr_check[1]:
            return 'You are ot activated yet'
        elif usr_check[0] != usr_pass:
            return 'Wrong password'
    else:
        return 'Unknown user'


# Вариант 2: Сложность :  O(n)  Наличие цикла, делает этот вариант менее эффективным.


def check_usr_2(users, usr_name, usr_pass):
    for some_k, some_v in users.items():
        if some_k == usr_name:
            if some_v[0] == usr_pass and some_v[1]:
                return 'Welcome !'
            elif some_v[0] == usr_pass and not some_v[1]:
                return 'You are ot activated yet'
            elif some_v[0] != usr_pass:
                return 'Wrong password'
    return 'Unknown user'


some_users = {'First': ['Pass', True], 'Second': ['addaZ', False], 'Third': ['zack54', True]}
print(check_usr_1(some_users, 'First', 'Pass'))
print(check_usr_1(some_users, 'Second', 'addaZ'))
print(check_usr_1(some_users, 'Third', 'addaZ'))

print(check_usr_2(some_users, 'Third', 'addaZ'))
print(check_usr_2(some_users, 'First', 'Pass'))