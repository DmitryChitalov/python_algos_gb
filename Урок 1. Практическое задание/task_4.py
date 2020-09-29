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
data = {'log':'Ann', 'pas':'AAA', 'sign':'0'}
def chekin(l, p):                                      #O(len(n)
    dict_1 = {'log': l, 'pas': p}
    if dict_1['log'] == data['log'] and dict_1['pas'] == data['pas']:
        if data['sign'] == '1':
            print('You are welcome')
            return
        print('You should activate your profile')
        return
    print('Incorrect login or password')
chekin('Ann', 'AAA')

def chekin_1(l, p):                                 #O(1)  Это решение эффективнее, сложность меньше.
    if l in data.values():
        if data['pas'] == p:
            if data['sign'] == '1':
                print('You are welcome')
                return
            print('You should activate your profile')
            return
        print('Incorrect password')
        return
    print('Incorrect login')
    return
chekin_1('Ann', 'AAA')


