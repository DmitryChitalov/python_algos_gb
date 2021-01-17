users = {'Vasya': {'password': '45umaU', 'active': True},
             'Petya': {'password': 'vpm5of', 'active': False},
             'Masha': {'password': '78omaU', 'active': True},
             'Dasha': {'password': 'vg4maU', 'active': True}
             }

""" Решение1, линейная сложность"""

def authentication_1(name, password):
    for key, value in users.items():
        if key == name:
            if value['password'] == password and value['active']:
                return f'{name}, доступ разрешен!'
            elif value['password'] == password and not value['active']:
                return f'{name}, учетная запись не активирована! Хотите пройти активацию?'
            elif value['password'] != password:
                return 'Доступ запрещен!'
    return f"Учетная запись {name} не существует!"


""" Решение2, сложность константа"""


def authentication_2(name, password):
    if users.get(name):
        if password == users[name]['password']:
            if users[name]['active']:
                return f'{name}, доступ разрешен!'
            else:
                return f'{name}, учетная запись не активирована! Хотите пройти активацию?'
        else:
            return 'Доступ запрещен!'
    else:
        return f"Учетная запись {name} не существует!"


print(authentication_1('Masha', '78omaU'))
print(authentication_1('Petya', 'vpm5of'))
print(authentication_1('Max', 'vg4maU'))
print(authentication_2('Dasha', 'vpm5of'))
print(authentication_2('Vasya', 'v77777'))
print(authentication_2('Max', 'vg4maU'))
"""
Второе решение более предпочтительно, сложность меньше
"""
