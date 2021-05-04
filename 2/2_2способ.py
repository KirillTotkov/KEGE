from itertools import *

for x, y, z, w in product(range(2), repeat=4):
    if (((y <= x) or (not (z) and w)) == (w == x)) == False:
        print(x, y, z, w)
