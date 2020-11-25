from memory_profiler import profile, memory_usage

def memory_check(func):
    def wrap(*args, **kwargs):
        mem_usage_dict = []
        for el in range(10):
            memory_start = memory_usage()
            print(f'Memory start: {memory_start}')

            func(args[0])

            memory_stop = memory_usage()
            print(f'Memory stop: {memory_stop}')

            mem_usage_dict.append(memory_stop[0] - memory_start[0])

        print(f'{sum(mem_usage_dict)/10} Mib')
    return wrap()

@memory_check
def sum_value_func(stop_number):
    value = 0
    for el in range(stop_number):
        value += el
        print(f'value is: {value}')
    return value

sum_value_func(10)
