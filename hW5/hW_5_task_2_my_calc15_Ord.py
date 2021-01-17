from collections import OrderedDict

simb_str = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'
DICT16 = OrderedDict()
sum_list = []
dec = 0
for i in range(len(simb_str)):
    DICT16[i] = simb_str[i]
DICT16.update({v:k for k,v in DICT16.items()})
print(DICT16)
a = input('Введите число в шестнадцатиричном формате: _')
a_list = list(a.upper())
b = input('Введите число в шестнадцатиричном формате: _')
b_list = list(b.upper())
if len(b_list) > len(a_list):
    a_list, b_list = b_list, a_list
while len(a_list) > 0:
    if len(b_list) >= 1:
        n = DICT16[a_list.pop()] + DICT16[b_list.pop()] + dec
        if n > 15:
            n = DICT16[n-16]
            dec = 1
        else:
            n = DICT16[n]
            dec = 0
        sum_list.append(n)
    else:
        n = DICT16[a_list.pop()]  + dec
        if n > 15:
            n = DICT16[n - 16]
            dec = 1
        else:
            n = DICT16[n]
        sum_list.append(n)
if dec > 0:
    sum_list.append(dec)
result = ''.join(str(n) for n in sum_list[::-1])
print(result)

