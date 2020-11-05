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

"""
Допустим мы получили данные c какой нить Redis (ключ - значение) или вытянули в неком json формате  :

Сложность O(n)
"""
users = [
    {'num': 0, "login": 'root', 'password': '12345678', 'status': True},
    {'num': 1, "login": 'ma', 'password': '1234', 'status': True},
    {'num': 2, "login": 'sa', 'password': '123456', 'status': False},
]


def check_login (users_mass, login):
    for i in users_mass:
        if (i['login']) == login:
            return i["num"]


def complite_autorication(x):
    if input("Вы не авторизированы,  хотите пройти авторизацию(Y/N)").lower().strip(" ") == 'y':
        x.update({'status': True})
        return print("Вы авторизованы")
    else:
        return print("Ну ладно((")

def autorisation(login, password, user_mass):
    foo = check_login(user_mass, login)
    if foo is not None:
        if user_mass[foo]['password'] == password:
            print("Добро пожаловать")
            if user_mass[foo]['status'] is False:
                complite_autorication(user_mass[foo])
        else:
            print("Введен неправильный пароль")
    else:
        print("Пользователь не существует")

#____________________________________________________________________________________________________________________
"""
Сложность O(n^2)
Первый вариант мне нравится больше и по красоте и по сложности 
"""
def autorisation_1(login, password, user_mass):
    log={}
    for i in user_mass:
        for k, v in i.items():
            if k == 'login' and v == login:
                log = i
    if log != {}:
        if log["password"] == password:
            print("Добро пожаловать")
            if log['status'] is not True:
                complite_autorication(log)
        else:
            print("Введен неправильный пароль")
    else:
        print("Пользователь не существует")



print(users)
autorisation("root", "12345678", users)
autorisation_1("root", "12345678", users)
print("*"*100)
autorisation("root1", "12345678", users)
autorisation_1("root1", "12345678", users)
print("*"*100)
autorisation("sa", "1234561", users)
autorisation_1("sa", "1234561", users)
print("*"*100)
autorisation("sa","123456",users)   # ------------- при ответе на авторизацию (да) изменит статус авторизации в изначальных данных
autorisation_1("sa","123456",users)
print(users)
