import collections
import time


def time_delta(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('Время выполнения: {} секунд.'.format(end - start))
        return return_value

    return wrapper


my_deque = collections.deque([i for i in range(10000)])
my_list = [i for i in range(10000)]


@time_delta
def append_x(list, x):
    list.append(x)
    return list


@time_delta
def copy_list(list):
    x = list.copy()
    return x

@time_delta
def copy_deque(deque):
    y = deque.copy()
    return y


@time_delta
def index_list(list, x):
    return list.index(x)


@time_delta
def len_list(list):
    return len(list)


@time_delta
def reverse(list):
    return list.reverse


append_x(my_list, 1001)
append_x(my_deque, 1001)
copy_list(my_list)
copy_deque(my_deque)
index_list(my_list, 900)
index_list(my_deque, 900)
len_list(my_list)
len_list(my_deque)
reverse(my_list)
reverse(my_deque)