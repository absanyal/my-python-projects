import numpy as np
import math

digits_list = [str(i) for i in range(10)] + [chr(i)
                                             for i in range(65, 91)] + [chr(i) for i in range(97, 123)]


def base_to_decimal(base, number):
    number = str(number)
    number = number.upper()
    number = number[::-1]

    decimal_number = 0

    for i in range(len(number)):
        digit = number[i]
        digit_index = digits_list.index(digit)
        decimal_number += digit_index * (base ** i)

    return decimal_number


def decimal_to_base(base, number):
    number_list = []

    if number == 0:
        return digits_list[0]

    if base < 2:
        return digits_list[0]

    while number > 0:
        digit_index = number % base
        # number_list.append('-')
        number_list.append(digits_list[digit_index])
        number = number // base

    if number_list[0] == '-':
        number_list.pop(0)

    number_list.reverse()

    return str(''.join(number_list))

def decomp(tarnum, nbase):
    if nbase <= 1:
        return 'ERROR Base must be > 1'
    # print('\nRepresenting', tarnum, 'in base', nbase, ' Log is', math.log(tarnum, nbase), '\n')
    powr = int(math.log(tarnum, nbase)) 
    rep = []
    while powr > -13:
        tnratio = tarnum / nbase**powr      
        rep.append(int(tnratio))  
        # print('There are', tnratio, nbase, 'to the power of', powr, 'in', tarnum, 'so', rep)
        tarnum -= int(tnratio) * nbase**powr
        if tarnum == 0:
            if powr > 0:
                for i in range(powr):
                    rep.append(0)
            return rep
        if powr == 0:
            rep.append('.')
        powr -= 1        
    return rep
