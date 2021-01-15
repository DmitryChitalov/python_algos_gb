import memory_profiler
import time


def find_low():
    lst = [x for x in range(10000)]
    low = lst.pop()
    for x in lst:
        for y in lst:
            if y == x:
                continue
            elif y < x and y < low:
                low = y
                break
            elif x < low:
                low = x
    return low

def find_low_2():
    lst = [x for x in range(10000)]
    lst.sort()
    return lst[0]



if __name__ == '__main__':

    t1 = time.process_time()
    m1 = memory_profiler.memory_usage()

    low = find_low()

    t2 = time.process_time()
    m2 = memory_profiler.memory_usage()

    time_diff = t2 - t1
    mem_diff = m2[0] - m1[0]

    print(f"Выполнение заняло {time_diff} сек and {mem_diff} Mib")

    t3 = time.process_time()
    m3 = memory_profiler.memory_usage()

    low2 = find_low_2()

    t4 = time.process_time()
    m4 = memory_profiler.memory_usage()

    time_diff2 = t4 - t3
    mem_diff2 = m4[0] - m3[0]

    print(f"Выполнение заняло {time_diff2} сек and {mem_diff2} Mib")

    '''Выполнение первой функции заняло 4.28125 сек and 0.140625 Mib
        Выполнение второй функции заняло 0.0 сек and 0.0 Mib
       Причина этому применение в первой функции двух циклов, один, вложенный во второй.
       Вторая же функция исползует только метод списка - sort'''


    def simple(i):

        count = 1
        n = 2
        while count <= i:
            t = 1
            is_simple = True
            while t <= n:
                if n % t == 0 and t != 1 and t != n:
                    is_simple = False
                    break
                t += 1
            if is_simple:
                if count == i:
                    break
                count += 1
            n += 1
        return n

    def simple_2(i):
        if i == 1:
            return 2
        elif i == 2:
            return 3
        elif i == 3:
            return 5
        elif i == 4:
            return 7
        num = 8
        count = 5
        while True:
            if num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
                simple = num
                count += 1
            num += 1
            if count > i:
                break
        return simple


    t5 = time.process_time()
    m5 = memory_profiler.memory_usage()

    n = simple(20000)

    t6 = time.process_time()
    m6 = memory_profiler.memory_usage()

    time_diff3 = t6 - t5
    mem_diff3 = m6[0] - m5[0]

    print(f"Выполнение заняло {time_diff3} сек and {mem_diff3} Mib")

    t7 = time.process_time()
    m7 = memory_profiler.memory_usage()

    n = simple_2(20000)

    t8 = time.process_time()
    m8 = memory_profiler.memory_usage()

    time_diff4 = t8 - t7
    mem_diff4 = m8[0] - m7[0]

    print(f"Выполнение заняло {time_diff4} сек and {mem_diff4} Mib")

    ''' Выполнение третьей функции заняло 131.671875 сек and -0.0390625 Mib, поскольку она 
    использует один цикл, вложенный во второй. Выполнение четвертой заняло 0.0 сек and 0.0 Mib, 
    поскольку она использует только простые инструкции и только один цикл'''