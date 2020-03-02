## TESTING THE Fp class

p = 5
Fp = PrimeFiniteField(5)
a = Fp(2)
print "a is " + str(a)
ainv = a.inv()
print "the inverse of a is " + str(ainv)
b = Fp(3)
print "b is " + str(b)
print "a + b is " + str(a + b)
print "a - b is " + str(a - b)
print "a/b is " + str(a/b)
print "a to the power 4 is " + str(a**4)
