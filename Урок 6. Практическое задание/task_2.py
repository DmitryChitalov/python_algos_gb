"""
Задание 2.
Предложить еще какие-гибудь варианты (механизмы, библиотеки) оптимизации и
доказать (наглядно, кодом) их эффективность
"""
from memory_profiler import profile
from random import randint
from collections import Counter


@profile
def func_1(target_, data_counter):
    for x in data_counter:
        y = target_ - x
        if y in data_counter and (x != y or data_counter[y] > 1):
            print(x, y)
            return "1"

    return "0"


@profile
def func_2(target_, tuple_):
    arr_ = sorted(tuple_)
    for i in range(len(arr_)):
        if arr_[i] < target_:
            for j in range(1, len(arr_)):
                if arr_[j] < target_:
                    s = arr_[i] + arr_[j]
                    if s == target_:
                        print(arr_[i], arr_[j])
                        return "1"
                    elif s > target_:
                        break
                else:
                    return "0"
        else:
            return "0"
    return "0"


if __name__ == "__main__":
    N = 300
    target = int(randint(0, N))
    a = [0] * N
    for i in range(N):
        a[i] = int(randint(0, N))  # заполняем элемент массива случайным числом от 0 до 100
        print(a[i], end=' ')
    data_counter = Counter(int(i) for i in a)
    tuple_ = tuple(a)
    print("*" * 50, target)
    func_1(target, data_counter)
    print("*" * 50, target)
    func_2(target, tuple_)

"""
Использовал коллекцию для оптимизации памяти, но результата не увидел
"""
