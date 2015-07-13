import sys
import math


try:
    outfilename = sys.argv[1]
except:
    print "Usage:", sys.argv[0], "infile  outfile"
    sys.exit(1)

ofile = open(outfilename, 'w')


def myfunc(y):
    if y >= 0.0:
        return y**5 * math.exp(-y)
    else:
        return 0.0


i = 2
while i+2 <= len(sys.argv):
    pair = sys.argv[i:i+2]
    x = float(pair[0])
    y = float(pair[1])
    fy = myfunc(y)
    ofile.write("%g %12.5e\n" % (x, fy))
    i += 2

ofile.close()
