
# The confusing elegant version. Cannot understand intuition about it but the math makes sense. 
# And this algorithm only make sense after checking and deriving the math.
# this helped: https://zerobone.net/blog/math/extended-euklidean-algorithm/
# gdc in this case is not intuitive between b mod a and a
def gcdExtended(a, b): 
    if a == 0: 
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1 
    y = x1 
    return gcd, x, y



# Most logical EEA version. Was able to reproduce after this vid https://www.youtube.com/watch?v=IwRtISxAHY4
# a and b are tracking x and y coefficients. 
# so to arrive at a or b you need to "make so many steps"
def r_eea2(a, b, ax, ay, bx, by):
    q = a // b
    r = a % b
    if r == 0:
        return b, bx, by

    rx = ax - q * bx
    ry = ay - q * by
    return r_eea2(b, r, bx, by, rx, ry)

# initial values also make sense 
# to arrive at a you need 1 a and 0 b
# to arrive at b you need 0 a and 1 b
# hence 1,0,0,1
def eea2(a, b):
    return r_eea2(a, b, 1, 0, 0, 1)


# iterative version
def iter_eea2(a, b):
    ax, ay = 1, 0
    bx, by = 0, 1
    r = None

    while r != 0:
        q, r = a // b, a % b
        rx, ry = ax - q * bx, ay - q * by
        a, b = b, r
        ax, ay = bx, by
        bx, by = rx, ry

    return a, ax, ay

print(iter_eea2(240, 46))


