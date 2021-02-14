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

#Уникальные подстроки строки
def all_str(my_str):
    str_dict = {}
    for i in range(len(my_str) - 1):
        # i+1 - длина подстроки
        for j in range(len(my_str) - i):
            # j - позиция подстроки длинны i+1
            sub_str = my_str[j:j + i + 1]
            str_dict[hash(sub_str)] = sub_str
    return str_dict


text1 = input("Введите текст: ")
my1 = all_str(text1)

print(f"{text1} - {len(my1)} уникальных подстрок")
for idx in my1:
    print(my1[idx])
