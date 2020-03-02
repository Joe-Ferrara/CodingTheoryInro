# this is taken from Jeremy Kun's code... say more

# memoize calls to the class constructors for fields
# this helps typechecking by never creating two separate instances of a number class

def memoize(f):
    cache = {}

    def memoizedFunction(*args, **kwargs):
        argTuple = args + tuple(kwargs)
        if argTuple not in cache:
            cache[argTuple] = f(*args, **kwargs)
        return cache[argTuple]

    memoizedFunction.cache = cache
    return memoizedFunction

# type check a binary operation, and silently typecase 0 or 1
def typecheck(f):
    def newF(self, other):
        if (hasattr(other.__class__, 'operatorPrecedence') and other.__class__.operatorPrecedence > self.__class__.operatorPrecedence):
            return NotImplemented

        if type(self) is not type(other):
            try:
                other = self.__class__(other)
            except TypeError:
                message = 'Not able to typecase %s of type %s to type %s in function %s'
                raise TypeError(message % (other, type(other).__name__, type(self).__name__, f.__name__))
            except Exception as e:
                message = 'Type error on arguments %r, %r for function %s. Reason:%s'
                raise TypeError(message % (self, other, f.__name__, type(other).__name__, type(self).__name__, e))

        return f(self, other)

    return newF

# require a subclass to implement +-* neg and to perform typechecks on all of
# the binary operations
# the __init__ must operate when given a single argument, provided that the
# argument is an integer
class RingElement(object):
    operatorPrecedence = 1

    # the 'r'-operators are only used when typecasting ints
    def __radd__(self, other): return self + other
    def __rsub__(self, other): return -self + other
    def __rmul__(self, other): return self * other

# additionally require inverse() on subclass
class FieldElement(RingElement):
    def __truediv__(self, other): return self * other.inverse()
    def __rtruediv__(self, other): return self.invers() * other
    def __div__(self, other): return self.__truediv__(other)
    def __rdiv__(self, other): return self.__rtruediv__(other)
