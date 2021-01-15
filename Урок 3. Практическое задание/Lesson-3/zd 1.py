
##############################################
import time
def time_test_func(func):
    def inner_func(*args, **kwargs):
        start_time = time.time()
        func(args[0])
        end_time = time.time()
        print(f' время работы функции : {end_time - start_time}')
    return inner_func

@time_test_func
def test_func_list(el):
    test_list = []
    for i in range(el):
        test_list.append(i)
    return test_list

@time_test_func
def test_func_dict(el):
    test_dict = {}
    for i in range(el):
        test_dict[i] = i
    return test_dict

print(f'Program "Test time of filling a list or dictionary"')
fill_max_el = 1000000
print(f' 1. Заполнение случайного списка {fill_max_el} элемента')
test_func_list(1000000)
print(f' 2. Заполнение случайного словаря {fill_max_el} элемента')
test_func_dict(1000000)


#############################################