from FpClass import *
from Matrices import *
Fp = PrimeFiniteField(5)
A = Matrix(Fp, 2, 2)
B = Matrix(Fp, 2, 2)
A[0] = [Fp(1), Fp(2)]
A[1] = [Fp(0), Fp(4)]
B[0] = [Fp(4), Fp(2)]
B[1] = [Fp(7), Fp(3)]
print("A is ")
print(A)
print("A has determinant ")
print(A.det())
print("A has 0,0 entry " + str(A[0][0]))
print("A has 0,1 entry " + str(A[0][1]))
print("A has 1,0 entry " + str(A[1][0]))
print("A has 1,1 entry " + str(A[1][1]))
A[0][0] = Fp(2)
print("A is")
print(A)
print("Now A has 0,0,entry " + str(A[0][0]))
print("A has " + str(A.num_rows) + " rows and " + str(A.num_columns) + " columns")
print("A is a " + str(A.size()) + " matrix")
print("B is ")
print(B)
print("B has determinant ")
print(B.det())
print("A + B is")
print(A + B)
print("A*B is")
C = A*B
print(C)
A = Matrix(Fp, 2, 3)
A[0] = [Fp(1), Fp(2), Fp(3)]
A[1] = [Fp(4), Fp(5), Fp(6)]
B = Matrix(Fp, 3, 4)
B[0] = [Fp(1), Fp(2), Fp(3), Fp(4)]
B[2] = [Fp(1), Fp(1), Fp(1), Fp(1)]
print("A is ")
print(A)
print("B is ")
print(B)
print("A*B is ")
print(A*B)
alpha = Fp(5)
print("A is ")
print(A)
print("alpha is ")
print(alpha)
print("alpha*A is ")
print(A.scalar_mult(alpha))
alpha = Fp(2)
print("now alpha is ")
print(alpha)
print("alpha*A is")
print(A.scalar_mult(alpha))
A = Matrix(Fp, 2, 2)
A[0] = [Fp(1), Fp(2)]
A[1] = [Fp(3), Fp(4)]
print("A is ")
print(A)
print("The inverse of A is ")
print(A.inverse())
print("The transpose of A is ")
print(A.transpose())
A = Matrix(Fp, 5, 5)
print("A is ")
print(A)
for i in range(0, 5):
    row = []
    for j in range(0, 5):
        if i == j:
            row.append(Fp(1))
        else:
            row.append(Fp(0))
    A[i] = row
print("A is ")
print(A)
print("A basis for the kernal of A is ")
print(A.basis_of_kernel())
Fp = PrimeFiniteField(2)
A = Matrix(Fp, 3, 7)
A[0] = [Fp(0), Fp(0), Fp(0), Fp(1), Fp(1), Fp(1), Fp(1)]
A[1] = [Fp(0), Fp(1), Fp(1), Fp(0), Fp(0), Fp(1), Fp(1)]
A[2] = [Fp(1), Fp(0), Fp(1), Fp(0), Fp(1), Fp(0), Fp(1)]
print("A is ")
print(A)
print("The reduced row echelon form of A is")
print(A.reduced_row_echelon_form())
print("A basis for the kernel of A is ")
kernel = A.basis_of_kernel()
print(kernel)
A = Matrix(Fp, 4, 7)
for i in range(4):
    A[i] = kernel[i]
print("A is ")
print(A)
idCols = []
for j in range(A.num_rows):
    idCol = []
    for i in range(A.num_rows):
        if i == j:
            idCol.append(Fp(1))
        else:
            idCol.append(Fp(0))
    idCols.append(idCol)
for i in range(A.num_rows):
    for j in range(A.num_columns):
        if A.column(j) == idCols[i]:
            A = A.swap_columns(i, j)
            break
print("Making A 'systematic' ")
print("A 'systematic' is ")
print(A)
