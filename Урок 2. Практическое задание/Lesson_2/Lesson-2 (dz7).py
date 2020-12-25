def sum_num(n):
    if n == 1:
        return 1
    return n + sum_num(n-1)


def form(n):
    return n * (n + 1) / 2


num = 5
print(sum_num(num) == form(num))