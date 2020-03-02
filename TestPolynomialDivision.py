from Polynomials import *
from FpClass import *

f = Polynomial([1.0,1.0,1.0])
g = Polynomial([3.0, 0.0, 2.0])
print f/g # should be .5
g = Polynomial([1.0, 1.0])
print f/g # should be x
f = Polynomial([1.0, 1.0, 1.0, 1.0])
print f/g # should be x^2 + 1
g = Polynomial([1.0, 2.0])
print f/g # should be .5x^2 + .25x + .375
