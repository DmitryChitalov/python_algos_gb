'''
Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
'''

from memory_profiler import profile, memory_usage

def memory_check(func):
    def wrap(*args, **kwargs):
        mem_usage_dict = []
        for el in range(10):
            memory_start = memory_usage()
            print(f'Memory start: {memory_start}')

            func()

            memory_stop = memory_usage()
            print(f'Memory stop: {memory_stop}')

            mem_usage_dict.append(memory_stop[0] - memory_start[0])

        print(f'{sum(mem_usage_dict)/10} Mib')
    return wrap()

@memory_check
def sum_value_func():
    sum_value = 0
    for el in range(10):
        sum_value += el**el
        print(f'value is: {el}')
        print(f'Sum value is: {sum_value}')
    return sum_value

print('Program "Memory usage with your own decorator"')
sum_value_func