from timeit import timeit

print('I-вариант')
print(timeit('''
def func_1(num):
    arr = []	   
    for i in range(len(num)):	    
        if num[i] % 2 == 0:	       
            arr.append(i)	           
    return arr	 
'''))

print(timeit('''
def func_2(num):
    arr = []
    for el in num:
        if el % 2 == 0:
            arr.append(num.index(el))
    return arr
'''))

# убрали лишний перебор массива

print('II-вариант')
def func_1(num):
    arr = []
    for i in range(len(num)):
        if num[i] % 2 == 0:
            arr.append(i)
    return arr

res_1 = func_1([0, 1, 2, 3, 4])


def func_2(num):
    arr = []
    for el in num:
        if el % 2 == 0:
            arr.append(num.index(el))
    return arr

res_2 = func_2([0, 1, 2, 3, 4])


print(
    timeit(
        "func_1([0, 1, 2, 3, 4])",
        setup='from __main__ import func_1',
        number=10000))

print(
    timeit(
        "func_2([0, 1, 2, 3, 4])",
        setup='from __main__ import func_2',
        number=10000))

print('III-вариант')
def func_3(num):
    return [i for i, el in enumerate(num) if el % 2 == 0]

num = [el for el in range(5)]

print(
    timeit(
        "func_3(num)",
        setup="from __main__ import func_3, num",
        number=10000))

''' выполняется быстрее генератор, чем перебор в цикле for, " \
но 2 вариант тоже достаточно быстро выполняется'''