# Для какого наименьшего целого неотрицательного числа А выражение
# (x**2 – 3x + 2 > 0) ∨ (y > x**2+7) ∨ (xy < A)
# тождественно истинно, т.е. принимает значение 1
# при любых целых положительных x и y?


def f(a,x,y):
    return (x**2 - 3*x + 2 > 0) or (y > x**2+7) or (x*y < a)
for a in range (1,1000):
    ok = True
    for x in range (1,1000):
        for y in range (1,1000):
            if f(a,x,y):
                pass
            else:
                ok=False
                break
        if not ok:
            break
    if ok:
        print(a)
        break
