def eratosfen():
    n = 2
    border = 10000
    sieve = [el for el in range(border)]
    sieve[1] = 0
    while n < border:
        if sieve[n] != 0:
            j = n + n
            while j < border:
                sieve[j] = 0
                j = j + n
        n += 1
    sieve_s = list(set(sieve))
    sieve_s.remove(0)
    i = 0
    for el in sieve_s:
        i += 1
    return i


print(eratosfen())
