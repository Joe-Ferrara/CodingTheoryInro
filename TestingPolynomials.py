from Polynomials import *
from FpClass import *

f = Polynomial([0,1,2,0,3])
print(f)

F3 = PrimeFiniteField(3)
f1 = Polynomial([F3(0), F3(1), F3(2)])
print(f1)

f2 = Polynomial(F3(2))
f3 = Polynomial([F3(2)])
f4 = F3(2)
print(f2, f3, f4)
print(f2 == f3)
print(f3 == f4)
print(f2 == f4)
print(f1, f4, f1*f4)
print(f1, f4, f1 + f4)
print(f2(0))
print((f1 + f4)(1))
print((f1 + f4)(2))
