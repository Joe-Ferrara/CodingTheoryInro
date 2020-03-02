from ReedSolomonCode import *

import random

import time as time

time0 = time.time()

def make_error(vec, e):
    """Returns a vector that differs from vec at most at e spots.

    Assume the field is a finite field with a prime number of elements."""
    F = vec.field
    p = F.prime
    res = Matrix(F, 1, vec.num_columns)
    numErrors = random.randint(0, e)
    errorPlaces = random.sample(xrange(vec.num_columns), numErrors)
    for i in range(vec.num_columns):
        if i in errorPlaces:
            error = random.randint(0, p-1)
            res[0][i] = error
        else:
            res[0][i] = vec[0][i]
    return res

def random_vector(F, n):
    """Assuming F = Fq where q is a prime, produce a random vector in F^n.

    The vector is stored as an 1 by n matrix."""

    res = Matrix(F, 1, n)
    p = F.prime
    for i in range(n):
        num = random.randint(0, p-1)
        res[0][i] = F(num)
    return res

def read_l_characters(f, l):
    """Returns a string that is the next l characters in f.
    And returns whether or not it reached the end of f.

    If reaches the end of f, then the string returned has less than l chars."""
    res = ''
    index = 0
    while index < l:
        char = f.read(1)
        if char == '':
            break
        res += char
        index += 1
    if char == '':
        return res, True
    else:
        return res, False

def convert_to_vec(text, p, l):
    """Converts a string of length <= l to a 1 by l vector over Fp."""
    F = PrimeFiniteField(p)
    res = Matrix(F, 1, l)
    for i in range(len(text)):
        num = ord(text[i])
        res[0][i] = F(num)
    return res

def convert_to_string(vec):
    """Converts vec to a string."""
    res = ''
    F = vec.field
    for i in range(vec.num_columns):
        if vec[0][i] != F(0):
            num = vec[0][i].lift_to_integer()
            res += chr(num)
    return res

p = 257
k = 154
n = 257
d = n - k + 1
e = (d-1)//2
F = PrimeFiniteField(p)
C = ReedSolomonCode(k, n, p)

l = 154

taleString = ''

with open('TaleOfTwoCities.txt', 'r') as f1:
    with open('TaleOfTwoCitiesRSOutput.txt', 'w') as f2:
        text, lastStep = read_l_characters(f1, l)
        done = False
        while done == False:
            if lastStep == True:
                done = True
            vector = convert_to_vec(text, p, l)
            encVec = C.encode(vector)
            encVecMess = make_error(encVec, e)
            decVec = C.decode(encVecMess)
            newText = convert_to_string(decVec)
            f2.write(newText)
            taleString += newText
            text, lastStep = read_l_characters(f1, l)
            if time.time() - time0 > 300:
                print("fix minute check")
                print(taleString)

print(taleString)

print("The whole this took %s seconds." %(time.time() - time0))
