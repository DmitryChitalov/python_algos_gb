"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""

# Можно конкатенировать строки при помощи оператора "+". Однако, строки в Python являются неизменяемым объектом,
# и операция сложения ("+") влечет за собой создание нового объекта и копирование в него старого содержимого.
# Более эффективный подход связан с использованием массива, чтобы модифицировать отдельные символы и потом заново
# создать строку при помощи функции join().

new = "This" + " " + "is" + " " + "going" + " " + "to" + " " + "require"

new_join = " ".join(["This", "is", "going", "to", "require"])
print(new)
print(new_join)

# Использование множественных присваиваний

first_name, last_name, city = "Kevin", "Cunningham", "Brighton"

x, y = y, x

# вместо

temp = x
x = y
y = temp

# избегать глобальных переменных насколько это возможно.

# завершать работу функции, как только поймете, что она уже выполнила намеченную задачу.
# Это позволит избегать вложенных инструкций if.

if not positive_case:
    raise exception
if not particular_example:
    raise exception
do_something

# вместо

if positive_case:
    if particular_example:
        do_something
else:
    raise exception

# “ленивая” оценка, если есть цепочка условий «and», то проверка остановится на первом ложном условии
