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
    def __init__(self, login, pwd):
        self._login = login
        self._pwd = pwd
        self._is_active = False

    def __hash__(self):
        return hash(self._login)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._login == other._login
        return self._login == other

    @property
    def is_active(self):
        return self._is_active

    def activate(self):
        self._is_active = True

    def __str__(self):
        return f'login: {self._login}, password: {self._pwd}, is active: {self._is_active}'


class Site:
    def __init__(self):
        self._users = dict()

    @staticmethod
    def _question():
        return input('User not found. For add new one press <a>, for cancel press any other key: ') == 'a'

    def check_user(self, login):
        res = self._users.get(login) # O(1)
        if res is None and Site._question():
            res = self._add_user(login)
        elif not res.is_active:
            res.activate()

        return res

    def _add_user(self, login):
        new_user = User(login, input('pwd:'))
        new_user.activate()

        return self._users.setdefault(login, new_user) # O(1)


site = Site()
print(site.check_user('test_user'))
print(site.check_user('test_user'))