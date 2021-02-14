"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
"""
Наиболее эффективно использовать кэш, и структуры, выделяющие память только при непосредственном обращении к нужному элементу.
Задачи из курса в плане использования памяти не очень показательны, так как даже искусственное увеличение
размерностей структур все равно не приводит к исчерпанию ресурсов, но выводы по замерам сделать можно -
даже на таких объемах данных хорошо видно преимущество структур с выделением памяти по необходимости, кэширования
и т.д., над обычными массивами, списками и т.п.

Python 3.9
ОС Windows 10 x64 
Before LL reverse: [26.046875]
Filename: C:\Users\hukut\Documents\GitHub\python_algos_gb\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   104     26.2 MiB     26.2 MiB           1       @profile
   105                                             def reverse(self):
   106     26.2 MiB      0.0 MiB           1           cur = self.head
   107     26.2 MiB      0.0 MiB           1           prev = None
   108     26.2 MiB      0.0 MiB       10001           while cur:
   109     26.2 MiB      0.0 MiB       10000               tmp = cur.get_next()
   110     26.2 MiB      0.0 MiB       10000               cur.set_next(prev)
   111     26.2 MiB      0.0 MiB       10000               prev = cur
   112     26.2 MiB      0.0 MiB       10000               cur = tmp
   113     26.2 MiB      0.0 MiB           1           self.head = prev


After func: [26.23828125]
Before func 1: [26.23828125]
Filename: C:\Users\hukut\Documents\GitHub\python_algos_gb\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    27     26.2 MiB     26.2 MiB           1   @profile
    28                                         def func_1():
    29     26.2 MiB      0.0 MiB           1       m = 0
    30     26.2 MiB      0.0 MiB           1       num = 0
    31     26.3 MiB  -2664.9 MiB      100001       for i in array:
    32     26.3 MiB  -2664.9 MiB      100000           count = array.count(i)
    33     26.3 MiB  -2664.9 MiB      100000           if count > m:
    34     26.2 MiB      0.0 MiB           6               m = count
    35     26.2 MiB      0.0 MiB           6               num = i
    36     26.2 MiB     -0.1 MiB           2       return f'Чаще всего встречается число {num}, ' \
    37     26.2 MiB      0.0 MiB           1              f'оно появилось в массиве {m} раз(а)'


Чаще всего встречается число 2725, оно появилось в массиве 23 раз(а)
After func: [26.21484375]
Before func 2: [26.21484375]
Filename: C:\Users\hukut\Documents\GitHub\python_algos_gb\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    39     26.2 MiB     26.2 MiB           1   @profile
    40                                         def func_2():
    41     26.2 MiB      0.0 MiB           1       new_array = []
    42     27.1 MiB  -5855.0 MiB      100001       for el in array:
    43     27.1 MiB  -5855.0 MiB      100000           count2 = array.count(el)
    44     27.1 MiB  -5854.1 MiB      100000           new_array.append(count2)
    45                                         
    46     27.1 MiB      0.0 MiB           1       max_2 = max(new_array)
    47     27.1 MiB      0.0 MiB           1       elem = array[new_array.index(max_2)]
    48     27.1 MiB      0.0 MiB           2       return f'Чаще всего встречается число {elem}, ' \
    49     27.1 MiB      0.0 MiB           1              f'оно появилось в массиве {max_2} раз(а)'


Чаще всего встречается число 2725, оно появилось в массиве 23 раз(а)
After func: [25.58203125]
Before func 3 [25.58203125]
Filename: C:\Users\hukut\Documents\GitHub\python_algos_gb\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    51     25.6 MiB     25.6 MiB           1   @profile
    52                                         def func_3():
    53     26.3 MiB      0.7 MiB           1       nums = set(array)
    54     26.3 MiB      0.0 MiB           1       num = 0
    55     26.3 MiB      0.0 MiB           1       total = 0
    56     26.3 MiB      0.0 MiB       10000       for k in nums:
    57     26.3 MiB      0.0 MiB        9999           count = array.count(k)
    58     26.3 MiB      0.0 MiB        9999           if count > total:
    59     26.3 MiB      0.0 MiB           7               total = count
    60     26.3 MiB      0.0 MiB           7               num = k
    61     26.3 MiB      0.0 MiB           2       return f'Чаще всего встречается число {num}, ' \
    62     26.3 MiB      0.0 MiB           1              f'оно появилось в массиве {total} раз(а)'


Чаще всего встречается число 2725, оно появилось в массиве 23 раз(а)
After func: [25.64453125]
Before func 4: [25.64453125]
Filename: C:\Users\hukut\Documents\GitHub\python_algos_gb\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    64     25.6 MiB     25.6 MiB           1   @profile
    65                                         def func_4():
    66     25.6 MiB      0.0 MiB           1       num = max(array, key=array.count)
    67     25.6 MiB      0.0 MiB           1       total = array.count(num)
    68     25.6 MiB      0.0 MiB           2       return f'Чаще всего встречается число {num}, ' \
    69     25.6 MiB      0.0 MiB           1              f'оно появилось в массиве {total} раз(а)'


Чаще всего встречается число 2725, оно появилось в массиве 23 раз(а)
After func: [25.64453125]
Before revers_3: [25.64453125]
Filename: C:\Users\hukut\Documents\GitHub\python_algos_gb\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    71     25.6 MiB     25.6 MiB           1   @profile
    72                                         def revers_3(enter_str):
    73     25.7 MiB      0.0 MiB           1       revers_str = enter_str[::-1]
    74     25.7 MiB      0.0 MiB           1       return revers_str


HBQQLuESRcdgYoNoCueVFZJKPCvncpTnZUIqOaTlrxDIKJUoxzQMUoDEurOaTJFKeIYKWrIEAmFUgYxLyJicyXIJqXbFzkPjZVYIDmazhFoRcNEULoIwJqtjuwizHBvzbYpdUFgyOwtFgzGykYBqJkSjCPsVmmpcsJADtpExSooMrkdpFZUJDXZKgFjpwPggXfwmcGDRlMBgfKpwBNBXGXZYxIyndqwaXGmfRPLPHXBYQglpsFAaEkFFOUeBPGsKXKsgSARkYSlEmYSjVjIuyIHAfgmCwaUkLNfefuFMLiuLYiYOPkCBRywWEjtfiCeoNLmLhSxdTBrvkgiLkmihGWUEjDuqeHkHwDsnfdNzpsViAJsljcdLVlsFwXVhpnWuMlLarfguXxULhhcaeXkUyKHKIgDCMiplrwLCBUuxrRntrzINYTdherJoLeOwPIsFmUBgyyhWKhbHzCXylzBoIVTIEiuKmvmcIEznvqfmUSnYQygMTCQZvQxaoSxRsaIvaRzgvrjfPrqweArwapKXDxsYmWmDavKZivxiAokNLUmZzPfbKpJAHyxMNbcxJQxGAPCTIouALJnndbeLhUJFSVnhfjbXkZviWMObsMtHJmoJHMZBAbvfudvbdFZccTTmLdbjHWJlkxGvjVVFIXjKiRKvaPEriUnWJjVMGIDKYgcCPcJexsGNqCqnegpvrxjqzUcmQSDOYRVUGnTjxKUyxRbhionPLkhLYokbwvCaXEIWvwHVmropfaoNiMGYpjRyhwxfIxZaJWDTXlBGJCnulxcYOEnxPSoUtNpNNtgoeLYLMpICDibVNpQFmzAxeQCUoEAlXpYnZPThKuRMKCVquGaBTzuZfrfZwgIMeMWbeQewDTweeRNpIhVUHIImSrjDjddUYfQJdKZETynAAmpLuncsDNvMcprKnbvaRjrkuaHQLpfoRHitTqRzXgyWqYVjGpFmdEDvlbLipDBvpOTSFTkIYZKuFvuvfepkooaDNcbzAoqPqcBQsSdAXPISMsXkCpbENpgRVolWeEHvbogCjhSQbSfgzqgfoeDVldHUSPwzAfTSEWGtPGldEwVSpKvYYxSoGEbHhGfSwWiWYflrEgFKdmTGLISmLufhXjegdVNHXNFJeXysvwzyZsGsScbAAKpdpILFIIOeAYuvpikysDsXZeXpamuDkMhMfdpGGniWmbqBolNUJKvXPqwJdQbRXfYuBudedbHWqzTkmsopQzrnmoystQhkeSqjQyqijRBNkOSPlIRGlwxcThQbVRrakdunyDNJclnMyIIiiqAMsMifbmfxZCDKROLooJBFmhDShmcZeVjZOJAllfTvktOiCPLqShLSRGYVFgYPTpFgBCPBQVBAFLrfXvuXQcZAfZsWtAAcUJJGYrhaNfkPWySDmQwJrmWYlVTwskWhsHDMOATiJUUpLGdGKEFAeMxlqiBJzbeXnKCwUPPnYaahdjwvxtiVQCGFJXNnpqMerxUMYpnUlZsdaWpkPvgmAexradYfTFJvsNWGEoFcQEJYNSKdhZSjsVKsBqnXFNXhYqCOtdPGrZttcOpJMKQAVYKtADbAYoubfpqqieKjsvPZyDSEsMhMqUAkPWHllysXJpMaQKaRTbOztDFaGMmvLsFirtQgvjJGRCmNFtRsjiASAdsHAIdFUObvoaIKTazBVRDjOzkZMndeYYpLThvpJsAWQUoVTrAOUBOoyaNyyEGsjCbPNTYYclxVAIxwKNNlHMqiBWxiykZqwfyAaLIEPhgKjFAqotQsuEJsxTHFRRMHudxUPSzKUjiPQUBfmISGYChEJXdRUVzmEZeMyUqTECDtotynpLxoyPUuZetpsKEBIOruwcEuHFEnXkRHoJorXWjWfVIhKExvaoFlBwNKhlRJyijDKDkmbGixoBvEbdfGwXKUCksgREOdnwfixbpvKNuhvPULDbisIUXycOLjsLLghGWknWvYQdrlHSKHsLGCvgORTMzMmRqHeqgwKRIlpZcZgyKFzHMxKtBVVzJBmGKgocoyZLrluIFejEJTojDTkwGZaZgFtqcUlwULfyUsDQdaPqrzFrZDirNQSMyDgwDgIBoJJKWDDHdrLYJOejtvFKyDcofWwrLdpiREqeuBNFXUDZgaWsZGCKOAuLBcuOKtthQbPPDlIsZdOZrQzhjskZPTpediOSQZBkVoZyXUvXUZPMVjyfQqjnuDsxAXwBramPYJxlDUHOiYRIHGBDhhEHRfzpFKzmzsjrkhbcliEIkIeFTQVAyKnCbonTOAFwORUVnXBhstsVWzZDrnhIOcpLDrDoelZAegeXMpcRVqqQHDcSNOUseDwDbRFAEYgVoWevxBdtZCthmivblplbBGVCtpLhFqDnQwgoCcQJykfekxCJnfYirzUQCxdMKUGfEfCImoTBzAgkqVsuLAsuVnWssZybaEYFDHkChXdjcUYEYTHUGswkHvGgoKidJsNeRoNidZRkhrzNzxWHuemAWTclmRDLoAMMViexZuMoPFSpNkWattcTBDhFVdmzzlLNIEwrvjrvAsiQoujteYdrgBXxANmSXoWpaJdFAagNWGWSCvGtcPYswVFzIMMoJufMKiUpURrvwkxBkfZJmngetUJVHUSnWXgBHWwGYvJGzenPhwKAPZDQvcjjeobnBfwcWpYcMfunSlooorAstkEOTryWzNrVkifVfCTEEwGNPhPJLovnsZqtsviyxiYfQDpSNpwjkYpXronUchEzmsrhpvgjbfzDleMDrnwVPGizpCuzuzqkPZkWqryMsuPnanImUFudnTEQlydksdYWZNDUgFXDYjkkfEokWIpndKvROEWhTYYiSkQZHEwsGwqeGztulqGDANdsdnLYtHkwCypxvKeQNWLpDLCfUChYqFbCRIwPUhwSlPXnoZPyYXdfjwAYzgdaWSqaOBphgtRjwkDbDgtkhpRxfmcPeMufnGBYQWYNLvMqfzEhElOWBAPINIZGhkGDanXdHWTWVkdqIZXchmopXoBlXjmFHDOmpWEShqUVNEhzYoZROBPyCpMlodgsftbznPRpQfwsooAPQUSLGoZzxQeGxETdYlSDGxPtRrrpJhXZujFBOVUhuYBrzqalfjCdVCtLAASdAmYYrEhuKfdynDmjidBZBRUqTbqwDRCRrhhrWGGjdnPuOijJtoqWzZfeBJDSKzneaCDlwPkZZVQjtuqSvKhZfduizvYRIZEraDfbinshmWtXSManOOgsvsYjWHyzLvrHTlhjWaHixFcLjKucyjvdEqIZuqoIozLpIeNisVYDDPLnTDWPJzzMnzQwhySuCvQqChZMcuKwOFtxEKcnYmMzGeWuDkTJQKOXPBHZHIOlriPaFmBvSzrwJICTWPSdfUnyzQHFDjoHKxWRldiLhbxRIfclRsXTWGtYyPjWMNScmbDcWNawrGakmdZEbfbmafIwdccqwfrzGQTUEurkbwYoKhLgKdBiiJoDjAEvBgrtvwDjLuOmlCxDAeVpNgKLncyXWtNgzvbNTfKuEglGBbmKpUrGTjWxEMCpaEvhXoqUcHePvssQOWRfmlTyTjzDcKKfDDcMsrgknhQQOCNYFJbslAVjSQvbJDPuoNRLSAbzAsBJijmgzdARhFXzdkggPOyCAEMYbFvxSFKIKSfdTsmpGonSYyRHXSSQuGNZZUGJbtvvpsxtxThyIfBcdSSNxIGzXCCQvxzjgDViGYrZBPtJrugLoowHpMmfbgfkxvlDMRYVPYIfDEWKubnmiZazgkQbsvZzYXPtSnQEBGzjEqryuqTjaiabwxKpkrlnoVMbIpHxuXROcOeWMbjvoYgkRtEfqupWkXLFxhDrZGTBmXwAzKyWeiQVVqupfgGwfaOSrynjIkXHzpJOiNFNRJWpkrgEnZTuGCdqQIdtfxbKKWIEXfbQIXOjVSZZjGwYaWkfukFlgqCJtkxUVxmJIUcPtzIVxGZfCxeRLTNVmjXbwvcrOJWfGXjtxuMvoOquJhrzgyjcipEhBwFMOWdnFBatFMQOoeoFvzzhCNSlSRljleNxNesZlnosylsCqiaICzDOTgGItlcVTNZpoNficmssUotClZqSraJCHdYcpmoikHDpHhRqxhsBMSILBfLqUIVFBSnOlZUuWTrOqMvEvyoByeUYkrrVkzlQtLOBcGlBVRYxqqVLsZFbtlAxcCltTSIyhjhpXavFUxCcijWUFeCxlPchbqbzxiAdVGYmXIRwegttmchOKNkIAHTwegimtYrXjwcezhEGgSKTxjYgQQwoKAkazAUqOFUfOicggYHjUaVVaxtihIXtpKinZtoEUpOxgBcuagSAoiUnKBhXXxXqCOsJPTzWgeaAgQMIpsBGERjhEWTpRKgsIVSqMqnPXJxVudImtYHmKGZSoViNTVTQIEdSWcvuWVEJShzFJrqVKEGiXYhCATSOmHIrKOjzPhdPbQFffZqscbPlDAvyxcFiwApbceshPZGlqizdxjznHmoyPvqDmHBDfbxKjVrbsIYRAsfAfOljRZJiwLanycSPYrVjSLfPSzoowyHRUgOEtGiafKxmAaMSOvikVNTeBRdOACmMQxHwjJuVCTZGPXXLVzSTCXednUNySbmCEJPzKkRIroYvNKEvMgzsiIgMwBSJTgCIuCPqpklQRlrIQMHdxmIdhObBeuQhxPRRINlDsDFStagDpQLUSHTiYeyOKuGExcyCnrjnWMvanTdaIBURfnYlovVsDuhpOylwEDPakZUTeHKlojXvaxuvgOJScYhhCweykBEeofmwmVumrUsVzldhGvhICwmVTBlcWbqKlXqrOFHTUgJxgCzLqYgooKVMjifZjmxOIZbpoTgBzLtBuVpEgYPixrFATLNxIsxRBtLbfkVDzUwYAVsoPGixWKyHUvOOmZBxWUpqPkqCzUhtCpzixFxfAQQndDDhhSZKlYgBGozcZKgLBOzCDQtnXWGdBJMDfNthHrWobAVhATHpUsjoftsYTtDkDLtUEeIEUocVCZAiXMYPAmqOiVzAduXInAQChUsxfgYWKUZHmPFBRVGVtuLqIulyNxUnHBjwwlXOUePWieHZPZPuWtjSxvRsubgFVTDwouFoNoJoHFiBSkETVOsSNfHVwvDghZSYocUvdIiupgLpHjAMxrGEIDEwWhMKNcGZLcAEdXQokbMbvAlMmCftJoJGTzsUTMiOfMndrUTZPyxpFeBtsWWerYgROjJLtkKBNEPRIGKTQpBuXYqDGSoXADiQdzcGahHDLhMparpOPuojApuMaUNMPsKwAkvShZgjsjKNNXVllrswyXSOJlUflnrwFdIDfNbQzIEMXIeMRQAEGpSVGYyMyqnNTKecWhpOyIcoGGktBPnQsiPBncmXqxtSfRQICDYmPYqiqRsKTaKUVDZwtxtdkJtNKQQPXoZRfRaNpTpYNxArngCLbecOzzUvfWTufBXDplVhFHTOpqaAFXwvgmlCikTCwoeIdZIUwNMzWrbieeZJbuOmhGnPPIcYhdPfJqIyKZVIXmIbDDqYKPRPfzYriUftkpHYshQSaDeQugbJqOleIjgWDhwdpAUdxvSaKnbHmYNSyqGrTomympyiMjVbkmyRLORaxkMNmgsySmmvuPyNUSBcxKvGGwDIQxjjEtuLSKpmAbhnbtEZKzDsreTZhghMQjLqYXselfzgKrqbPnuXdEBRYCepHbfLXRmELkViTrnCEeoelDhoXcOaRBFCHwXpqDKHVESPsjXkxsPWkhgdZbwYavdEUHGPdhEXfTwkoQamKPAslrKOziUWdEsLyNxybLwjFfDUCNckJHWKNFxFhPnpnjagqAhiGQNtNMOfELWumIOcACxcoixmGgOsBuUhZKGXYjlRYujCGGoIJAKuZyuwhshvMhJwCCsYHOxSLSyWfgmBCaGURvtitupufVCZdNWMHOsZnESCBihPeaRWUqZJEVkPYoVzBZNKYFUynMvpEcCsptgXArIMwfKVWEexEvRjLNMwkLEZrkHpeqzJHUdFdPlNPNxCdYNemevnzfquVqpcSMtqJkxHlAVGPPHPThrmngcmSZHudOEQIiSTHvndhAuKqGMmOfWlSLQoZibSRWJGFvpGQeCMqfHehDtNhcXceQvMZTiVJLtKqcmKiTWxRzEgtSYXqvrudnpxQZaXxwjqCaAeJVCKiQSPTGtGukfBGqUUynUzfupRuucYqcnbVazvXGGJsqQTmKOwDuJUyJvCWPoijMsHtyQXNsdtTmglfmkWgnwHzmggHnlumeaoxlvMGNnvwrDTcswkMcGAkodKFppmvWcejPBiHOKiYXrnwBSSmXCRjjxxFuOrQCQYnazqbwULCBiYurruVXoDZLPVARhpQcBocaeLfgCyOoZZSLoKiPWOyNYsLzCQyaaKHxAuTBnYUuUpyRFsedgaVeULIpbwtoHbHQKirAAQTTOxXTjqzLXAPbHaTsUKRDkfevNYirKoPiWbEmWXwNGFEVdnXfbZXqEvVbKNviGRbHgkzvbNHmIOHQZZBwzhAjxcRZfpKHqVuoNSiKeDcOppphrzcnKcbFNqkKIkmxUGCteHDKcsLDqKmwwScHZqzQOIqwRgUuoGuzgFSEFgnIlByfUHMIpUKxtBEBRauGpLNpguBrzYDxihpIrMMasDCgRnTnexNHdadPJfiiKddOashZgteAulqDiKrTOFwvfgwrbesePkYwdKSWjDMdKZViNDGgCnJqgmrpoGvpWtvlMxodzgDgBZxFcicqVVYHuiPVDrxfnyTmmXkgbfucwKscINuItiMYIpywPmLgWlpULFRKjBPZyaqMvaDdTGPCTkAhoyHjSHgNGFLnUUBCBlLRAkTQAssQOTdGZDRohozBHeSIDtIUVDIKtOVIENzBNvNAvaqpPOBVrqPntRQPtDEriCUBXMyNWVEdBKPdNqNSNLpdumVonKmIzsfpGEjnYKZdYaiBiDjEHSKshHIeAnUwXXJEqqbhJmqPiYWcxYeXrfMkKKhAVSnzHurUonriAUmLgFIDVteOqhOdyddMMuaMyajbugwwjYMDQyEssagzTdVFARRtiuKonjxkWAoJVWGRChxktpoNFCCmfuwbQhlZNWZiFsfSiTlKMDUvVzniRxfXTGZwXDbavQFutdpLHXWAvwnFFncwfleQJhtuUChWTqIcichYoYjQassJcqixfAwCEVYNgDcPXcCStYfPUjjoAYdYWCUWycKUauSFxtZQfjOGGjiLYMAJMdLZGlosJuyalrhQTymqjoqCWalviTTfZzQBxIDeASrBNrAYHYTMsOeiayhAgfcZzEDMsQttVfIHRpIhmKgkRMBsYWYTfIMeNcFNkiZkKtBGJrNwvzxwVVyMJsqJToZsmtMinysPuwTObWdZsBvACAgYnwelFWJhDxHVnzCBgRTHirrthiwKCQwTsLBjmsWKDEVMJFAszZPZwIfAeVwasxIowKkOBXkBTsKmUzQNfxWMlLeTYSKsPVYLDJPINYmUyBIXpauHDllJSytOGbFfwEvHgglsRdJOLnHVIxjzrKLXyTTtyydkJXycbYdHLGeTTAGqYYCZhYFZzwtZZgBFgGmSTGhXDIrVdGZVDGqqjDhOUXZHtihtKQwWHHQDSSyoAlKgbscNcJBnbKNoSSHfefVOBhYSYmDtLFeRYyxLiJvydzHtDTBlfNAPoKXqslZBduQjSspFxfdRSVsfmuwaTySdKCeYxaJGfmIfvLomfjhQFrdzZdPLbKgyLoXRejYLEmflkClZhyGQLTkgkMkBUyQiCuwwAJWVrNpdXsTYzwxqCxUKgOBMpMoeHCRhkkVNhUAujrSPKQoYBmsHetTxKhWOvHHiXxLGSCNZJsniHFEYDQumeqcNMxjjLHLdObJMNGfvWdAdXLGIUTUXjSbpCRUVlRhUeIHSpTvcwmuRpduElaksrLQjCGvSmCBLAwvQtxSAvUYZasGfZfJCBKCwgjiTsazwHAMHzMPtWEdOQNqrNLthaesbLIhFxGYTiZewIAkvONbrjqDCOeOByWjDIZbNLQmolSGoZCzByhweqmzDZDCRZOcxecyTfbHuBzmBZuzlJOVlrTPLEamPmAplMbSnhgkdQPvhhrCDWbnPibLfeIzRklbtCFohVaTGGwrfLlByHNwrXRwrpsHVxDnjVQTDNHkQumgcMRcsIbUZloxBaZosiwADiqPZKnXpWwEhPzvoypyrGmVtVpfSpNnJSVOpumgxguXdopheIAYsFRaFBnbCkfoCWYbepmDghftpnTcRMiwryCCTYakQUovFWtrRajjnrBatpezsBcBmYIsBFfYGvjFgGIfPiElNMIDGvVCdJdNIWEKndXpRtDpCqHZurRAkIMGnyQNKsCXoAaJeUBhqedRZUZnNwDnbyfKdmrvJhgzgcVLliFEablypyxhEKhfpnDKLkbNLwubzYkjGWtzRAIoLmWUfKTLMxCrAFwVzrDrzWZrClJRoYKKZRSgyplhsXLiNAgapLbTMpDpRNyNmAxfUmFRNnrEwucTzNOfXjkkPUlPhBWxWeBtBjIVZaFJcWrnYYFEcaXcoYZVDCLqpxyUgTWyYHSGsacnJEIoBlvcGaWIkcokzytoUseYSlasLFenMCjlyTbesIwwtjdxAttHXslXjpvujKrFKpWotRSxBnUxbjamZkcGAwywTVpzLZDalSnTXRBOhnQpEtuCpHlKMigHVBwrUVwYLIMAGwnVTTATBqJVYfHpCRCBsbuGUdwPyGxyyvgwPGaNAWTHAjoqXyWiFyfPLnJPlWndyvjPHJgPEtlAsUNsmMbthwKInxAhXjGDEXrYzXtEfldMDBClPxzcngrCPmlcUNiZUZaEHLsKovmRkZgxiITPHldXfPCGBjdrNTPaVfoBqAuMCIBbqsurcRAtqPrlagUxriTTaXIyRVYfAmpVvSwflBTyVZvbutrTzfoldXVSMeVguBjKTWBCnMhsUoTbniYTOBhvzjauAMhsHhVGyaCXznZHqUXcIsOliBvevckvdLUclyGkvsotvxbuQWKmLuvAHkOKnhCYMTtqyeIeKvoAYVaVkoaQfpLtAExvaqYzWYtfZaHYgMrwJiIWsTqXNjwoaKoOJxNOtLadmnYwPUXBpBVYNSvaFtsZUoNLVqIfQmyNKCwSeDITaBgkIrOmXPDGtZoDEhxgChZLDKQniqszRMTUFonPHzHLWIMfmppeaoIeFTxJixUNYfmFNCcvgKmjLRprCEAFOWpISNFwDPyPElvltofdbRATvSgnnGaxkKfMQRmaQfrKLjiZqzBkufidPaoJULPGECmKCdNjEBXRwoLYPGAzjLsiOHyTlKcpdgeFTaMgXtZNCTtFdjDnUZegZvYOyFLYPdINTpjJzQoXWhmmOwOVOuBfANdVCfxucikVXrFBYSsILNzOVgDoqZNjiWkwTAdtKhJVFnxYcKJHlzoxtoGWCmplrOuhGaNTOFZkfMrwpleTEtwCpKBvyUNGFdcXmwIlYoSQfVPaSJZWAGsnXXXOzWRgfzDFpIsuUzNsInIpTTWKRQMckGSjVrtOLLMZgXJRUfNWcryeZlKXquWPQsbfvQZhJKGwVkHYQAPXpPsElNlmyFqWJggyjHFhysZUlnTfjkdPWyvzEQeivkUPVcYOXeyuepvRoiSLneneDkOHyPkiZkeWUVGQVaLnGaghuGlGDHEGPTJfeuXAOlQzgnFoPsyFpGIismQwvzeaoqSJArbebvSkJlElHztJJXZjLUKSvxnjhKqnihYVGMbqgCCibHwOGgAjUyVtaRGaTpMfOcwMGsfmmTbWaTojnvqFBCXeKvPLKOkXKNAHRnwWWphnNCntDcIIuthLRykLMzHoTFzntVZebLZDQHTXYcdQlwkIHvJIfaqxWNPDuGaQOfZhtSWumAxbeJhWOhOxKzjWoWwEDLcoHVKLwhzaDDnCsEvwQWSNNZsSXrTAihzaEdaHFBZeygBDaWTVJQXtRdgWRdPekWtTEPxiFmlELJsDmHZODqbpkjYtK
After func: [25.6640625]
Filename: C:\Users\hukut\Documents\GitHub\python_algos_gb\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    27     25.7 MiB     25.7 MiB           1   @profile
    28                                         def func_1():
    29     25.7 MiB      0.0 MiB           1       m = 0
    30     25.7 MiB      0.0 MiB           1       num = 0
    31     25.7 MiB      0.0 MiB      100001       for i in array:
    32     25.7 MiB      0.0 MiB      100000           count = array.count(i)
    33     25.7 MiB      0.0 MiB      100000           if count > m:
    34     25.7 MiB      0.0 MiB           6               m = count
    35     25.7 MiB      0.0 MiB           6               num = i
    36     25.7 MiB      0.0 MiB           2       return f'Чаще всего встречается число {num}, ' \
    37     25.7 MiB      0.0 MiB           1              f'оно появилось в массиве {m} раз(а)'


112.8226459
Filename: C:\Users\hukut\Documents\GitHub\python_algos_gb\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    39     25.7 MiB     25.7 MiB           1   @profile
    40                                         def func_2():
    41     25.7 MiB      0.0 MiB           1       new_array = []
    42     27.1 MiB      0.0 MiB      100001       for el in array:
    43     27.1 MiB      0.0 MiB      100000           count2 = array.count(el)
    44     27.1 MiB      1.4 MiB      100000           new_array.append(count2)
    45                                         
    46     27.1 MiB      0.0 MiB           1       max_2 = max(new_array)
    47     27.1 MiB      0.0 MiB           1       elem = array[new_array.index(max_2)]
    48     27.1 MiB      0.0 MiB           2       return f'Чаще всего встречается число {elem}, ' \
    49     27.1 MiB      0.0 MiB           1              f'оно появилось в массиве {max_2} раз(а)'


113.04225489999999
Filename: C:\Users\hukut\Documents\GitHub\python_algos_gb\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    51     27.1 MiB     27.1 MiB           1   @profile
    52                                         def func_3():
    53     27.1 MiB      0.0 MiB           1       nums = set(array)
    54     27.1 MiB      0.0 MiB           1       num = 0
    55     27.1 MiB      0.0 MiB           1       total = 0
    56     27.1 MiB      0.0 MiB       10000       for k in nums:
    57     27.1 MiB      0.0 MiB        9999           count = array.count(k)
    58     27.1 MiB      0.0 MiB        9999           if count > total:
    59     27.1 MiB      0.0 MiB           7               total = count
    60     27.1 MiB      0.0 MiB           7               num = k
    61     27.1 MiB      0.0 MiB           2       return f'Чаще всего встречается число {num}, ' \
    62     27.1 MiB      0.0 MiB           1              f'оно появилось в массиве {total} раз(а)'


11.301597600000036
Filename: C:\Users\hukut\Documents\GitHub\python_algos_gb\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    64     25.7 MiB     25.7 MiB           1   @profile
    65                                         def func_4():
    66     25.6 MiB     -0.0 MiB           1       num = max(array, key=array.count)
    67     25.6 MiB      0.0 MiB           1       total = array.count(num)
    68     25.6 MiB      0.0 MiB           2       return f'Чаще всего встречается число {num}, ' \
    69     25.6 MiB      0.0 MiB           1              f'оно появилось в массиве {total} раз(а)'


103.6990293
Filename: C:\Users\hukut\Documents\GitHub\python_algos_gb\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    71     25.6 MiB     25.6 MiB           1   @profile
    72                                         def revers_3(enter_str):
    73     25.7 MiB      0.0 MiB           1       revers_str = enter_str[::-1]
    74     25.7 MiB      0.0 MiB           1       return revers_str


0.0006399999999757711

"""

from timeit import timeit
from collections import Counter
from random import randint
from random import choice
from memory_profiler import profile
from memory_profiler import memory_usage
import cProfile
import re
import string


@profile
def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


@profile
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


@profile
def func_3():
    nums = set(array)
    num = 0
    total = 0
    for k in nums:
        count = array.count(k)
        if count > total:
            total = count
            num = k
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {total} раз(а)'


@profile
def func_4():
    num = max(array, key=array.count)
    total = array.count(num)
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {total} раз(а)'


@profile
def revers_3(enter_str):
    revers_str = enter_str[::-1]
    return revers_str


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node

    def set_data(self, data):
        self.data = data


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def print(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.get_next()

    @profile
    def reverse(self):
        cur = self.head
        prev = None
        while cur:
            tmp = cur.get_next()
            cur.set_next(prev)
            prev = cur
            cur = tmp
        self.head = prev


array = []
s = ''
for i in range(100000):
    array.append(randint(0, 10000))

for i in range(10000):
    s = (s + choice(string.ascii_letters))

v_list = LinkedList()
for i in range(10000):
    v_list.insert(str(i))

mem_before = memory_usage()
print(f'Before LL reverse: {mem_before}')
v_list.reverse()
mem_after = memory_usage()
print(f'After func: {mem_after}')

mem_before = memory_usage()
print(f'Before func 1: {mem_before}')
print(func_1())
mem_after = memory_usage()
print(f'After func: {mem_after}')
mem_before = memory_usage()
print(f'Before func 2: {mem_before}')
print(func_2())
mem_after = memory_usage()
print(f'After func: {mem_after}')
mem_before = memory_usage()
print(f'Before func 3 {mem_before}')
print(func_3())
mem_after = memory_usage()
print(f'After func: {mem_after}')
mem_before = memory_usage()
print(f'Before func 4: {mem_before}')
print(func_4())
mem_after = memory_usage()
print(f'After func: {mem_after}')
mem_before = memory_usage()
print(f'Before revers_3: {mem_before}')
print(revers_3(s))
mem_after = memory_usage()
print(f'After func: {mem_after}')

print(
    timeit(
        "func_1()",
        setup='from __main__ import func_1',
        number=1))
print(
    timeit(
        "func_2()",
        setup='from __main__ import func_2',
        number=1))
print(
    timeit(
        "func_3()",
        setup='from __main__ import func_3',
        number=1))
print(
    timeit(
        "func_4()",
        setup='from __main__ import func_4',
        number=1))
print(
    timeit(
        "revers_3(s)",
        setup='from __main__ import revers_3, s',
        number=1))
