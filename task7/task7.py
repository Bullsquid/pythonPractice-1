import random as r


def experiment(n):
    success = 0
    for i in range(0, n):
        first = r.randint(1, 6)
        second = r.randint(1, 6)
        if first == 6 or second == 6:
            success += 1
    p = success / float(n)
    return p


# calculate probability for reference
p_theory = 11/36.0
eps = 0.0001

i = 0
p_practice = 0
while True:
    i += 1
    p_practice = experiment(i)
    if abs(p_practice - p_theory) < eps:
        break
print "After {} throws practical probability {} differs from theoretical ({}) less than {}"\
    .format(i, p_practice, p_theory, eps)
