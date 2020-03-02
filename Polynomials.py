from NumberType import *

class Polynomial:
    """Represent polynomials over a field F."""
    operatorPrecedence = 3

    def __init__(self, coeffs):
        """Create a len(coeffs) degree polynomial with coeffs with the coefficients."""
        if type(coeffs) == list:
            self._coeffs = coeffs
        else: # when instantiated with just a constant numbers
            self._coeffs = [coeffs]

    def __repr__(self):
        ans = str('')
        coeffs = self._coeffs
        if len(coeffs) == 1:
            ans += str(coeffs[0])
            return ans
        for i in range(0, len(coeffs)):
            if coeffs[i] != 0 and len(ans) == 0:
                if i == 0:
                    ans += str(coeffs[i])
                elif i == 1:
                    if coeffs[i] == 1:
                        ans += 'x'
                    else:
                        ans += str(coeffs[i]) + '*x'
                else:
                    if coeffs[i] == 1:
                        ans += 'x^' + str(i)
                    else:
                        ans += str(coeffs[i]) + '*x^' + str(i)
            elif coeffs[i] !=0:
                if i == 1:
                    if coeffs[i] == 1:
                        ans += ' + x'
                    else:
                        ans += ' + ' + str(coeffs[i]) + '*x'
                else:
                    if coeffs[i] == 1:
                        ans += ' + x^' + str(i)
                    else:
                        ans += ' + ' + str(coeffs[i]) + '*x^' + str(i)
        return ans

    def deg(self):
        """Returns the degree of self.

        Self may have leading zeros, so returns the degree ignoring the leading zeros if they exist."""

        coeffs = self._coeffs
        res = len(coeffs) - 1
        if res == 0:
            return res
        index = -1
        while coeffs[index] == 0:
            if index == -len(coeffs):
                return 0
            res -= 1
            index -= 1
        return res

    def leading_zeros(self, other):
        l1 = self._coeffs
        l2 = other._coeffs
        if len(l1) == len(l2):
            return [self, other]
        elif len(l1) > len(l2):
            # add leading zeros
            for i in range(0, len(l1) - len(l2)):
                l2.append(0)
            return [self, Polynomial(l2)]
        else:
            for i in range(0, len(l2) - len(l1)):
                l1.append(0)
            return [Polynomial(l1), other]

    @typecheck
    def __eq__(self, other):
        l1 = self._coeffs
        l2 = other._coeffs
        if len(l1) == len(l2):
            return l1 == l2
        elif len(l1) > len(l2):
            # add leading zeros in order to compare
            for i in range(0, len(l1) - len(l2)):
                l2.append(0)
            return l1 == l2
        else:
            for i in range(0, len(l2) - len(l1)):
                l1.append(0)
            return l1 == l2

    @typecheck
    def __ne__(self, other):
        return not self == other

    @typecheck
    def __add__(self, right):
        newSelfRight = self.leading_zeros(right)
        self, right = newSelfRight[0], newSelfRight[1]
        res = []
        for i in range(len(self._coeffs)):
            res.append(self._coeffs[i] + right._coeffs[i])
        return Polynomial(res)

    @typecheck
    def __sub__(self, right):
        newSelfRight = self.leading_zeros(right)
        self, right = newSelfRight[0], newSelfRight[1]
        res = []
        for i in range(len(self._coeffs)):
            res.append(self._coeffs[i] - right._coeffs[i])
        return Polynomial(res)

    @typecheck
    def __neg__(self):
        return 0 - self

    @typecheck
    def __mul__(self, right):
        n = max(self.deg(), right.deg())
        for i in range(0, 2*n - self.deg()):
            self._coeffs.append(0)
        newSelfRight = self.leading_zeros(right)
        self, right = newSelfRight[0], newSelfRight[1]
        res = []
        for i in range(2*n + 1):
            coef = 0
            for j in range(0, i + 1):
                coef += (self._coeffs[j])*(right._coeffs[i - j])
            res.append(coef)
        return Polynomial(res)

    @typecheck
    def __div__(self, right):
        """This is really // (floor division).

        Returns q such that self = q*right + r where deg(r) < deg(right)."""
        f = self
        g = right
        gdeg = g.deg()
        res = Polynomial(0)
        if g.deg() == 0:
            coeffs = []
            for i in range(f.deg() + 1):
                coeffs.append(f._coeffs[i]/g._coeffs[0])
            res = Polynomial(coeffs)
            return res
        while f.deg() >= g.deg():
            tempLeadCoeff = (f._coeffs[f.deg()])/(g._coeffs[g.deg()])
            tempCoeffs = []
            for i in range(f.deg() - g.deg()):
                tempCoeffs.append(0)
            tempCoeffs.append(tempLeadCoeff)
            temp = Polynomial(tempCoeffs)
            res += temp
            f = f - temp*g # multiplication changes the degree of g
                           # by adding leading 0s
        return res

    def __call__(self, num):
        ans = 0
        for i in range(0, len(self._coeffs)):
            ans += self._coeffs[i]*(num**i)
        return ans

    def __pow__(self, exponent):
        ans = Polynomial(1)
        for i in range(0, exponent):
            ans = ans*self
        return ans
