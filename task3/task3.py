import sys, random


def compute(n):
    i = 0
    s = 0
    while i <= n:
        s += random.random()
        i += 1
    return s/n

n = int(sys.argv[1])
print "average of %d random number(s) is %g" % (n, compute(n))
