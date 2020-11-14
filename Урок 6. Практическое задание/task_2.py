"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
# использование форматирования строк вместо конкатенации(внутри цикла)
#  избегать использование глобальных переменных
#  использовать встроенные функции-они уже оптимизированны


##пример генератора

from memory_profiler import profile, memory_usage


@profile
def work_with_items(items):
    result = []
    for item in items:
        result.append('Changed {}'.format(item))
    return result


@profile
def yield_items(items):
    for item in items:
        yield 'Changed {}'.format(item)


m1 = memory_usage()
for i in work_with_items(range(10)):
    print(i)
m2 = memory_usage()
mem_diff = m2[0] - m1[0]
print(f"Выполнение заняло {mem_diff} Mib")

m1 = memory_usage()
for i in yield_items(range(10)):
    print(i)
m2 = memory_usage()
mem_diff = m2[0] - m1[0]
print(f"Выполнение заняло {mem_diff} Mib")


"""
генератор yield_items возвращает элементы по одному, 
а функция work_with_items - собирает их в список, а потом возвращает. 
Если количество элементов небольшое, это не существенно. 
Но, при обработке больших объемов данных, лучше работать с элементами по одному.
Например, при обработке большого log-файла, лучше обрабатывать его построчно, не выгружая все содержимое в память.
"""
