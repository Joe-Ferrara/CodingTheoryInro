def gcd_x_y(a, b):
    """returns [g,x,y] such that g = gcd(x,y) and a*x + b*y = g

    we're assuming a and b are positive integers"""
    # we assume a < b
    switch = False
    if b < a:
        temp = a
        a = b
        b = temp
        switch = True
    # do the extended Euclidean algorithm
    q = int(b/a)
    r = b - q*a
    if r == 0:
        return [a, 1-q, 1]
    x0, x1, y0, y1 = 1, -q, 0, 1
    while r != 0:
        g = r
        x = x1
        y = y1
        b = a
        a = r
        q = int(b/a)
        r = b - q*a
        tempx = x1
        tempy = y1
        x1 = x1*(-q) + x0
        y1 = y1*(-q) + y0
        x0 = tempx
        y0 = tempy
    # remember the order
    if switch == True:
        return [g, y, x]
    else: return [g, x, y]
