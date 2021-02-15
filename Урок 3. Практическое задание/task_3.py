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

user_string = input("Введите строку из маленьких латинских букв: ")
len_of_user_string = len(user_string)
array = set()

for el in range(len_of_user_string):
    last_el = user_string[el:]
    #print(last_el)
    #print(range(1, len(last_el) + 1))

    for length in range(1, len(last_el) + 1):
        #print(range(1, len(last_el) + 1))
        sub_str = user_string[el:el + length]
        #print(sub_str)

        if user_string != sub_str:
            hash_sub_str = hash(sub_str)
            array.add(hash_sub_str)
            #print(hash_sub_str)

#print(len(array))

print(f"Количество различных подстрок в строке {user_string} равно {len(array)}")
