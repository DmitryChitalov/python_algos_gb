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


class UserInfo:
    def __init__(self, name, password, is_active):
        self.name = name
        self.__password = password
        self.__is_active = is_active

    def activate(self):
        self.__is_active = True

    def is_active(self):
        return self.__is_active

    def check_password(self, password):
        return self.__password == password

    def deactivate(self):
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

    """ Вариант первый, простой перебор массива 
        сложность O(n)
        Скрипт аутентификации выполняется линейно, сложность  константная O(1) 
    """
    def search_info(self, name):
        for el in self.data:  # O(n)
            if el.name == name:
                return el

    """ Вариант второй, для индексации используется словарь.
        сложность O(1), но требуется больше памяти, т.к. хранится еще словарь 
        Операция аутентификации более частая, чем регистрации(добавление логин-пароль-флаг активности)
    """
    def search_info2(self, name):
        index = self.index_data.get(name)  # O(1)
        if index:
            return self.data[index]  # 0(1)


def auth_script():
    info = StorageInfo()
    info.save_info(UserInfo('Vasya', 'qweasd', False))
    info.save_info(UserInfo('Masha', 'qweasd', True))
    info.save_info(UserInfo('Petya', 'qweasd', True))
    while True:
        user = info.search_info2(input('Введите имя пользователя'))  # можно заменить на search_info, работать будет
        if user:
            password = input('Ввведите пароль')
            if user.check_password(password):
                if user.is_active():
                    print('аутентификация успешна, ура')
                    break
                else:
                    activate_phrase = input('учетная запись неактивна. активировать?(yes/no)')
                    if activate_phrase == 'yes':
                        user.activate()
                        print('учетная запись активирована, \nаутентификация успешна, ура')
                        break
            else:
                print('Пароль неверен')
        else:
            print('Нет такого логина')


if __name__ == '__main__':

    auth_script()




