import random as r
import sys

n = int(sys.argv[1])
summ = 0
for i in range(0, n):
    rand = r.uniform(-1, 1)
    summ += rand
    print '%.4f' % rand,

avg = summ / n
print '\nAvg: %.4f' % avg
