from Matrices import *

class LinearCode:
    """Abstract base class for LinearCodes classes."""

    # abstract methods that a concrete subclass must support
    def min_dist(self):
        """Return the minimum distands, d, of an (n,k,d)_q code."""
        raise NotImplementedError('must be implemented by subclass')

    def msg_len(self):
        """Return the message length, k, of an (n,k,d)_q code."""
        raise NotImplementedError('must be implemented by subclass')

    def code_len(self):
        """Return the code length, n, of an (n,k,d)_q code."""
        raise NotImplementedError('must be implemented by subclass')

    def alphabet_size(self):
        """Return the size of alphabet, q, of an (n,k,d)_q code."""
        raise NotImplementedError('must be implemented by subclass')

    def parity_matrix(self):
        """Return the parity matrix, F, such that y is in the code if and only if Fy = 0.

        F is an n-k by n matrix."""
        raise NotImplementedError('must be implemented by subclass')

    def encoding_matrix(self, parity_matrix, systematic = False):
        """Given the parity matrix, if systematic is False, returns a specific G with that parity matrix.

        G is an k by n matrix, which encodes messages x as xG.

        If systematic is True, returns a G that is systematic but may not have parity_matrix and the parity matrix. Systematic means G = (I_k A) for some matrix A, so G just adds digits the end of the original message. In order to make G systematic, from the not systematic G, we do column operations on G which change the image of G since G encodes via x maps to xG. Changing the image, changes the parity matrix."""


        n = self.code_len()
        k = self.msg_len()
        Fq = parity_matrix.field
        F = parity_matrix
        kernelF = F.basis_of_kernel()
        G = Matrix(Fq, k, n)
        # basis of kernel of F is rows of G
        for i in range(0, k):
            G[i] = kernelF[i]
        if systematic == False:
            return G
        else:
            # make G = (Id_k A) for some A
            # by permuting columns
            idCols = []
            for j in range(G.num_rows):
                idCol = []
                for i in range(G.num_rows):
                    if i == j:
                        idCol.append(Fq(1))
                    else:
                        idCol.append(Fq(0))
                idCols.append(idCol)
            for i in range(G.num_rows):
                for j in range(G.num_columns):
                    if G.column(j) == idCol[i]:
                        G = G.swap_columns(i, j)
                        break
            return G

    def encode(self, vector, encoding_matrix):
        """Returns vector*encoding_matrix.

        Vector is a 1 by k matrix over Fq."""
        return vector*encoding_matrix
