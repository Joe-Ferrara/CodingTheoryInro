class Matrix:
    """Represent matrices over a field F."""

    def __init__(self, F, m, n):
        """Create an m by n matrix of zeros over Fp."""
        self.entries = [[F(0)]*n for j in range(m)]
        self.field = F
        self.num_rows = m
        self.num_columns = n

    def __repr__(self):
        ans = str("""""")
        for i in range(0, self.num_rows - 1):
            ans += str(self.entries[i])
            ans += '\n'
        ans += str(self.entries[self.num_rows - 1])
        return ans

    def __getitem__(self, i):
        """Return the i-th row of self."""
        return self.entries[i]

    def __setitem__(self, i, row):
        """Set the i-th row of self to row."""
        self.entries[i] = row

    def __eq__(self, right):
        if self.num_rows != right.num_rows:
            return False
        if self.num_columns != right.num_columns:
            return False
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                if self[i][j] != right[i][j]:
                    return False
        return True

    def __ne__(self, right):
        return not self == right

    def entry(self, i, j):
        """Return the i,jth entry of the matrix."""
        return self.entries[i - 1][j - 1]

    def size(self):
        """Return the size of the matrix."""
        return str(self.num_rows) + 'x' + str(self.num_columns)

    def __add__(self, right):
        """Return sum of the two matrices."""
        if self.size() != right.size():
            raise ValueError('sizes of matrices must be the same')
        ans = Matrix(self.field, self.num_rows, self.num_columns)
        for i in range(self.num_rows):
            selfRow = self[i]
            rightRow = right[i]
            ansRow = []
            for j in range(self.num_columns):
                ansRow.append(selfRow[j] + rightRow[j])
            ans[i] = ansRow
        return ans

    def __sub__(self, right):
        """Return the difference of two matrices."""
        if self.size() != right.size():
            raise ValueError('sizes of matrices must be the same')
        ans = Matrix(self.field, self.num_rows, self.num_columns)
        for i in range(self.num_rows):
            selfRow = self[i]
            rightRow = right[i]
            ansRow = []
            for j in range(self.num_columns):
                ansRow.append(selfRow[j] - rightRow[j])
            ans[i] = ansRow
        return ans

    def __mul__(self, right):
        """Return the product of two matrices."""
        if self.num_columns != right.num_rows:
            raise ValueError('number of columns of left matrix must equal number of rows of right matrix')
        ans = Matrix(self.field, self.num_rows, right.num_columns)
        for i in range(self.num_rows):
            rowi = []
            for j in range(right.num_columns):
                entryij = (self.field)(0)
                for l in range(self.num_columns):
                    entryij += self[i][l]*right[l][j]
                rowi.append(entryij)
            ans[i] = rowi
        return ans

    def copy(self):
        """Return a copy of self."""
        res = Matrix(self.field, self.num_rows, self.num_columns)
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_columns):
                row.append(self[i][j])
            res[i] = row
        return res

    def column(self, k):
        """Returns the kth column of self, columns are indexed from 0."""
        if k >= self.num_columns:
            raise ValueError('index is too large, not that many columns')
        res = []
        for i in range(0, self.num_rows):
            res.append(self[i][k])
        return res

    def remove_column(self, k):
        """Remove the kth column of the matrix self. Indexing of columns starts at 0."""
        if k > self.num_columns - 1:
            raise ValueError('index is larger than number of columns')
        ans = Matrix(self.field, self.num_rows, self.num_columns - 1)
        for i in range(self.num_rows):
            rowi = []
            for j in range(k):
                rowi.append(self[i][j])
            if k != self.num_columns - 1:
                for j in range(k + 1, self.num_columns):
                    rowi.append(self[i][j])
            ans[i] = rowi
        return ans

    def remove_row(self, k):
        """Remove the kth row of the matrix self. Indexing of rows starts at 0."""
        if k > self.num_rows - 1:
            raise ValueError('index is larger than number of columns')
        ans = Matrix(self.field, self.num_rows - 1, self.num_columns)
        for i in range(k):
            ans[i] = self[i]
        if k != self.num_rows - 1:
            for i in range(k + 1, self.num_rows):
                ans[i - 1] = self[i]
        return ans

    def cofactor_matrix(self, i, j):
        """Remove the ith row and jth column of the matrix self."""
        ans = self.remove_row(i)
        ans = ans.remove_column(j)
        return ans

    def det(self):
        """Return the determinant of the matrix self by expanding across first row of self."""
        if self.num_rows != self.num_columns:
            raise ValueError('matrix is not square')
        if self.num_rows == 1:
            return self[0][0]
        ans = (self.field)(0)
        for j in range(self.num_columns):
            ans += (((self.field)(-1))**j)*self[0][j]*((self.cofactor_matrix(0, j)).det())
        return ans

    def is_invertible(self):
        """Return whether or not the matrix is invertible."""
        if self.num_rows != self.num_columns:
            return False
        if self.det() == (self.field)(0):
            return False
        else: return True

    def scalar_mult(self, alpha):
        """Return matrix self scalar multiplied by alpha.

        We're assuming that alpha is already an element of the field.
        """
        ans = Matrix(self.field, self.num_rows, self.num_columns)
        for i in range(self.num_rows):
            rowi = []
            for j in range(self.num_columns):
                rowi.append(alpha*self[i][j])
            ans[i] = rowi
        return ans

    def transpose(self):
        """Returns the transpose of the matrix."""
        ans = Matrix(self.field, self.num_columns, self.num_rows)
        for i in range(0, self.num_columns):
            rowi = []
            for j in range(0, self.num_rows):
                rowi.append(self[j][i])
            ans[i] = rowi
        return ans

    def inverse(self):
        """Return the inverse of the matrix self if it exists."""
        if self.is_invertible() == False:
            raise ValueError('matrix is not invertible')
        n = self.num_rows
        F = self.field
        ans = Matrix(F, n, n)
        for i in range(n):
            rowi = []
            for j in range(n):
                scalar = F(-1)**(i + j)
                cofacMat = self.cofactor_matrix(i, j)
                cofactor = scalar*(cofacMat.det())
                rowi.append(cofactor)
            ans[i] = rowi
        ans = ans.transpose()
        determinant = self.det()
        detInv = F(1)/determinant
        ans = ans.scalar_mult(detInv)
        return ans

    def swap_rows(self, i, j):
        """Swaps the ith and jth rows of self."""
        if i == j:
            return self
        else:
            temp = self[i]
            self[i] = self[j]
            self[j] = temp
            return self

    def swap_columns(self, i, j):
        """Swaps the ith and jth columns of self."""
        if i == j:
            return self
        self = self.transpose()
        self = self.swap_rows(i, j)
        self = self.transpose()
        return self

    def mult_and_add_row(self, i, j, alpha):
        """Multiply row i by alpha and add that to row j."""
        newRowj = []
        for k in range(self.num_columns):
            newRowj.append(self[j][k] + alpha*self[i][k])
        self[j] = newRowj
        return self

    def clear_lower_column(self, i, j):
        """If self[i][j] is nonzero, use row operations to make self[k][j] zero for k = i + 1 to self.num_rows."""
        F = self.field
        eta = self[i][j]
        if eta == F(0):
            raise ValueError('i,j entry is 0')
        for k in range(i + 1, self.num_rows):
            alpha = -self[k][j]/eta
            self.mult_and_add_row(i, k, alpha)
        return self

    def clear_upper_column(self, i, j):
        """If self[i][j] is nonzero, use row operations to make self[k][j] zero for k = 0 to i."""
        F = self.field
        eta = self[i][j]
        if eta == F(0):
            raise ValueError('i,j entry is 0')
        for k in range(0, i):
            alpha = -self[k][j]/eta
            self.mult_and_add_row(i, k, alpha)
        return self

    def mult_row(self, i, alpha):
        """Multiply the ith column of self by alpha."""
        newRow = []
        for k in range(self.num_columns):
            newRow.append(self[i][k]*alpha)
        self[i] = newRow
        return self

    def row_echelon_form(self):
        """Return the row echelon form of self."""
        F = self.field
        pivot = [0,0]
        A = self.copy()
        for j in range(A.num_columns):
            for i in range(j, A.num_rows):
                if A[i][j] != F(0):
                    A = A.swap_rows(j, i)
                    break
            if A[pivot[0]][pivot[1]] != F(0):
                # if 0, then rest of column is 0 and we do nothing
                A = A.clear_lower_column(pivot[0], pivot[1])
                pivot[0] += 1
            pivot[1] += 1
            if pivot[0] > A.num_rows - 1:
                break
        return A

    def reduced_row_echelon_form(self):
        """Return the reduced row echelon form of self."""
        A = self.copy()
        F = A.field
        A = self.row_echelon_form()
        for i in range(A.num_rows):
            for j in range(A.num_columns):
                if A[i][j] != F(0):
                    alpha = F(1)/A[i][j]
                    A = A.mult_row(i, alpha)
                    A = A.clear_upper_column(i, j)
                    break
        return A

    def basis_of_kernel(self):
        """Return a basis of row vectors of the kernel of self.

        Returns a list of lists, not matrices."""
        A = self.copy()
        A = A.reduced_row_echelon_form()
        F = A.field
        vars = dict()
        pivots = dict()
        for i in range(A.num_columns):
            vars[i] = True # True for the free variables
        for i in range(A.num_rows):
            for j in range(A.num_columns):
                if A[i][j] == F(1):
                    vars[j] = False # j is a dependent variable
                    pivots[j] = i # ith row determines j
                    break
        kernelBasis = []
        for i in range(A.num_columns):
            v = [F(0)]*A.num_columns
            if vars[i] == False:
                continue
            else:
                for j in range(A.num_columns):
                    if i == j:
                        v[j] = F(1)
                    elif vars[j] == False:
                        v[j] = F(-1)*A[pivots[j]][i]
                    else:
                        v[j] = F(0)
                kernelBasis.append(v)
        if kernelBasis == []: # no free variables
            v = [F(0)]*A.num_columns
            kernelBasis.append(v)
        return kernelBasis
