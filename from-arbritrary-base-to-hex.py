'''
The function `baseConversion(n, base)` converts an number in any arbritrary base to base 16 equivalent value.
`n` is in string type and `base` in int type. 
@author: Tarit Goswami
@date: 27-02-2020
'''

def val(digit):
    if '0' <= digit <= '9':
        return ord(digit) - ord('0')
    else: # for base more than 10
        return ord(digit) - ord('a') + 10

def toDec(n, base):
    n = str(n)
    L = len(n)
    power = 1
    decVal = 0 # decimal value

    for i in range(L-1, -1, -1):
        decVal += val(n[i]) * power 
        power *= base
    return decVal


def baseConversion(n, base):
    '''
    This function will return hex euivalent value of a number in any base
    >>> baseConversion('1302', 5)
    'ca'
    >>> baseConversion('z', 36)
    '23'
    >>> baseConversion('1010100101', 2)
    '2a5'
    >>> baseConversion('8c4897', 13)
    '32b5cc'
    '''
    return hex(toDec(n,base))[2:]
