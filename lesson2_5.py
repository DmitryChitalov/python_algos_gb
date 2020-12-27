def ascii_code(el):
    if el > 127:
        return ' '
    else:
        t = ' '
        if el % 10 == 2:
            t = '\n'

        c = chr(el)
        return f'{t}{el} - {c} {ascii_code(el + 1)}'


print(ascii_code(32))