def rev(num, rev_num=''):
    if num == 0:
        return int(rev_num)
    else:
        rev_num += str(num % 10)
        return rev(num // 10, rev_num)


print(rev(123498541))
