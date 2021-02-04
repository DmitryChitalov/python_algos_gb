"""
Задание 7.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
"""
# палиндром

from task_7_1 import DequeClass


def pal_checker(string):
    dc_obj = DequeClass()

    for el in string.replace(" ", ""):
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal


# Функция проверки на полиндромность:
def my_pal_checker(i_string):
    check_string = i_string.replace(" ", "")

    return check_string == check_string[::-1]


check_str = "молоко делили ледоколом"

print(pal_checker(check_str))

print(my_pal_checker(check_str))



