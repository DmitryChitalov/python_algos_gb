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

# 1) Сложность О(1)
class Auth:
    def __init__(self, login, passwd, authoriz=True):
        self.login = login
        self.passwd = passwd
        self.authoriz = authoriz
    def __check__(self):
        if self.authoriz == True:
            return f'Passed'
        else:
            return f'You`ll need to activate your acc'


first = Auth('john', 'Abaas', True)
second = Auth('jane', 'Bas123', True)
third = Auth('dave', 'Bopo123', False)

print(first.__check__())
print(second.__check__())
print(third.__check__())

# 2) Сложность О(1)

users_dict = {'user1': { 'passwd': 'ffA', 'authorized': True}, 
'user2': { 'passwd': 'ddaffA', 'authorized': True}, 
'user3': {'passwd': 'dddaB', 'authorized': False}}

def check_auth(login, passwd, authorized):
    if login in users_dict:
        if users_dict[login]['passwd'] == passwd:
            if authorized == True:
                return f'Passed'
            else:
                return f'You`ll need to activate your acc'
    else:
        return f'Wrong login name'


print(check_auth('user3', 'dddaB', False))
print(check_auth('user2', 'ddaffA', True))
print(check_auth('user4', 'ddaffA', True))

""" Оба варианта имеют константную сложность, оба варианта оптимальны """