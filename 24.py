from itertools import product
from string import ascii_uppercase as alp
string = open('24 (1).txt').readline()
d={i: 0 for i  in alp}
for p in product(alp,repeat=3):
    s=''.join(p)
    if s[0]==s[2]:
        d[s[1]]+= string.count(s)
print(d)



