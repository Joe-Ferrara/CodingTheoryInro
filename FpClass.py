
from EuclideanAlgorithm import *
from NumberType import *

@memoize
def PrimeFiniteField( p ):
    class Fp(FieldElement):
        operatorPrecedence = 2

        prime = p

        def __init__(self, val):
            self._val = val % p
            self.field = Fp

        @typecheck
        def __eq__(self, other):
            if self._val == other._val:
                return True
            else:
                return False

        @typecheck
        def __ne__(self, other):
            return not self == other

        def __repr__(self):
            return str(self._val)

        @typecheck
        def __add__(self, right):
            return Fp(self._val + right._val % p)

        @typecheck
        def __sub__(self, right):
            return Fp(self._val - right._val % p)

        def __neg__(self):
            return Fp(-self._val % p)

        @typecheck
        def __mul__(self, right):
            return Fp(self._val * right._val % p)

        def inverse(self):
            if self._val == 0:
                raise ZeroDivisorError('0 does not have an inverse')
            else:
                return Fp(gcd_x_y(self._val, p)[1])

        @typecheck
        def __div__(self, right):
            if right._val == 0:
                raise ZeroDivisorError('cannot divide by 0')
            else:
                return Fp(self._val*((right.inverse())._val))

        def __pow__(self, exponent):
            ans = Fp(1)
            for i in range(0, exponent):
                ans = ans*self
            return ans

        def lift_to_integer(self):
            return self._val

    Fp.__name__ = 'F%i' % (p)

    return Fp
