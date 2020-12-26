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
# не понимаю как решить задачу, используя хеш-функцию. Сделал свою реализацию
def count_str(string, n):
    set_sub = set()
    for i in range(n):
        length = n
        while length > 0:
            cur_sub = string[i:length]
            set_sub.add(cur_sub)
            length -= 1
    set_sub.remove('')
    return len(set_sub)

print(count_str('qwerty', 6))