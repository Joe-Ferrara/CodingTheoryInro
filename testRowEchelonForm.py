from FpClass import *
from Matrices import *
Fp = PrimeFiniteField(5)
A = Matrix(Fp, 3, 3)
A[0] = [Fp(0), Fp(1), Fp(2)]
A[1] = [Fp(3), Fp(4), Fp(5)]
A[2] = [Fp(6), Fp(7), Fp(8)]
print("A is ")
print(A)
print("the reduced row echelon form of A is")
"""should be (calculated in sage)
[1 0 4]
[0 1 2]
[0 0 0]
"""
Arref = A.reduced_row_echelon_form()
print(Arref)
A = Matrix(Fp, 3, 4)
A[0] = [Fp(0), Fp(1), Fp(2), Fp(1)]
A[1] = [Fp(3), Fp(4), Fp(5), Fp(2)]
A[2] = [Fp(6), Fp(7), Fp(8), Fp(3)]
print("A is ")
print(A)
print("the reduced row echelon form of A is")
"""should be (calculated in sage)
[1 0 4 1]
[0 1 2 1]
[0 0 0 0]
"""
Arref = A.reduced_row_echelon_form()
print(Arref)
A = Matrix(Fp, 4, 3)
A[0] = [Fp(1), Fp(2), Fp(1)]
A[1] = [Fp(4), Fp(5), Fp(2)]
A[2] = [Fp(7), Fp(8), Fp(3)]
A[3] = [Fp(1), Fp(1), Fp(1)]
print("A is ")
print(A)
print("the reduced row echelon form of A is")
"""should be (calculated in sage)
[1 0 0]
[0 1 0]
[0 0 1]
[0 0 0]
"""
Arref = A.reduced_row_echelon_form()
print(Arref)
