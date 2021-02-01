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


# O(n) - неэффективное
class User(object):
    def __init__(self, username, password, is_activated=False):
        self.username = username
        self.password = password
        self.is_activated = is_activated


def check_access(users_lst, username, password):
    for i in range(len(users_lst)):
        if users_lst[i].username == username:
            if users_lst[i].password != password:
                break
            elif not users_lst[i].is_activated:
                print('Необходимо пройти активацию учётной записи')
                return
            else:
                print('Пользователь может быть допущен')
                return
    print('Неверный пользователь или пароль')
    return


# O(1) - эффективное
class UserRepository(object):
    def __init__(self, users_list):
        self.rep = {u[0]: (u[1], u[2]) for u in users_list}

    def add(self, username, password, is_activated=False):
        self.rep[username] = (password, is_activated)

    def pop(self, username):
        return self.rep.pop(username)

    def check_access(self, username, password):
        user_rec = self.rep.get(username)
        if user_rec is None or user_rec[0] != password:
            print('Неверный пользователь или пароль')
            return
        elif not user_rec[1]:
            print('Необходимо пройти активацию учётной записи')
            return
        else:
            print('Пользователь может быть допущен')
            return


users = [('A', 'qwerty', True), ('B', 'password', False), ('C', 'alligator', True)]
ur = UserRepository(users)
# ur.add('D', 'asdfg')
# ur.pop('C')

ur.check_access('B', 'password')
