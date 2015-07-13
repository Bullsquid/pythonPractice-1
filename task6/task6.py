import sys


try:
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
except:
    print "Usage:", sys.argv[0], "infile outfile"
    sys.exit(1)

ifile = open(infilename, "r")
ofile = open(outfilename, 'w')


def avg(line):
    sum = 0.0
    for num in line:
        sum += float(num)
    return sum/len(line)


for s in ifile:
    line = s.split()
    a = avg(line)
    for num in line:
        ofile.write("%12.6f" % float(num))
    ofile.write("%12.6f\n" % a)

ofile.close()
