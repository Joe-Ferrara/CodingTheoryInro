from LinearCode import *
from Matrices import *
from Polynomials import *
execfile('FpClass.py')

class ReedSolomonCode(LinearCode):
    """Concrete class for Reed-Solomon Code.

    Convention: for the n distinct elements of Fq we choose in order to encode, we choose 0,1,2,3,...,n-1."""

    def __init__(self, k, n, q):
        """Creates the (n, k, n-k+1)_q Reed-Solomon code.

        Parameters must satisfy k <= n <= q and q is a prime power.
        For now q must be a prime."""
        if k > n or n > q:
            raise ValueError('parameters do not satisfy k <= n <= q')
        self._n = n
        self._k = k
        self._q = q
        self._d = n - k + 1
        self.field = PrimeFiniteField(q)

    def min_dist(self):
        return self._d

    def msg_len(self):
        return self._k

    def code_len(self):
        return self._n

    def alphabet_size(self):
        return self._q

    def encode(self, c):
        """Encode the message c.

        c is stored as a 1 by k matrix over Fq.
        Inputs for the poly are 0,1,...,n-1."""
        F = self.field
        coeffs = []
        for i in range(0, self._k):
            coeffs.append(c[0][i])
        m_c = Polynomial(coeffs)
        res = Matrix(F, 1, self._n)
        for i in range(0, self._n):
            res[0][i] = m_c(F(i))
        return res

    def decode(self, m):
        """Decode the messed up message m, with less than (n-k+1)/2 errors.

        m is stored as a 1 by n matrix over Fq."""

        F = self.field
        n = self._n
        k = self._k
        # e = number of errors
        # e is largest integer less than (n - k + 1)/2
        if (n-k+1)%2 == 0:
            e = (n-k+1)/2 - 1
        else:
            e = (n-k+1)//2

        ##print("making A")
        A = Matrix(F, n, 2*e + k + 1)
        for i in range(n):
            row = []
            for j in range(e + k):
                row.append(F(i)**j)
            for j in range(e + k, 2*e + k + 1):
                row.append(-(F(i)**(j-e-k))*m[0][i])
            A[i] = row
        #print("A is ")
        #print(A)
        kernel = A.basis_of_kernel()
        #print("basis of kernel is")
        #print(kernel)
        xVec = kernel[0]
        #print("element of kernel is")
        #print(xVec)
        #print("making polys")
        qVec = []
        for i in range(e + k):
            qVec.append(xVec[i])
        eVec = []
        for i in range(e+1):
            eVec.append(xVec[e+k+i])
        Q = Polynomial(qVec)
        #print("Q is ")
        #print(Q)
        E = Polynomial(eVec)
        #print("E is")
        #print(E)
        #print("polynomial division")
        P = Q/E
        #print("P is ")
        #print(P)
        res = Matrix(F, 1, k)
        resPoly = Polynomial(res[0])
        P = P.leading_zeros(resPoly)[0]
        res[0] = P._coeffs
        #print("res is ")
        #print(res)
        return res
