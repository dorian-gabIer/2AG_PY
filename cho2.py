a = int(input())
g1 = 1
g2 = 1
o1 = a
o2 = a
for i in range(a):
    for j in range(o1): print(' ', end = '')
    for j in range(g1): print('*', end = '')
    o1 = o1 - 1
    g1 = g1 + 2
    print('')
for i in range(a+1):
    for j in range(o2): print(' ', end = '')
    for j in range(g2): print('*', end = '')
    o2 = o2 - 1
    g2 = g2 + 2
    print('')
