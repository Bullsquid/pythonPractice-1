import math
import sys


def print_ln(x):
    x = float(x)
    if x > 0:
        print "ln({:g}) = {:g}".format(x, math.log(x))
    else:
        print "ln({:g}) is illegal".format(x)


for r in sys.argv[1:]:
    print_ln(r)
print

for i in range(1, len(sys.argv)):
        print_ln(sys.argv[i])
print

i = 1
while i < len(sys.argv):
    print_ln(sys.argv[i])
    i += 1
print

i = 1
while 1:
    try:
        print_ln(sys.argv[i])
        i += 1
    except LookupError:
        break
print
