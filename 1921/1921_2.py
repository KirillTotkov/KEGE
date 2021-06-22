from functools import lru_cache

def moves(h):
    a,b=h
    return (a+3,b),(a,b+3),(a*2,b),(a,b*2)
@lru_cache(None)


def g(h):
    a,b=h
    def next(*condition):
        return (g(m)in condition for m in moves(h))
    if a+b>=75: return 'W'
    if any(next('W')):return 'P1'
    if all(next('P1')): return 'V1'
    if any(next('V1')):return 'P2'
    if all(next('P1','P2')): return 'V2'
for s in range(1,66):
    print(s,g((9,s)))
