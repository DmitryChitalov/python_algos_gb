"""
Задание 4.
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
# Вариант 1
# Решение через ООП
# (Общая сложность алгоритма O(n))


class User:
    def __init__(self, login, password, is_active_check):
        self.login = login
        self.__password = password
        self.__is_active = is_active_check

    def show_password(self, password):
        return self.__password == password

    def is_active_check(self):
        return self.__is_active

    def activation(self):
        self.__is_active = True

    def deactivation(self):
        self.__is_active = False


class StorageInfo:
    def __init__(self):
        self.__current_index = 0
        self.data = []
        self.index_data = dict()

    def save_info(self, info):
        self.data.append(info)
        self.index_data.update({info.name: self.__current_index})
        self.__current_index += 1

    def search_info(self, name):
        for el in self.data:
            if el.name == name:
                return el


# Вариант 2
# Цикл (Общая сложность алгоритма O(n))

def auth(users, user_name, user_passwd):
    for key, value in users.items():
        if key == user_name:
            if value['password'] == user_passwd and value['activation']:
                return 'Ура!Пользователь может быть допущен к ресурсу'
            elif value['password'] == user_passwd and not value['activation']:
                return 'Учетная запись не активна, для доступа к ресурсу активируйте свою учетную запись!'
            elif value['password'] != user_passwd:
                return 'Пароль не верный'

    return 'Такого пользователя не существует'

# сравнить какое из этих решений лучше для меня проблемно, оба они имеют линейную сложность,
# однако певрый вариант мне кажется более масштабируемым, а второй может занимать больше памяти,
# так как отдельно нужно хранить словарь пользователей
