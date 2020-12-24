""
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

S = str(input("Введите строку S: "))

print("Строка \'%s\' имеет длину из %d символа(ов)." % (S, len(S)))


subs_dict = {}
for i in range(len(S)):
    for j in range(len(S) - 1 if i == 0 else len(S), i, -1):

         print(S[i:j], i, j)
         subs_dict[S[i:j]] = hash(S[i:j])

print(len(list(subs_dict.keys())), list(subs_dict.keys()))


S = str(input("Введите строку S: "))

print("Строка \'%s\' имеет длину из %d символа(ов)." % (S, len(S)))

#######################################################################################################

subs_set = set()
subs_dict = {}
for i in range(len(S)):
    for j in range(len(S) - 1 if i == 0 else len(S), i, -1):
        subs_set.add(hash(S[i:j]))

print("Количество различных подстрок в этой строке:", len(subs_set))
