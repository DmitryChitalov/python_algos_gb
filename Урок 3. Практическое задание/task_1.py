"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
import timeit

time_start = timeit.default_timer()
dic1 = {}
for a in range(100000):
    k = str(a + 1) + ' qwerty'
    dic1[a] = k
    # print(d)
time_end = timeit.default_timer()
print("Dictionary ", time_end - time_start)

time_start = timeit.default_timer()
list1 = []
for a in range(100000):
    k = str(a + 1) + ' qwerty'
    list1.append(k)
    # print(d)
time_end = timeit.default_timer()
print("List ", time_end - time_start)

time_start = timeit.default_timer()
dic2 = dic1.copy()
time_end = timeit.default_timer()
print("Dic copy ", time_end - time_start)

time_start = timeit.default_timer()
list2 = list1.copy()
time_end = timeit.default_timer()
print("List copy ", time_end - time_start)
# ------------------------------------------------


time_start = timeit.default_timer()
if "256 qwerty" in list1:
    print("True")
else:
    print("False")
time_end = timeit.default_timer()
print("List поиск ", time_end - time_start)



time_start = timeit.default_timer()
if dic1[256]:
    print("True")
else:
    print("False")
time_end = timeit.default_timer()
print("Dic поиск ", time_end - time_start)

# print(dic1[5])

# операции со списком работают быстрее например запись у словаря медленнее, потому что надо посчитать хэш и в память
# по индексам положить, а в list() чтоб добавить элемент в конец достаточно просто записать в заранее выделенную память.
# а например поиск по словарю зная ключ значительно быстрее чем в списке
