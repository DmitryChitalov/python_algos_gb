"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""

########################################################################################################################

string = input('Введите строку: ')
some_list = []
some_dict = {}
for i in range(len(string)):
    for j in range(len(string)-1 if i == 0 else len(string), i, -1):
        some_list.append(hash(string[i:j]))
        some_dict[string[i:j]] = hash(string[i:j])

print(list(some_dict.keys()))
print(f'Количество подстрок в строке: {len(set(some_list))}')



