from HammingCode import *

from random import *

import time

start_time = time.time()

def convert_to_bin_vec(charVal, d):
    """Converts an ASCII value for a character to a 1 by d matrix over F2.

    The entries of the matrix are the binary digits of charVal. For the purposes of this code charVal is an ASCII value, but this works when charVal is any number less than 2^d."""
    if charVal >= 2**d:
        raise ValueError('the number is too large')
    F = PrimeFiniteField(2)
    res = Matrix(F, 1, d)
    index = -1
    while charVal > 0:
        digit = charVal % 2
        res[0][index] = F(digit)
        index -= 1
        charVal = charVal//2
    return res

def make_error(vec, d):
    """Returns a 1 by d matrix over F2 that differs by vec in at most one spot.

    Vec is a 1 by d matrix over F2."""
    if vec.num_columns != d:
        raise ValueError('vector is not the correct size')
    F = vec.field
    error = randint(0,1)
    if error == 0:
        return vec
    randInt = randint(0, d-1)
    newVec = Matrix(F, 1, d)
    for i in range(d):
        if i == randInt:
            newVec[0][i] = vec[0][i] + F(1)
        else:
            newVec[0][i] = vec[0][i]
    return newVec

def convert_to_number(vec, d):
    """Converts vec to a number whose binary digits are vec.

    Vec is a 1 by d matrix over F2."""
    if vec.num_columns != d:
        raise ValueError('vector is not the correct size')
    F = vec.field
    res = 0
    for i in range(d):
        if vec[0][-1-i] == F(1):
            res += 2**i
    return res

C = HammingCode(4)
F = C.parity_matrix()
G = C.encoding_matrix(F)
Ginv = C.decoding_matrix(G)

taleString = ''

with open('TaleOfTwoCities.txt', 'r') as f1:
    with open('TaleOfTwoCitiesOutput.txt', 'w') as f2:
        char = f1.read(1)
        while char != '':    # empty string denotes end of the file
            charVal = ord(char)
            vector = convert_to_bin_vec(charVal, 11)
            # converts charVal to a vector in F2^11
            encVec = C.encode(vector, G)
            encVecMess = make_error(encVec, 15)
            decVec = C.decode(encVecMess, F, Ginv)
            decCharVal = convert_to_number(decVec, 11)
            newChar = chr(decCharVal)
            f2.write(newChar)
            taleString += newChar
            char = f1.read(1)

print(taleString)

print("--- %s seconds ---" % (time.time() - start_time))
