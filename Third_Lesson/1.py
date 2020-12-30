from timeit import timeit,repeat ,default_timer

def memorize(func):
    cache = {}
    def wrapper(num):
        if cache.get(num):
           return cache[num]
        else:
            cache[num]=func(num)
            return cache[num]
    return wrapper

num = 900

@memorize
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

def fib_t(n):
    if n < 2:
        return n
    return fib_t(n-2) + fib_t(n-1)

#print(timeit("fib(num)",setup= "from __main__ import fib, num",number=1))
#print(timeit("fib_t(num)",setup= "from __main__ import fib_t, num",number=1))
fib(20)
fib(20)