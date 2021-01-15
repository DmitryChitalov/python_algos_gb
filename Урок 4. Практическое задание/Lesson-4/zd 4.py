from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]

def funcia():
    elem = max(array, key=array.count)
    return f"Чаще всего встречается число {elem}, оно появилось в массиве {array.count(elem)} раз(а)"

print(funcia())

print(timeit("funcia()", setup="from __main__ import funcia"))