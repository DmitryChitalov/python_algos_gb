"""
Задание 5.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
"""


def palindrome_check(line):
    mod_line = line.replace(' ', '').lower()
    if mod_line == mod_line == mod_line[::-1]:
        return 'это палиндром.'
    else:
        return 'это не палиндром.'


line_1 = 'А роза упала на лапу Азора'
line_2 = 'У Лукоморья дуб зелёный'

print(line_1, '-', palindrome_check(line_1))
print(line_2, '-', palindrome_check(line_2))

'''
В уроке честно говоря не помню как оно было, решил с нуля.
'''
