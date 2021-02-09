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

#########################################################
users = []


#########################################################

def check_the_person(login, password):
    print("You are not authorized!")
    ccn = input("Enter your credit card number, valid through info and 3 digits on the back of a card: ")
    if ccn == "":
        return 0
    else:
        return 1


#########################################################
def main_func(login, passwd):
    counter = -1
    my_user = ""
    for user in users:
        counter += 1
        if user[0] == login:
            my_user = user
            break
    if my_user == "":
        ret = input(f"Undefined user {login}. Wished to join us? (Y/N) : ")
        if ret == 'Y':
            pwd = input("Enter password: ")
            users.append([login, pwd, 0])
            print(f"Welcome, {login}")
        else:
            print("have a nice day")
        return

    if passwd != users[counter][1]:
        print(f"Не такой уж ты и {users[counter][0]}")
        return
    else:
        print(f"Hello, {users[counter][0]}")

    if my_user[2] != 1:
        if check_the_person(my_user[0], my_user[1]) != 1:
            print(f"Плохой ты, {my_user[0]}")
            return
        else:
            users[counter][2] = 1

    print(f"{my_user[0]}, I love you!!!")


#########################################################

while True:
    print("---------------------------")
    login = input("Login: ")
    if login == "":
        break
    passwd = input("Password: ")

    main_func(login, passwd)
    print(f"Total users: {users}")
