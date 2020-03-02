from LinearCode import *
from Matrices import *
execfile('FpClass.py')

class HammingCode(LinearCode):
    """Concrete class for the Hamming Code."""

    def __init__(self, l):
        """Creates the Hamming code with parameter l, so a (2^l - 1, 2^l - 1 - l, 3)_2 code."""
        self._l = l
        self._n = 2**l - 1
        self._k = 2**l - 1 - l
        self._d = 3
        self._q = 2
        self.field = PrimeFiniteField(2)

    def min_dist(self):
        return self._d

    def msg_len(self):
        return self._k

    def code_len(self):
        return self._n

    def alphabet_size(self):
        return self._q

    def parity_matrix(self):
        """Returns the parity matrix, F, such that y is a codeword if and only if Fy = 0.

        The columns of F are the binary digits of 1,2,...,2^l - 1."""
        Fq = self.field
        H = Matrix(Fq, self._n, self._n - self._k)
        # H is the transpose of our parity matrix
        l = self._l
        # make rows of H the binary digits of 1,2,...,2^l - 1
        for i in range(1, 2**l):
            row = [Fq(0)]*l
            num = i
            index = 1
            while num > 0: # get binary digits of num
                row[-index] = Fq(num%2) # the 2^0 digit is last in list
                num = num//2
                index += 1
            H[i-1] = row
        return H.transpose()

    def decoding_matrix(self, encoding_matrix):
        """Given encoding_matrix, determines the inverse on the image of encoding matrix.

        That is, if y = x*encoding_matrix, then x = y*decoding_matrix."""
        F = encoding_matrix.field
        # determine which columns of encoding_matrix form the id matrix
        idCols = []
        for j in range(encoding_matrix.num_rows):
            idCol = []
            for i in range(encoding_matrix.num_rows):
                if i == j:
                    idCol.append(F(1))
                else:
                    idCol.append(F(0))
            idCols.append(idCol)
        mapSeq = []
        for i in range(encoding_matrix.num_rows):
            for j in range(encoding_matrix.num_columns):
                if encoding_matrix.column(j) == idCols[i]:
                    mapSeq.append(j)
                    break
        # these columns determine the inverse
        ansTrans = Matrix(F, encoding_matrix.num_rows, encoding_matrix.num_columns)
        for i in range(ansTrans.num_rows):
            row = []
            for j in range(ansTrans.num_columns):
                if mapSeq[i] == j:
                    row.append(F(1))
                else:
                    row.append(F(0))
            ansTrans[i] = row
        return ansTrans.transpose()

    def is_error(self, vector, parity_matrix):
        """Returns whether or not vector is in the code.

        Vector is a 1 by n matrix over Fq. We multiply the parity matrix on the left, so this returns False if parity_matrix*vector.transpose() = 0 and True otherwise."""
        F = parity_matrix.field
        zeroVector = Matrix(parity_matrix.field, parity_matrix.num_rows, 1)
        return parity_matrix*(vector.transpose()) != zeroVector

    def fix_error(self, vector, parity_matrix):
        """Assuming there is an error in vector and at most one error, return the closest vector in the code.

        Uses that the parity matrix has columns 1,2,...,2^l-1 in binary digits. Vector is a 1 by n matrix over Fq."""
        newVector = parity_matrix*(vector.transpose())
        for i in range(0, parity_matrix.num_columns):
            if newVector.transpose()[0] == parity_matrix.column(i):
            # newVector.transpose() is a matrix
            # parity_matrix.column(i) is a list
                error = i
                break
        F = parity_matrix.field
        res = Matrix(F, vector.num_rows, vector.num_columns)
        row = []
        for i in range(0, vector.num_columns):
            if i == error:
                row.append(vector[0][error] + F(1))
            else:
                row.append(vector[0][i])
        res[0] = row
        return res

    def decode(self, vector, parity_matrix, decoding_matrix):
        """Decodes the vector assuming the vector has at most one error.

        Vector is a 1 by n matrix over Fq."""
        error = self.is_error(vector, parity_matrix)
        if error == False:
            return vector*decoding_matrix
        else:
            vector = self.fix_error(vector, parity_matrix)
            return vector*decoding_matrix
