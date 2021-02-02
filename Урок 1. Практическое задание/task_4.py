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
f = open('pwd.txt', 'a+')
f.write('user1 user1 1\n')
f.write('user2 user2 1\n')
f.write('user3 user3 0\n')
f.write('user4 user4 0\n')
f.close()
"""
# Сложность O(N)

login = input("введите логин:")
password = input("введите пароль:")


def check_authentification(log, pwd):
    f = open('pwd.txt', 'r')
    for line in f:
        line = line.rstrip('\n')
        user_list = line.split(" ")
        if (user_list[0] + " " + user_list[1]) == (login + " " + password):
            if user_list[2] == "1":
                print("You've passed!")
                f.close()
                return 1
            else:
                print("You're not activated! Print 1 if you wanna be activated right now")

                while True:
                    is_activated = input(":")
                    if is_activated == "1":
                        print("You've been activated successfully!")
                        f.close()
                        return 1
                    else:
                        print("You're wrong! Try again")

    print("You've not passed!")
    f.close()
    return 0


check_authentification(login, password)
