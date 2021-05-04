# Для какого наибольшего целого неотрицательного числа А выражение
# (x**2 – 11x + 28 > 0) ∨ (y**2 – 9y + 14 > 0) ∨ (x**2 + y**2 > A)
# тождественно истинно, т.е. принимает значение 1
# при любых целых положительных x и y?


from itertools import product

def f(a,x,y):
    return (x**2 - 11*x + 28 > 0) or (y**2 - 9*y + 14 > 0) or (x**2 + y**2 > a)
for a in range (100,0,-1):
    ok = True
    for x,y in product( range (1,1000),repeat=2):
        if not f(a,x,y):
            ok=False
            break
        if not ok:
           break
    if ok:
        print(a)